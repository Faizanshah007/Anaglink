import random
import csv
def produce():
    '''anag_dict = {}
    for ag in Pre_setup.get():
        anag_dict[ag[0]] = len(ag)
    print(anag_dict)'''
    random_list = list()
    with open('4-word.csv')as f:
        wor = f.read().split()
        for i in range(5):
            chosen_row = random.choice(wor)
            random_list.append(chosen_row)
        
    with open('5-word.csv')as f:
        wor = f.read().split()
        for i in range(10):
            chosen_row = random.choice(wor)
            random_list.append(chosen_row)
    
    with open('7-word.csv')as f:
        wor = f.read().split()
        for i in range(10):
            chosen_row = random.choice(wor)
            random_list.append(chosen_row)
    return random_list

