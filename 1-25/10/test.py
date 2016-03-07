"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import time
start_time = time.time()

import math
# A function to check for primes
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

sumprime = 17 #below 10
seed = 9
limit = 2e6
check = 0

while seed < limit-2:
    seed+=2
    if seed%3==0:
        continue
    else:
        r = int(math.floor( math.sqrt(seed)))
        f = 5
        check = 1
        while f<=r:
            if seed%f==0:
                check = 0
                break
            if seed%(f+2)==0:
                check = 0
                break
            f=f+6
    if check == 1:
        sumprime += seed
        check = 0

print sumprime

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
