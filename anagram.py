from itertools import permutations
from nltk.corpus import words
import enchant
import random

import csv
print("welcome to anafun.......starting might take couple of minutes")
d = enchant.Dict("en_US")
def meaningful(string):
    return string in words.words()

def jumbleword(wrd):
    testset = set([''.join(p) for p in permutations(wrd)])
    anag1= []
    for case in testset:
        if meaningful(case):
            anag1.append(case)

    return anag1

random_list=list()
def random_word_generator():

    print("random words are")
    with open('word length 4.csv')as f:
        wor = f.read().split()
        for i in range(5):
            chosen_row = random.choice(wor)
            random_list.append(chosen_row)
        #print(random_list)
    with open('word length 5.csv')as f:
        wor = f.read().split()
        for i in range(10):
            chosen_row = random.choice(wor)
            random_list.append(chosen_row)
        #print(random_list)
    with open('wordlength 7.csv')as f:
        wor = f.read().split()
        for i in range(10):
            chosen_row = random.choice(wor)
            random_list.append(chosen_row)
    print(random_list)
def random_word_list():
    with open('new list','w') as f:
        wt = csv.writer(f)
'''def random():
    print("random words are:")
    for i in range(10):
        chosen=random.choice(anaglist)
        print(chosen)




anaglist = list()
list1=[]
with open('word length 4.csv', 'rU') as csvfile:
    rd = csv.reader(csvfile)
    for row in rd:

        list1.append(row[0])
list2=[]
with open('word length 5.csv', 'r') as csvfile:
    rd = csv.reader(csvfile)
    for row in rd:

        list2.append(row[0])

list3 = []
with open('wordlength 7.csv', 'r') as csvfile:
    rd = csv.reader(csvfile)
    for row in rd:
        list3.append(row[0])

    #for i in list1:
        #print(i)
   

for w in list1:
    print("hi")
    anaglist.append(jumbleword(w))
print("list is")
print(anaglist)
print("random")



with open('word length 4.csv','w') as csvfile:
    wt = csv.writer(csvfile)
    for anag in anaglist:
        wt.writerow(anag)
csvfile.close()

'''
#random()




random_word_generator()

