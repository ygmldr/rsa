import math
import random
import time
import numpy as np
#p = [2,3,5,7,11,13]

def pd(x):
    if(x <= 2):
        return x == 2
    if(not (x & 1)):
        return False
    r = int(math.sqrt(x + 0.5))
    i = 3
    while(i <= r):
        if(x % i == 0):
            return False
        i += 2
    return True


def Eratosthenes(Len,l):
    l.clear()
    Boolp = []
    for i in range(0,Len):
        Boolp.append(True)
    for i in range(2,Len):
        if(Boolp[i]):
            l.append(i)
            j = i * i
            while(j < Len):
                Boolp[j] = False
                j += i
                
def Erato(Len,l):
    l.clear()
    Boolp = []
    for i in range(0,Len):
        Boolp.append(True)
    for i in range(2,Len):
        if(Boolp[i]):
            l.append(i)
            j = i * i
            while(j < Len):
                Boolp[j] = False
                j += i

def Erato_np(Len,l):
    l = np.empty(int(Len / math.log(Len) + 10),dtype = np.uint64)
    l[0] = 1
    Boolp = np.ones((Len,0),dtype = np.bool_)
    i = 2
    while(i < Len):
        if(Boolp[i]):
            l[l[0]] = i
            l[0] += 1
            j = i * i
            while(j < Len):
                Boolp[j] = False
                j += i
        i = i + 1
                
def Euler(Len,l):
    l = np.array
    Boolp = []
    for i in range(0,Len):
        Boolp.append(True)
    r = 0
    for i in range(2,Len):
        if(Boolp[i]):
            l.append(i)
            r = r + 1
        for j in range(0,r):
            tmp = i * l[j]
            if(tmp >= Len):
                break
            Boolp[tmp] = False
            if(i % l[j] == 0):
                break
            
l = []
start = time.time()
Erato_np(1000000,l)
#print(l)
print(time.time() - start)
start = time.time()
Erato(1000000,l)
print(time.time() - start)

