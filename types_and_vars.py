# 
# Write a Python script types_and_vars.py that does the following:
#   Declares a variable name and assigns it your name as a string.
#   Declares a variable age and assigns it your age as an integer.
#   Declares a variable height and assigns it a floating-point number representing your height in meters.
#   Prints a sentence introducing yourself, for example: "Hello, my name is Alice. I am 20 years old and 1.65 meters tall."
#
name = "Ty"
age = 25
heightInFeet = 5.7
height = heightInFeet * 0.3048

print("\n\nHello, my name is", name, ". I am ", age, " years old and ", height," meters tall.")
print() 

 #  
 # After the introduction sentence, add code that calculates 
 # what your age will be in 5 years and print a sentence stating that. 
 # For example: "In 5 years, I will be 25 years old."
 #    

FutureAge = age+5
print("\nIn 5 years, I will be ", FutureAge, "years old.")
print()

#
# Calculate the area of a rectangle with width = 5.5 and height = 2 
# (you can hardcode these numbers or store them in variables). 
# Print the result in a formatted sentence: "The area of a 5.5 x 2 rectangle is 11.0."
#
width = 5.5
height = 2 
area = width * height

print("\nThe area of a 5.5 x 2 rectangle is ", area)
print()

#
# Demonstrate the use of at least two different arithmetic operators (e.g., +, -, *, /, //, or %) and 
# one string concatenation or repetition (e.g., using + to join strings or * to repeat a string).
#
# Integer division  and Modulo
items = int(input("How many items?"))
groups = int(input("How many item in a groups?")) 

sets = items // groups
remainder = items % groups

print("\nIf you have",items,"items and you divide them into groups of",groups)
print("You will have", sets,"sets")
print("You will have", remainder,"remaining")
print()