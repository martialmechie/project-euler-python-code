"""
What is the largest n-digit pandigital prime that exists?
"""
import time
start_time = time.time()
import math

def trinum(n):
    return n*(n+1)

def istrinum(n):
    start = int(math.floor(math.sqrt(2*n)))
    if trinum(start) == 2*n:
        return True
    return False

f = open('data.txt','r')
text = f.read()
text =  text.replace('"',"")
text =  text.replace(' ',"")
text= text.split(",")

def wordval(input):
    input = input.lower()
    output = 0
    for character in input:
        number = ord(character) - 96
        output+=number
    return output

count = 0
for i in text:
    if istrinum(wordval(i)):
        count+=1

print count
print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
