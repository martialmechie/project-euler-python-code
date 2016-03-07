"""
Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.
"""
import time
start_time = time.time()

text = open('data.txt','r')
numlist = text.read()
numlist = numlist.strip('\n')

result = []
carry = 0
addrow = 0

for i in range(49,-1,-1):
    addrow = 0
    for j in range(100):
        addrow+=int(numlist[i+(51*j)])
    result.append((addrow+carry)%10)
    carry = (addrow+carry-result[-1])/10


result.append(carry)
out ="The first 10 digits are "
for x in range(1,10):
    out+=str(result[-x])

print out

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
