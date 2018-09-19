#!/usr/bin/env python3.4

'''
It's a programm from a study book I'm reading.

This program reads in a ﬁle of forenames and a ﬁle
of surnames, creating two lists, and then creates the ﬁle test-names1.txt and
writes 100 random names into it.
'''

import random

def get_forenames_and_surnames():
    forenames = []
    surnames = []
    for names, filename in ((forenames, "data/forenames.txt"),
                            (surnames, "data/surnames.txt")):
        for name in open(filename, encoding="utf8"):
            names.append(name.rstrip())
    return forenames, surnames

forenames, surnames = get_forenames_and_surnames()
fh = open("test-names1.txt", "w", encoding="utf8")
for i in range(100):
    line = "{0} {1}\n".format(random.choice(forenames),
                              random.choice(surnames))
    fh.write(line)
