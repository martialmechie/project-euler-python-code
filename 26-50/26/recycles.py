"""
Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""
import time
start_time = time.time()

from decimal import *
getcontext().prec = 5000

x= 7
def inverse(n):
    a=Decimal(1)
    b=Decimal(n)
    raw = str(a/b)
    raw = raw[2:]
    return raw

import re
def big_cycle(string):
    length = 0
    x=0
    y=0
    for y in range(len(string)):
        for x in range(len(string)):
            substring = string[y:x]
            if len(list(re.finditer(substring,string))) > 1  and len(substring) > length:
                match = substring
                length = len(substring)
    return match
r = re.compile(r"(.+?)\1+")

search_range =999
longest = 0
candidate =[]
index=1
"""
for i in range(search_range):
    cycle = r.findall(inverse(i+1))
    if cycle and len(cycle[0]) > longest :
        longest = len(cycle[0])
        candidate = cycle[0]
        index = i+1

print index,"---", longest,"---",candidate
"""
for i in range(900,910):
    out= r.findall(inverse(i+1))
    if out:
        print len(out[0])
        print out[0]
    print inverse(i+1)[:20]
    print "-----------"


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
