import math
import random
import time

def pt_pd(x):
    if(x <= 2):
        return x == 2
    if(not (x & 1)):
        return False
    r = int(math.sqrt(x + 0.5))
    i = 3
    while(i <= r):
        if(x % i == 0):
            print(i)
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
            
def quick_pow(a,n,p):
    if(n == 1):
        return a
    t = quick_pow(a,n>>1,p) % p
    if((n&1)==1):
        return t * t * a % p
    else:
        return t * t % p

def fakeprime(l,r,primelist):
    while(True):
        t = random.randint(l,r)
        fprime = True
        if(t in primelist):
            return t
        for i in primelist:
            if(t % i == 0):
                fprime = False
                break
        if(fprime):
            return t

def Miller_Rabin(pt,primelist):
    if(pt in primelist):
        return True
    if((pt & 1) == 0):
        return False
    u = pt - 1
    t = 0
    while((u&1)==0):
        u>>=1
        t+=1
    #print(u,t)
    for i in primelist:
        x = quick_pow(i,u,pt)
        for j in range(0,t):
            y = x * x % pt
            #print(x,y)
            if(y == 1 and (x != 1 and x + 1 != pt)):
                return False
            x = y
        if(x != 1):
            return False
    return True

def make_prime(l,r,primelist,millerlist):
    while(True):
        t = fakeprime(l,r,primelist)
        if(Miller_Rabin(t,millerlist)):
            return t

primelist=[]
Erato(10000,primelist)
millerlist=[]
Erato(50,millerlist)

print(make_prime(int(1e200),int(1e201),primelist,millerlist))

#while True:
#    print(pt_pd(int(input())))

#while True:
#    s = input()
#    l = int(s[:s.find(' ')])
#    r = int(s[s.find(' '):])
#    print(make_prime(l,r,primelist,millerlist))
    
