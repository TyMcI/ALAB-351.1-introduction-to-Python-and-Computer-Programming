#
# Write a script even_sum.py that:

# Uses a for loop to iterate through the numbers 1 to 50.
# Calculates the sum of all even numbers in that range.
# Prints the result as: "The sum of even numbers from 1 to 50 is X." (where X is the calculated sum).
#
Even_Sum=0
#
for Num in range(0, 50):
    if ((Num % 2) == 0):
        Even_Sum = Even_Sum + Num
        print(Num, Num % 2, "The running sum is:", Even_Sum)
      
    
print(Num,"The sum of the even numbers is:", Even_Sum)