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
    ret = 1
    while(n > 0):
        if((n & 1)==1):
            ret = ret * a % p
        a = a * a % p
        n >>= 1
    return ret
    '''
    if(n == 1):
        return a
    t = quick_pow(a,n>>1,p) % p
    if((n&1)==1):
        return t * t * a % p
    else:
        return t * t % p
    '''
def fakeprime(l,r,primelist):
    while(True):
        t = random.randint(l,r)
        fprime = True
        #if(t in primelist):
        #    return t
        for i in primelist:
            if(t % i == 0):
                fprime = False
                break
        if(fprime):
            return t

def Miller_Rabin(pt,primelist):
    #if(pt in primelist):
    #    return True
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
    cnt = 0
    while(True):
        t = fakeprime(l,r,primelist)
        print('made fakernum ',cnt,'，Miller test start')
        cnt += 1
        if(Miller_Rabin(t,millerlist)):
            return t

start = time.time()

primelist=[]
Erato(100000,primelist)

millerlist1=[]
millerlist2=[]
millerlist3=[]

for i in range(2,10):
    if(pt_pd(i)):
        millerlist1.append(i)
for i in range(10,40):
    if(pt_pd(i)):
        millerlist2.append(i)
#print(len(millerlist1)+len(millerlist2))
for i in range(40,1000):
    if(pt_pd(i)):
        millerlist3.append(i)
while True:
    start = time.time()
    while True:
        pr = make_prime(10**1000,10**1001,primelist,millerlist1)
        print('进行强伪素数测试:')
        if(Miller_Rabin(pr,millerlist2)):
            f = open('bigprime.txt','a')
            f.write("cost:" + str(time.time() - start) + '\n' + str(pr) + '\n\n')
            f.close()
            print("cost:",time.time() - start)
            break
print(pr)
print('All cost:',time.time() - start)
#while True:
#    print(pt_pd(int(input())))

#while True:
#    s = input()
#    l = int(s[:s.find(' ')])
#    r = int(s[s.find(' '):])
#    print(make_prime(l,r,primelist,millerlist))
    
