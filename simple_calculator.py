#
# Write a Python script simple_calculator.py that:
#  1. Asks the user to input two numbers (use two separate input() calls). Make sure to convert these inputs from strings to integers or floats as needed.
#  2. Asks the user to choose an operation (e.g., addition, subtraction, multiplication, division). This can be a simple prompt like "Choose an operation (+, -, *, /): ".
#  3. Performs the chosen operation on the two numbers.
#  4. Prints the result in a user-friendly way. For example: "7 * 3 = 21" (assuming the user chose 7, 3, and *).
#
# define boolean variable inititial state
# 
ValidOperator = False

# Tries added logic to verify id input was number but was not successful
#   ValidNumber1 = isdigit(Number1)
#   ValidNumber2 = isdigit(Number2)
# Will assume all variable entered are valid as a work around

ValidNumber1  = True
ValidNumber2  = True

print("\n******************************************")
print()
print("\nPart 2: User Interaction and Input")  
print()
print("\n******************************************\n\n")

Number1 = int(input("Input number 1:"))
Number2 = int(input("Input number 2:"))


operation = input("Choose an operation (+, -, *, /): ") 

#
# perform math based on the operator that was entered
#


if operation == "+":
   ValidOperator = True
   result = Number1 + Number2
elif operation == "-":
   ValidOperator = True
   result = Number1 - Number2
elif operation == "/":
    ValidOperator = True
    result = Number1 / Number2
elif operation == "*":
    ValidOperator = True
    result = Number1 * Number2
else :
    print("\n Invalid operation was entered -->", operation)

if ((ValidOperator is True) and (ValidNumber1 is True) and (ValidNumber2 is True)):
    print(Number1, operation, Number2, "equals", result)
else :
    print("\nProblem occured'\n")

print()
print("\n******************************************\n\n")