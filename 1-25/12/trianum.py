"""
Sum of triangle numbers
"""
import time
start_time = time.time()

def numdivisors(number):
    count =1
    ndivisors=1
    powercount=0
    while number != 1:
        count+=1
        while number%count == 0:
            number = number/count
            powercount+=1
        if powercount > 0:
            ndivisors*=(powercount+1)
            powercount=0
    return ndivisors

count = 1
trianglenum = 1
divisors = 500
while numdivisors(trianglenum) <= divisors:
    count+=1
    trianglenum+=count

print trianglenum


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
