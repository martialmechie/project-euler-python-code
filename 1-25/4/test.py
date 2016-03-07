"""
Find the largest palindrome made from the product of two
3-digitnumbers.
"""
import time
start_time = time.time()

maxnum = 999
minnum = 100
bigpalin = 0

searchspace = range(minnum,maxnum+1)
searchspace.reverse()

for num1 in searchspace:
    if num1*maxnum < bigpalin:
        break
    for num2 in searchspace:
        current = num1*num2
        if current < bigpalin:
            break
        testlist = str(current)
        if testlist == testlist[::-1]:
            bigpalin = current

print bigpalin
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
