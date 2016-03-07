"""
A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which
a + b + c = 1000.
Find the product abc.

performed arithmetic to reduce the equation
"""
import time
start_time = time.time()

def isint(limit,seed):
    out  = 0
    if (limit/2*(limit-2*seed))%(limit-seed)==0:
        out = 1
    return out
limit=1000
redrange = 292
check = 0
seed = 0
while check <  1 and seed < 292:
    seed+=1
    check = isint(limit,seed)

a= seed
b= (limit/2*(limit-2*a))/(limit-a)
c= 1000 - a - b
print a*b*c


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
