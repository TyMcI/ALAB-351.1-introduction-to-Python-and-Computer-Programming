#
#Goal: Understand how Python uses True and False to make decisions using if, elif, and else.
# Your Mission
# Write a script for a virtual club bouncer. The program should ask the user for their age.
# If they are under 18, print: "Access denied. Too young!"
# If they are between 18 and 20 (inclusive), print: "You can come in, but no drinking!"
# If they are 21 or older, print: "Welcome in! Enjoy your night."
#
print()
print()

# Ask users age
AGE = int(input("What is your age?"))

# calculate if user can center bar and drink
if AGE <18:
    print("\nAccess denied. Too young. Your Age= ", AGE)
elif (AGE >= 18 and AGE <= 20):
    print("\nYou are can come in, but no drinking. Your Age= ", AGE)
elif AGE >21:
    print("Welcome in! Enjoy your night. Your age AGE= ", AGE)
print()


