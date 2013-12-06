#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Top Title Words
===================

Top Title Words

Run:
----
$ python top_users.py user-visits_msweb.data

Store:
----
$ python top_users.py user-visits_msweb.data > top_users.data

author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""
from mrjob.job import MRJob
from combine_user_visits import csv_readline
from nltk import word_tokenize

class Toptitlewords(MRJob):


    def extract(self, line_no, line):
        """ Extract users """
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
        if word.isalpha() == True:
            total = sum(word_counts)
            yield word, total


    def distribute(self, word, word_total):
        yield word_total, word


    def aggregate(self, word_total, word):


        yield word_total, list(word)


    def steps(self):
        """
        mapper1: <line, record> => <user_id, business_id>
        reducer1: <user_id, business_id> => <user_id, [business_ids]>
        mapper2: <user_id, [business_ids]> => <KEY, [user_id, business_ids]>
        reducer2: <KEY, [user_id, business_ids]> => <[user_a, user_b], jaccard>
        """
        return [
            self.mr(mapper=self.extract, reducer=self.combine),
            self.mr(mapper=self.distribute, reducer=self.aggregate)
        ]



if __name__ == '__main__':
    # print __doc__
    Toptitlewords.run()

