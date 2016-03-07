"""
What is the index of the first term in
the Fibonacci sequence to contain 1000 digits?
"""
import time
start_time = time.time()
import math
def add(a,b):
    out = []
    len_a = len(a)
    len_b = len(b)
    carry = 0
    for i in range(1,len_b+1):
        net = a[-i]+b[-i]+carry
        out.append(net%10)
        if math.floor(net/10):
            carry = int(math.floor(net/10))
        else:
            carry = 0
    if len_a > len_b:
        extra = add([carry],a[:len_a-len_b])
    elif carry !=0 and len_a == len_b:
        extra =[carry]
    else:
        extra = []
    out.reverse()
    return extra + out

x = [1]
y = [1]


digits = len(y)
index =2
while digits<1000:
    x,y = y,add(y,x)
    digits = len(y)
    index+=1

print index


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
