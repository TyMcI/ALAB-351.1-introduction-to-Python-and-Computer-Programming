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

multiples_of_three =[]
varlist =[]

index = 0

#

for i in range(0, 21):
 #   print(i,  index)
    
    varlist.append(i)
   
    if i % 3 == 0:
        multiples_of_three.append(i)
        

 #  
print("\n")
print("\n list of number 0-20")
print(varlist)

print("")
print("\n Multiples of 3")
print(multiples_of_three)
print()
print()

