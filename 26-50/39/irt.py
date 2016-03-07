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
    s = int(s)              # 123
    return s

def nsols(p):
    c_min = int(p/(math.sqrt(2)+2))
    c_max = int(p/2)
    count = 0
    for c in range(c_min,c_max+1):
        x = p - c
        c2 = c**2
        for a in range(1,int(x/2)+2):
            b=x-a
            if (a**2) + (b**2) == c2:
                count+=1
                break
    return count

maxn = 1
cache = 0
for i in range(10,1000):
    if nsols(i)>maxn:
        maxn = nsols(i)
        cache = i

print maxn,cache

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
