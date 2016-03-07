"""

"""
import time
start_time = time.time()

def num_digits(n):
    return len(str(n))

def max_digits(p):
    x=1
    while num_digits(x*(9**p)) >= x:
        x+=1
    return x-1

def sum_pdigits(n,p):
    raw = str(n)
    praw = [ int(i)**p for i in raw]
    return sum(praw)

powerup = 5
ulimit = max_digits(powerup)
llimit = num_digits(2**powerup)

start = 10**(llimit-1)
stop = 10**(ulimit+1)

pnums = []
for i in range(start,stop):
    if sum_pdigits(i,powerup) == i:
        pnums.append(i)

print pnums
print sum(pnums)





print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
