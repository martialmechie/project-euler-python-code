"""

"""
import time
start_time = time.time()

seed = range(100)

def digitize(n):
    a=n%10
    b=(n-a)/10
    return [b,a]

result_num = []
result_den = []
for i in range(11,100):
    a=digitize(i)
    for j in range(10,i):
        b=digitize(j)
        x = list(set(a)-set(b))
        if len(x) == 1 and a[0]!=a[1]:
            y = list(set(b)-set(x))
            if i*y[0] == j*x[0]:
                result_num.append(j)
                result_den.append(i)

print result_num
print result_den

from numpy import prod
n = prod(result_num)
d= prod(result_den)
print d

from fractions import gcd
print d/gcd(n,d)

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
