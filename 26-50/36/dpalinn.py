"""
How many circular primes are there below one million?
"""
import time
start_time = time.time()
import math

def digitize(n):
    return [int(i) for i in str(n)]
def makenum(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s
def dec_to_bin(x):
    return int(bin(x)[2:])
def ispalindrome(n):
    x= digitize(n)
    if len(x) ==1:
        return True
    elif len(x)%2 == 0:
        i = len(x)/2
        if makenum(x[:i]) == makenum(x[:i-1:-1]):
            return True
    else:
        i = int(math.floor(len(x)/2))
        if makenum(x[:i]) == makenum(x[:i:-1]):
            return True
    return False


check_1=[]
for i in range(1,1000000):
    if ispalindrome(i):
        check_1.append(i)

check1_b = [ dec_to_bin(i) for i in check_1]
check_2 =[]
for i in check1_b:
    if ispalindrome(i):
        index = check1_b.index(i)
        check_2.append(check_1[index])

print sum(check_2)
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
