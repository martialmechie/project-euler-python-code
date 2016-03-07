"""
Find the sum of the digits in the number 100!
"""
import time
start_time = time.time()

import math
num =10
fac = math.factorial(100)

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print sum_digits(fac)

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
