"""

"""
import time
start_time = time.time()
import math
def digitize(n):
    return [int(i) for i in str(n)]

def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = long(s)              # 123
    return s

def last_ten(n):
    digits = digitize(n)
    if len(digits) <=10:
        return n
    else:
        return makenum(digits[-10:])

def add(a,b):
    a1 = last_ten(a)
    b1 = last_ten(b)
    return last_ten(a1 + b1)

def product(a,b):   #Let b be small
    a1 = last_ten(a)
    b1 = last_ten(b)
    return last_ten(a*b)

def riseup(n,ex):
    out = n
    for i in range(ex):
        out = product(out,out)
    return out

def power(a1,n):
    if n == 0:
        return long(1)
    elif n == 1:
        return a1
    else:
        exp = int(math.floor(math.log(n,2)))
        extra = n-long(2**exp)
        return product(riseup(a1,exp),power(a1,extra))


out = long(0)
for i in range(1,1001):
    out = add( out,power(long(i),long(i)))
    if i%100 ==0:
        print i,out

print out



print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
