"""
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import time
start_time = time.time()
import math
import itertools

def digitize(n):
    return [int(i) for i in str(n)]

def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s

def pandigits(n):
    seed = range(n+1)
    perm = list(itertools.permutations(seed))
    out = [ list(i) for i in perm]
    out.reverse()
    return out

def isprop(digits):
    if digits[0] == 0:
        return False
    if not makenum(digits[1:4])%2 == 0:
        return False
    if not makenum(digits[2:5])%3 == 0:
        return False
    if not makenum(digits[3:6])%5 == 0:
        return False
    if not makenum(digits[4:7])%7 == 0:
        return False
    if not makenum(digits[5:8])%11 == 0:
        return False
    if not makenum(digits[6:9])%13 == 0:
        return False
    if not makenum(digits[7:10])%17 == 0:
        return False
    return True


select= []
digit = 9
source = pandigits(digit)
for i in source:
    if isprop(i):
        select.append(makenum(i))


print sum(select)




print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
