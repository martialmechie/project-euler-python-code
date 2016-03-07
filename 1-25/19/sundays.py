"""
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""
import time
start_time = time.time()

import datetime
count =0
for year in range(1901,2001):
    for month in range(1,13):
        day =1
        cache = datetime.date(year,month,day)
        if cache.weekday() == 6:
            count+=1

print count


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
