import Pre_setup
import random
import csv
def produce():
    size = 0
    anag = Pre_setup.get()
    random_list = list()
    while( size <= 25 ):
        rnd = random.choice(anag)
        anag.remove(rnd)
        for r in rnd:
            if( size > 25 ):
                break
            random_list.append(r)
            size = size + 1
    random.shuffle(random_list)     
    print(random_list)

    
    return random_list

