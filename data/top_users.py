#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Top Users
===================

Users > 20 visits

Run:
----
$ python top_users.py user-visits_msweb.data

author = "Shreyas"
email = "shreyas@ischool.berkeley.edu"
python_version = "Python 2.7.5 :: Anaconda 1.6.1 (x86_64)"
"""

from mrjob.job import MRJob
from combine_user_visits import csv_readline

class Topusers(MRJob):

    def mapper(self, line_no, line):
        """ Extract users """
        cell = csv_readline(line)

        if cell[0] == 'V':
            yield cell[3], 1

    def reducer(self, user, user_counts):
        total = sum(user_counts)

        if total > 20:
            yield user, total



if __name__ == '__main__':
    Topusers.run()
