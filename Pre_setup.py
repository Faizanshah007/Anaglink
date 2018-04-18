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
    anaglist.append(jumbleword(w))

for w in list3:
    anaglist.append(jumbleword(w))
    
anaglist.sort(key = len, reverse = True)

csvfile1 = open('4-word.csv','w',newline='')
wt1 = csv.writer(csvfile1)
csvfile2 = open('5-word.csv','w',newline='')
wt2 = csv.writer(csvfile2)
csvfile3 = open('7-word.csv','w',newline='')
wt3 = csv.writer(csvfile3)

for anag in anaglist:

    if(len(str(anag[0])) == 4):
        wt1.writerow([anag[0]])

    elif(len(str(anag[0])) == 5):
        wt2.writerow([anag[0]])

    elif(len(str(anag[0])) == 7):
        wt3.writerow([anag[0]])


csvfile1.close()
csvfile2.close()
csvfile3.close()

def get():
    st = set()
    for anag in anaglist:
        st.add(tuple(anag))
    return st
