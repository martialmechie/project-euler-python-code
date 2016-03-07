"""
What is the smallest odd composite that cannot be written as the
 sum of a prime and twice a square?
"""
import time
start_time = time.time()
import math

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

def isnatural(n):
    if n - math.floor(n) == 0:
        return True
    return False

def isgold(n):
    limit = math.floor(math.sqrt(n/2))
    for i in range(int(limit+1)):
        diff = n - 2*(i**2)
        if diff == 0:
            return True
        elif isprime(diff):
            return True
    return False

found = False
num=3

while not found:
    num+=2
    if not isgold(num):
        found = True
        print num

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
