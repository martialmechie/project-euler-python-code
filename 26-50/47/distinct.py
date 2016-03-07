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

def factorize(number):
    factors = []
    powers = []
    count =1
    powercount=0
    while number != 1:
        count+=1
        while number%count == 0:
            number = number/count
            powercount+=1
        if powercount > 0:
            factors.append(count)
            powers.append(powercount)
            powercount=0
    return factors,powers

found =False
num =1
goal =4
while not found:
    num+=1
    f1,p1 = factorize(num)
    if len(f1) != goal:
        continue
    f2,p2 = factorize(num+1)
    if len(f2) != goal:
        continue
    f3,p3 = factorize(num+2)
    if len(f3) != goal:
        continue
    f4,p4 = factorize(num+3)
    if len(f4) != goal:
        continue
    found = True
    print num,num+1,num+2,num+3


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
