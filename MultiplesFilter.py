#
#
# Goal: Practice iterating through data with a for loop and building a new list on the fly.
# Your Mission
# Create a list of numbers from 1 to 20.
# Create a second, empty list called multiples_of_three.
# Use a for loop to look at every number in your first list. If a number is perfectly divisible by 3, append it to your second list.
# Print the final multiples_of_three list.
#
#
# 
varlist =[]
index = 0

for i in range(1, 21):
 #   print(i,  index)
    
    varlist.append(index)
    index = index+1 # update index counter
 #  
print(varlist)
    