#
#
# Implement a simple bubble sort in a script bubble_sort_demo.py:

#   Use a list of unsorted integers (you can use a fixed example list like [64, 25, 12, 22, 11] or a list of random numbers).
#   Implement the bubble sort algorithm using nested loops:
#   Loop through the list elements, and for each element, loop through the list again comparing adjacent pairs.
#  Swap elements if they are in the wrong order.
#   Continue until the list is sorted.
#   Print the list at each pass of the outer loop to show the progress of the sorting.
#   Finally, print the sorted list.
#   This exercise will demonstrate understanding of loops and list indexing.
#
#
#
ENTER_num = 0
BUBLE_list =[]
FIRST_time = True

ENTER_num = int(input("How many numbers to sort: "))

#BUBLE_list = [64, 25, 12, 22, 11]
for i in range(ENTER_num):
    BUBBLE_interger = int(input("Enter number to add to list: "))
    BUBLE_list.append(BUBBLE_interger)

print ("\nOriginal list: ", BUBLE_list) 
# Loop through the list elements, and for each element, 
for x in range(0,len(BUBLE_list)):
    # print ("\noutter Loop: ", x)
    # print ("Current list Item: ", BUBLE_list[x])

# loop through the list again comparing adjacent pairs.
    for i in range(len(BUBLE_list)-1):
        # print ("\n x=",x, " i=", i)
        # print (BUBLE_list)
        # print ("\     Inner Loop", BUBLE_list[i], "and", BUBLE_list[i+1])

        if BUBLE_list[i] > BUBLE_list[i+1]:
            # print ("       \Swap", BUBLE_list[i], "and", BUBLE_list[i+1])
            yy = BUBLE_list[i]
            BUBLE_list[i] = BUBLE_list[i+1]
            BUBLE_list[i+1] = yy
            # print ("       \Swapped", BUBLE_list[i], "and", BUBLE_list[i+1])  


print ("\nSorted list: ", BUBLE_list) 
print()
