"""

"""
import time
start_time = time.time()

def spiral_diag(n):
    ulimit = n**2
    llimit = (n-2)**2
    gap = n-1
    out = 0
    for i in range(4):
        llimit+=gap
        out+=llimit
    return out

def diag_sums(n):
    net = 1
    for i in range(n)[1::2]:
        net+=spiral_diag(i+2)
    return net


print diag_sums(1001)
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
