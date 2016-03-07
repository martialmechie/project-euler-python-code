"""
215 = 32768 and the sum of its digits is
3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""
import time
start_time = time.time()


def doubleit(num):
    out = []
    carry = 0
    for i in num:
        p = (2*i)+carry
        out.append(p%10)
        if p < 10:
            carry = 0
        else:
            carry = (p-(p%10))/10
    while carry > 0:
        out.append(carry%10)
        carry = (carry-(carry%10))/10

    return out

def powerit(num,x):
    out = num
    for i in range(x-1):
        out = doubleit(out)
    return out

digit = powerit([2],1000)
print sum(digit)
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
