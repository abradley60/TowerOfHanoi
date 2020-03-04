#Creating class for the poles of Hanoi tower 
class Pole:
    def __init__(self,label,disks):
        self.label = label
        self.disks = disks
# class Disk:
#     def __init__(self,size):
#         self.size = size 

import random
import numpy as np 

# dlabel = ['disk_']*20
# for i in range(0,20):
#     dlabel[i] = dlabel[i]+str(i+1)


def towergenerator():
    '''Randomise number of disks initialised, assign each disk a 
    unique size denoted by an integer between 0 -> 100.'''
    global A,B,C
    numdisks   = random.randint(0,20)                   
    disks  = random.sample(range(1,100),numdisks)   
    disks.sort()
    A = Pole('A',disks)
    B = Pole('B',[])
    C = Pole('C',[])    
    
        
towergenerator()
print(A.disks)


