"""

"""
import time
start_time = time.time()

distict_powers = []

for a in range(2,101):
    for b in range(2,101):
        cache = a**b
        if cache not in distict_powers:
            distict_powers.append(cache)


print len(distict_powers)



print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
