"""
Champernowne's Constant
"""
import time
start_time = time.time()
import math

def digitize(n):
    return [int(i) for i in str(n)]

def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s


def fetch_pos(n):
    net = 0
    i=1
    while net < n:
        current = i*9*(10**(i-1))
        net+=current
        i+=1
    return [n-net+current,i-2]

def pos(pos,order):
    x=int(math.floor(pos/(order+1)))
    mod_pos = pos - ((order+1)*x)
    start = 10**order
    if mod_pos == 0:
        return digitize(start+(x-1))[-1]
    else:
        return digitize(start+x)[mod_pos-1]


prod = 1
for i in range(7):
    [position,order]=fetch_pos(10**i)
    prod*= pos(position,order)

print prod

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
