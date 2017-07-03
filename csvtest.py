#!/usr/local/bin/env python

import csv

with open("csv.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[3] == '':
            print "NONE"
        else:
            print row


'''
word = "word"
print word
newword = word[1:]
print newword
'''
