#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Top Title Words
===================

Top Title Words

Run:
----
$ python top_titlewords.py user-visits_msweb.data

Store:
----
$ python top_titlewords.py user-visits_msweb.data > top_titlewords.data

author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""
from mrjob.job import MRJob
from combine_user_visits import csv_readline
from nltk import word_tokenize

class Toptitlewords(MRJob):


    def extract(self, line_no, line):
        """
        Extract words from title
        """
        cell = csv_readline(line)

        if cell[0] == 'A':
            # title = cell[3]
            # words = title.split(' ')

            # using nltk tokenizer so it splits the titles better
            # as initial split left brackets
            words = word_tokenize(cell[3])

            for w in words:
                yield w.lower(), 1

    def combine(self, word, word_counts):
        """
        Aggregate Counts for each word
        """

        if word.isalpha() == True:
            total = sum(word_counts)
            yield word, total


    def distribute(self, word, word_total):
        """
        Distribute count and words for each count, word combo
        """
        yield word_total, word


    def aggregate(self, word_total, word):
        """
        Aggregate words for each count
        """

        yield word_total, list(set(word))


    def splitter(self, count, word_list):
        """
        Distribute count and words for each count, word combo
        """
        yield "allwords", [count, word_list]


    def assembler(self, _, wordcombolist):
        """
        Aggregate words for each count
        """
        wordcombodict = {}

        for w in wordcombolist:
            wordcombodict[w[0]] = w[1]

        count = 0
        for key in reversed(sorted(wordcombodict.iterkeys())):
            if count < 10:
                yield key, wordcombodict[key]

            count += 1




    def steps(self):
        """
        mapper1: <line, title> => <word, 1>
        reducer1: <word, 1> => <word, count>

        mapper2: <word, count> => <count, word>
        reducer2: <count, word> => <count, [word1, word2, ...>

        mapper2: <count, [word1, word2, ...> => <'allwords', [count, [word1, word2,..]] >
        reducer2: <'allwords', [count, [word1, word2,..]] > => <count, [word1, word2, ...]>

        """
        return [
            self.mr(mapper=self.extract, reducer=self.combine),
            self.mr(mapper=self.distribute, reducer=self.aggregate),
            self.mr(mapper=self.splitter, reducer=self.assembler)
        ]



if __name__ == '__main__':
    # print __doc__
    Toptitlewords.run()

