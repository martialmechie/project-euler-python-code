"""
Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""
import time
start_time = time.time()

import math

index =2

def cycle_len(n):
    digits= len(str(n))
    seed = 10**digits
    r_list = []
    for i in range(n):
        r = seed%n
        if r in r_list:
            return len(r_list) - r_list.index(r)
        else:
            r_list.append(r)
            seed = 10*r
    return None

cycles = [cycle_len(x) for x in range(1,1000)]


print cycles.index(max(cycles))
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
