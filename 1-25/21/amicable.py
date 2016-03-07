"""
sum of amicable pairs below 10000
"""
import time
start_time = time.time()

import math
def divisors(number):
    a = []
    b = []
    count =1
    limit=int(math.floor(math.sqrt(number)))
    while count <= limit:
        if number%count == 0:
            a.append(count)
            b.append(number/count)
        count+=1
    b=list(reversed(b))
    out = a+b
    return out

def divsum(n):
    x= divisors(n)
    return sum(x[:-1])

searchrange=10000
num = range(1,searchrange)
dsum = [ divsum(i) for i in num]
mirror = [divsum(i) for i in dsum]

amicables = []
for x in num:
    if mirror[x-1] == x and x!=dsum[x-1]:
        amicables.append(x)
        amicables.append(dsum[x-1])



print amicables
print sum(amicables)/2
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
