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

def pent_diff(n):
    return (3*n) +1

list_pent = [1]
diff=1e6
i=1
current_diff = 4
while diff  > current_diff :
    new = current_diff + list_pent[-1]
    old = list(reversed(list_pent))
    for x in old:
        if ispent(new-x) and ispent(new+x):
            diff = new - x
            print diff
            break
    i=i+1
    list_pent.append(new)
    current_diff = pent_diff(i)



print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
