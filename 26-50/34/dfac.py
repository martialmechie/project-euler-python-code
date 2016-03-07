"""
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""
import time
start_time = time.time()

import math

limit = math.factorial(9)*7

def digitize(n):
    return [int(i) for i in str(n)]

def checksum(digit, d_list):
    fac_list = [math.factorial(i) for i in d_list]
    if digit == sum(fac_list):
        return True
    return False

curious = []
for x in range(3,limit):
    digits = digitize(x)
    if x < len(digits)*math.factorial(min(digits)):
        continue
    elif x > len(digits)*math.factorial(max(digits)):
        continue
    else:
        if checksum(x,digits):
            curious.append(x)
            print x

print sum(curious)
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
