"""
How many circular primes are there below one million?
"""
import time
start_time = time.time()
import math
def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s
def digitize(n):
    return [int(i) for i in str(n)]
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
from collections import deque
def rotate(number):
    rotator = deque(number)
    rotations = [number]
    for _i in range(len(number) - 1):
        rotator.rotate()
        rotations += [list(rotator)]
    return rotations

#Creating list of primes below million
prime_list = []
for i in range(2,1000000):
    if isprime(i):
        prime_list.append(i)


circular_list=[]
for i in prime_list:
    marker = 1
    for num in list(rotate(digitize(i))):
        if makenum(num) not in prime_list:
            marker = 0
            break
    if marker == 1:
        circular_list.append(i)
        print i

print len(circular_list)
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
