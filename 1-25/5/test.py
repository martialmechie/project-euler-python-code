"""
2520 is the smallest number that can be divided by each of the
numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""
import time
start_time = time.time()

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
def allfactors(number):
    f,p=factorize(number)
    for i in range(len(p)):
        while p[i] > 1:
            f.append(f[i])
            p[i]-=1
    return f
minnum=1
maxnum=20
reqnum=1
cache =1
numrange = range(minnum,maxnum+1)
for num in numrange:
    if reqnum%num == 0:
        continue
    current = allfactors(num)
    for i in current:
        if cache%i == 0:
            cache=cache/i
            continue
        reqnum*=i
    cache=reqnum

print reqnum



print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
