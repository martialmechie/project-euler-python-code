"""
How many different ways can 200 be made using any number
of coins?
"""
import time
start_time = time.time()

coin_val = [1,2,5,10,20,50,100,200]

def max_index (chain,price):
    index = 0
    if chain[-1] <= price:
        return len(chain)-1
    while  chain[index] <= price:
        index+=1
    return index-1
def partial_sum(price,token):
    out = [0]
    current = token
    while price >= current:
            out.append(current)
            current+=token
    return out

def num_ways(chain,price):
    if price == 0:
        return 1
    limit = max_index(chain,price)
    if limit > 0:
        ways = 0
        token = chain[limit]
        for j in partial_sum(price,token):
            ways+=num_ways(chain[:limit],price - j)
        return ways
    else:
        return 1


print(num_ways(coin_val,200))



print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
