"""

"""
import time
start_time = time.time()
import math
import itertools

def digitize(n):
    return [int(i) for i in str(n)]

def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = float(s)              # 123
    return s

def isprime(n):
    if n==1:
         return False
    elif n<4:
         return True
    elif n%2==0:
         return False
    elif n<9:
         return True
    elif n%3==0:
         return False
    else:
        r = int(math.floor( math.sqrt(n)))
        f = 5
        while f<=r:
            if n%f==0:
                return False
            if n%(f+2)==0:
                return False
            f=f+6
    return True

def permuts(n):
    seed = digitize(n)
    perm = list(itertools.permutations(seed))
    out = [ list(i) for i in perm]
    return out

for a in range(1000,9998):
    if not isprime(a):
        continue
    for d in range(1,((9999-a)/2)+1):
        if not isprime(a+d):
            continue
        if not isprime(a+(2*d)):
            continue
        match = permuts(a)
        if digitize(a+d) not in match:
            continue
        if digitize(a+(2*d)) not in match:
            continue
        print str(a)+str(a+d)+str(a+(2*d))


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
