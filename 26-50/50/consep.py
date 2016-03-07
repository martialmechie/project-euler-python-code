"""
Which prime, below one-million, can be written as
the sum of the most consecutive primes?
"""
import time
start_time = time.time()
import math

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

length_max = 0
prime_max = 0
origin = 0
max_reach = 100
primes = [2]
i=3
while prime_max < 1000000:
    if isprime(i):
        primes.append(i)
        for j in range(len(primes)-length_max):
            if isprime(sum(primes[j:])):
                prime_max = sum(primes[j:])
                length_max = len(primes[j:])
                origin = primes[j]
                print length_max,prime_max
                break
    i+=2

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
