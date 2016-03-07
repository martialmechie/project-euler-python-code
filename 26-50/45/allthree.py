"""
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import time
start_time = time.time()
import math

def ispent(n):
    if math.sqrt((24*n)+1)%6 == 5:
        return True
    return False
def trinum(n):
    return n*(n+1)
def istrinum(n):
    start = int(math.floor(math.sqrt(2*n)))
    if trinum(start) == 2*n:
        return True
    return False

def hex_diff(n):
    return 4*n +1

count = 0
current = 1
index = 1
number =[]
while count <2:
    current += hex_diff(index)
    index+=1
    if ispent(current) and istrinum(current):
        count+=1
        number.append(current)

print number


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
