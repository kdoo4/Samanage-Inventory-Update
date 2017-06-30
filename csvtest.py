#!/usr/local/bin/env python

import csv

with open("csv.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row[1]

'''
word = "word"
print word
newword = word[1:]
print newword
'''
