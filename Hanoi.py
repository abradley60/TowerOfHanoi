#Creating class for the poles of Hanoi tower 
class Pole:
    def __init__(self,label,disks):
        self.label = label
        self.disks = disks
    
    def addto(self,newdisk):
        self.disks = disks.append(newdisk)
    
    def subtractfrom(self):
        del disks[-1]
    
    def topdisk(self):
        topdisk = self.disks[-1]
        return topdisk


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
    disks.sort(reverse = True)
    A = Pole('A',disks)
    B = Pole('B',[])
    C = Pole('C',[])    

def move(n,f,t):
    #Function move disk from f -> t  
    

def solver(n,f,h,t):
    #n:no. of disks, f:from, h:helper, t:target
    if n == 0:
        pass
    else:
        hanoi(n-1,f,t,h)
        move(n,f,t)
        hanoi(n-1,h,f,t)    

towergenerator()
print(A.disks)


