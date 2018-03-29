#To generate 25 phrases.

from itertools import permutations
from nltk.corpus import words
import csv

def meaningful(string):
    return string in words.words()

def jumbleword(wrd):
    testset = set([''.join(p) for p in permutations(wrd)])
    anag = []
    for case in testset:
        if meaningful(case):
            anag.append(case)
    return anag

anaglist = list()
list1=[]
with open('word length 4.csv', 'r') as csvfile:
    rd = csv.reader(csvfile,delimiter=' ',quotechar='|')
    for row in rd:
        list1.append(row[0])


for w in list1:
    anaglist.append(jumbleword(w))

print(anaglist)

