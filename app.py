
import random 

random.randint(0, 20)

def lis_to_string(items):
    if not items: return
    elif len(items) == 1:
        return items[0]
    else:
        return items[-1], items[-1]
    
# def revise(items):
#     if not items: 
#         return
#     elif len(items) == 1:
#         return
l = ['ths', 'is', 'my', 'day']
output = ['this is my and day']

# ans = lis_to_string(l)

def revise(items):
	if not items:
  	    return 
	elif len(items) == 1:
  	    return items[0]
	else:
		items.insert(-1, 'and')
		return ','.join(items)

ans = revise(l)
print(ans)


      
class Users:
    pass 

user1 = Users()
user2 = Users()

users_list = [user1, user2]
      
      
# extend [3,4]
# pop - remove at end
# insert - a position index
# append - adding an the end
# count - ooccurence of a certain item
    

# [1,2,3,4] 3## [4,5]

import random

def generateflips(numflips):
    head = 0
    tail = 1
    #does work 
    total_value = []
    for i in range(numflips):
    	random_value = random.randint(0, 1)
    	total_value.append(random_value)
    return total_value





def hasstreak(flips, length_of_streaks):
    numstreak = 0
    value = 0
    count = 0
    for i in range(flips):
        
        if count > 0:
            if i == value:
                count = count+1
                
            
            
        
        
		#  string in integer
    
# numberOfStreaks = 0
# for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.



flip = 10

ans = generateflips(flip)
print(ans)

