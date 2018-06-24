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
    #cnt = 0
    while(True):
        t = fakeprime(l,r,primelist)
        #print('made fakernum ',cnt,'，Miller test start')
        #cnt += 1
        if(Miller_Rabin(t,millerlist)):
            return t

def exgcd(a,b):#ax+by=1
    if(b == 0):
        return a,1,0
    gcd,tmp,y = exgcd(b,a%b)
    x = y
    y = tmp - int(a/b)*y
    return gcd,x,y

def solve_function(a,b,c):#ax + by = c
    gcd,x,y = exgcd(abs(a),abs(b))
    if(c % gcd != 0):
        print(gcd)
        raise Exception
    x *= c
    y *= c
    if(a < 0):
        x = -x
    if(b < 0):
        y = -y
    if(x < 0):
        if(b < 0):
            s = int((abs(x) - b + 1) / b)
        else:
            s = int((abs(x) + b - 1) / b)
        x += s * b
        y -= s * a
    return x,y


def encrypt(message,N,e):
    return quick_pow(message,e,N) % N

def decode(message,N,d):
    return quick_pow(message,d,N) % N

def makekey(l,r):

    primelist=[]
    millerlist=[]
    Erato(100000,primelist)
    Erato(20,millerlist)

    prime1 = make_prime(l,r,primelist,millerlist)
    prime2 = make_prime(l,r,primelist,millerlist)

    N = prime1 * prime2
    ef = (prime1 - 1) * (prime2 - 1)

    del prime1
    del prime2

    l = ef / 10
    r = ef / 3
    
    while(True):
        private_key = random.randint(l,r)*2+1
        if(math.gcd(private_key,ef) == 1):
            break

    public_key,tmp = solve_function(private_key,-ef,1)

    del tmp
    del ef
    
    return N,private_key,public_key


N,private_key,public_key = makekey(10**100,10**101)


t = encrypt(int(input()),N,public_key)
print('加密：',t)
print('解密：',decode(t,N,private_key))
print('公钥：%d\n私钥：%d' % (public_key,private_key))


