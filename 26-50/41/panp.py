"""
What is the largest n-digit pandigital prime that exists?
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
    s = int(s)              # 123
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

def pandigits(n):
    seed = range(1,n+1)
    perm = list(itertools.permutations(seed))
    out = [ list(i) for i in perm]
    out.reverse()
    return out

max_panp= [0]
digit = 9

while digit >= len(max_panp):
    source = pandigits(digit)
    for i in source:
        if isprime(makenum(i)) and makenum(i) > makenum(max_panp):
            max_panp = i
            print max_panp
            break
    digit-=1


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
