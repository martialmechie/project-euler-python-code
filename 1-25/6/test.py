"""

"""
import time
start_time = time.time()

def sum1 (num):
    out=num*(num+1)/2
    return out

def sum2 (num):
    out = num*(num+1)*((2*num)+1)/6
    return out

target = 100
print (sum1(target)**2) - sum2(target)

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
