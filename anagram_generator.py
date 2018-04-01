#To generate 25 phrases.

from itertools import permutations
import enchant
import csv

d = enchant.Dict("en_US")

def meaningful(string):
    return d.check(string)

def jumbleword(wrd):
    testset = set([''.join(p) for p in permutations(wrd)])
    anag = []
    for case in testset:
        if meaningful(case):
            anag.append(case)
    return anag

anaglist = list()
list1=[]
list2=[]
list3=[]
with open('4-word.csv', 'r') as csvfile:
    rd = csv.reader(csvfile)
    for row in rd:
        list1.append(row[0])
csvfile.close()

with open('5-word.csv', 'r') as csvfile:
    rd = csv.reader(csvfile)
    for row in rd:
        list2.append(row[0])
csvfile.close()

with open('7-word.csv', 'r') as csvfile:
    rd = csv.reader(csvfile)
    for row in rd:
        list3.append(row[0])
csvfile.close()

for w in list1:
    anaglist.append(jumbleword(w))

for w in list2:
    print("ok")
    anaglist.append(jumbleword(w))

for w in list3:
    anaglist.append(jumbleword(w))
    
anaglist.sort(key = len, reverse = True)

'''with open('4-word.csv','w',newline='') as csvfile:
    wt = csv.writer(csvfile)
    for anag in anaglist:
        wt.writerow([anag[0]])
csvfile.close()

with open('5-word.csv','w',newline='') as csvfile:
    wt = csv.writer(csvfile)
    for anag in anaglist:
        wt.writerow([anag[0]])
csvfile.close()

with open('7-word.csv','w',newline='') as csvfile:
    wt = csv.writer(csvfile)
    for anag in anaglist:
        wt.writerow([anag[0]])
csvfile.close()'''

for anag in anaglist:
    print(anag)

