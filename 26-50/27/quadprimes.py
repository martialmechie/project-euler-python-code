"""

"""
import time
start_time = time.time()

import math
# A function to check for primes
def isprime(n):
    if n==1 or n ==0:
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
def quad(a,b,x):
    out= x**2 + (a*x) + b
    if out > 0:
        return out
    else:
        return 0
def max_primes(a,b):
    index = 0
    while isprime(quad(a,b,index)):
        index+=1
    return index

max_prime = 0
max_a = 0
max_b =0
search = 999
for a in range(-search+1,search):
    for b in range(-search+1,search):
        now = max_primes(a,b)
        if now > max_prime:
            max_prime = now
            max_a = a
            max_b = b

print max_a,max_b,max_prime
print max_a*max_b


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
