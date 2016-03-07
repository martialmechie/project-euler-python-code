"""

"""
import time
start_time = time.time()

text = open('data.txt','r')
height =15
numlist = []

for x in range(height): #getting input in handy format
    pull = text.readline()
    pull = pull.replace(" ","")
    numline =[]
    i=0
    while i < len(pull)-1:
        numline.append(int(pull[i:i+2]))
        i+=2
    numlist.append(numline)

def subtria(grid,index): #producs a subtriangle left or right
    out=[]
    if index == 1:
        out = [i[:-1] for i in grid[1:]]
    elif index == 2 :
        out = [i[1:] for i in grid[1:]]
    return out

def sumtria(grid): #recursive algo to get the sums
    size = len(grid)
    if size ==2 : # for when we reach the end
        if grid[1][0] > grid[1][1]:
            return grid[1][0] + grid[0][0]
        else:
            return grid[1][1] + grid[0][0]
    else:
        left=sumtria(subtria(grid,1))+grid[0][0]
        right=sumtria(subtria(grid,2))+grid[0][0]
        return max(left,right)


print sumtria(numlist)


print("--- %s ms ---" %int(round((time.time() - start_time)*1000)))
