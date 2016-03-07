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
    return sorted(list(set(out)))

def divsum(n):
    x= divisors(n)
    return sum(x[:-1])

abun = []
searchrange=28123
for i in range(1,searchrange+1):
    if divsum(i) > i:
        abun.append(i)

sumabun = []
for i in range(len(abun)):
    for j in abun[i:]:
        sumabun.append(abun[i]+j)

sumabun = sorted(list(set(sumabun)))

index = 0
while sumabun[index] <= searchrange:
    index+=1

abundant_sum = sum(sumabun[:index])
total_sum = searchrange*(searchrange+1)/2

print total_sum-abundant_sum


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
