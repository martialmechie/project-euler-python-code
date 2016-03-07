"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

seed = 600851475143
factors = []
powers = []

number = seed
count =1
powercount=0
while number != 1:
    count+=1
    while number%count == 0:
        number = number/count
        powercount+=1
    if powercount > 0:
        factors.append(count)
        powers.append(powercount)
        powercount=0

print factors[-1]
