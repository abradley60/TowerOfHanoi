class Disk:
    """
    Disk class.

    The point of this class is to house properties of a disk.
    """
    def __init__(self, size):
        self.size = size
    
    def __lt__(self, other):
        return self.size < other.size

class Pole:

    def __init__(self,label,disks):
        self.label = label
        self.disks = disks
    
    def addto(self,newdisk):
        self.disks.append(newdisk)
        return self.disks
    
    def subtractfrom(self):
        del self.disks[-1]
    
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
    global A,B,C,n
    n   = random.randint(2,20)                   
    disks  = random.sample(range(1,100),n)   
    disks.sort(reverse = True)
    A = Pole('A',disks)
    B = Pole('B',[])
    C = Pole('C',[])    

def move(f,t):
    '''Function move disk from f -> t'''
    d = f.topdisk()
    t.addto(d)
    f = f.subtractfrom()

def solver(n,f,h,t):
    #n:no. of disks, f:from, h:helper, t:target
    if n == 0:
        pass
    else:
        solver(n-1,f,t,h)
        move(f,t)
        solver(n-1,h,f,t)    

towergenerator()
print("Hanoi tower initialised")
print(A.disks)
print(B.disks)
print(C.disks)
print('\n')
solver(n,A,B,C)
print("Hanoi tower solved.")
print(A.disks)
print(B.disks)
print(C.disks)

