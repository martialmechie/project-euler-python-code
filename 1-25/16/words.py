"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
 words, how many letters would be used?
"""
import time
start_time = time.time()

import inflect
p = inflect.engine()
netcount = 0

for i in range(1000):
    raw = p.number_to_words(i+1)
    raw = raw.replace(" ", "")
    raw = raw.replace("-", "")
    netcount+= len(raw)

print netcount


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
