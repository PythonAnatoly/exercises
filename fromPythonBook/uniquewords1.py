#!/usr/bin/env python3.4
'''
Here is a program from a study book that I'm reading.
The programm lists every word and the
number of times it occurs in alphabetical order for all the ﬁles listed on the
command line:
'''

import string
import sys
words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            if len(word) > 2:
                words[word] = words.get(word, 0) + 1
for word in sorted(words):
    print("'{0}' occurs {1} times".format(word, words[word]))
