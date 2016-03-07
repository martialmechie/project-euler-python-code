"""

"""
import time
start_time = time.time()

f = open('data.txt','r')
raw = f.read()
raw=raw.replace("\n","")
raw=raw.replace("\"","")
raw=raw.replace(" ","")
raw = raw.split(',')
mid = sorted(raw)

def av(word):
    val =[ord(char) - 96 for char in word.lower()]
    return sum(val)

total =0
for i in range(len(mid)):
    total +=(i+1)*av(mid[i])

print total


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
