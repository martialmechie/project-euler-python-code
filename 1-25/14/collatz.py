"""

"""
import time
start_time = time.time()

def lencollatz (n):
    length = 1
    while n > 1:
        if n%2 == 0:
            n=n/2
        else:
            n = 3*n +1
        length+=1
    return length

search = 1000000
chainlen = 0
out =0
for i in range(search):
    x= lencollatz(i+1)
    if x>chainlen:
        chainlen=x
        out = i+1
print out

print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
