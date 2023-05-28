
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:02:56 2019

@author: cacer019
"""
import random
die1 = [1,2,3,4,5,6]
die2 = [1,2,3,4,5,6]
count = 0
diecount = [0,0,0,0,0,0,0,0,0,0,0,0]
while count <= 10000:
    if random.choice(die1) + random.choice(die2) == 2:
        diecount[0] = diecount[0] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 3:
        diecount[1] = diecount[1] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 4:
        diecount[2] = diecount[2] + 1
        count + count + 1
    elif random.choice(die1) + random.choice(die2) == 5:
        diecount[3] = diecount[3] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 6:
        diecount[4] = diecount[4] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 7:
        diecount[5] = diecount[5] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 8:
       diecount[6] = diecount[6] + 1
       count = count + 1
    elif random.choice(die1) + random.choice(die2) == 9:
        diecount[7] = diecount[7] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 10:
        diecount[8] = diecount[8] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 11:
        diecount[9] = diecount[9] + 1
        count = count + 1
    elif random.choice(die1) + random.choice(die2) == 12:
        diecount[10] = diecount[10] + 1
        count = count + 1
print('2: {}'.format(diecount[0])) 
print('3: {}'.format(diecount[1]))
print('4: {}'.format(diecount[2]))
print('5: {}'.format(diecount[3]))
print('6: {}'.format(diecount[4]))
print('7: {}'.format(diecount[5]))
print('8: {}'.format(diecount[6])) 
print('9: {}'.format(diecount[7]))
print('10: {}'.format(diecount[8]))
print('11: {}'.format(diecount[9]))    
print('12: {}'.format(diecount[10]))    
    
    
   




    


    
    
    






    
        

