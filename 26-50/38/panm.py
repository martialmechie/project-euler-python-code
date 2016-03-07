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

def ispanm(n):
    vector = range(1,10)
    cache = []
    for i in vector:
        p=i*n
        digits = digitize(p)
        if set(digits).isdisjoint(cache):
            cache.extend(digits)
        elif set(cache) == set(vector):
            return makenum(cache)
        else:
            return 0

large = 1
num = 1
for i in range(1,9999):
    digits = digitize(i)
    if digits[0]==9 and ispanm(i)>large:
        large = ispanm(i)
        num =i
print large
print i
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
