"""
Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.
"""
import time
start_time = time.time()

def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s


raw = range(1,10)
import itertools


max_len = 4
cache = [0,0,0]
prod_list =[]

for seed in list(itertools.permutations(raw)):
    for i in range(1,5):
        for j in range(1,5):
            cache[0]=makenum(seed[:i])
            cache[1]=makenum(seed[i:i+j])
            cache[2]=makenum(seed[i+j:])
            cache.sort()
            if cache[0]*cache[1] == cache[2]:
                prod_list.append(cache[2])

prod_list = list(set(prod_list))

print sum(prod_list)


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
