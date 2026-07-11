#
#Write a script grade_checker.py that:

# Asks the user to input a numeric grade (0-100).
# Uses an if-elif-else structure to convert the numeric grade to a letter grade based on a typical scale:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F
# Prints the letter grade. For example: "Your grade is: B"
# Includes a final message using a conditional expression (for example, if the grade is passing (A-C) congratulate the user, if it is a D or F, encourage them to try again).
# Make sure to handle edge cases (like inputting 100 or 0) so that they fall into the correct letter grade. You can assume the user enters a valid number for this task.

#
user_grade = (int)(input("please input a numeric grade (0-100) "))
User_Letter_grade = ""
low_grade = False

#
if (user_grade >= 90 and user_grade <=100):
    User_Letter_grade = "A"
elif (user_grade >= 80) and (user_grade <=89):
    User_Letter_grade = "B"
elif  (user_grade >= 70 and user_grade <=79):
    User_Letter_grade = "C"
elif  (user_grade >= 60 and user_grade <=69):
    User_Letter_grade = "D"
    low_grade = True
    print("D is a Low_grade: ", low_grade)
elif  (user_grade >= 0 and user_grade <=59):
    User_Letter_grade = "F"
    low_grade = True
else:
    print("Invald grade was entered")
#
#
# print("Low_grade: ", low_grade)
if (low_grade == True):
    print("\nYour grade is Low ",User_Letter_grade, " Please try again to improve your grade. ")
else:
    print("\nYour grade is passing ",User_Letter_grade, " Congratulation!!!!")
#
#
print()
print()
#