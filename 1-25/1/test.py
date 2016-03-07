#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import math

numrange = 999

#Creating a function to do the sums
def sumup(range,seed):
	count = math.floor(range/seed)
	return int(seed*count*(count+1)/2)
	
	
#Sum of muliples of 3, 5 and 15
Sum3 = sumup(numrange,3)
Sum5 = sumup(numrange,5)
Sum15 = sumup(numrange,15)


print Sum3+Sum5-Sum15

