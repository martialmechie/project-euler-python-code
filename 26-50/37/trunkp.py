"""
Find the sum of the only eleven primes that are both truncatable from
left to right and right to left.
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

#using prime seive methodology
def prime_list(n):
    natural = range(n)
    prime = []
    composite = []
    for i in natural[2:]:
        if i not in composite:
            prime.append(i)
            hopper = i+i
            while hopper < n :
                if hopper not in composite:
                    composite.append(hopper)
                hopper+=i
    return prime

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

def lefttoright(n):
    digits = digitize(n)
    for i in range(1,len(digits)):
        if not isprime(makenum(digits[i:])):
            return False
    return True

def righttoleft(n):
    digits = digitize(n)
    for i in range(1,len(digits)):
        if  not isprime(makenum(digits[:-i])):
            return False
    return True


trunk_p = []
i = 2
while len(trunk_p) < 15:
    if isprime(i) and lefttoright(i) and righttoleft(i):
        trunk_p.append(i)
        print i
    i+=1

print sum(trunk_p[4:])
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
