"""
What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import time
start_time = time.time()

import math
"""
data = [0,1,2]

def rankit(num_list,rank):
    digits = len(num_list)
    order_list = sorted(num_list)
    if digits < 3:
        if rank == 1:
            return order_list
        elif rank == 2:
            return order_list[::-1]

    else:
        block_size =


print rankit(data,2)
"""
import itertools
data =range(10)
a=itertools.permutations(data)
x=list(a)
print x[999999]

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
