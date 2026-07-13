# Goal: Use a while loop to keep a program running until a specific logical condition is met.
# Your Mission
# Write a program that continuously asks the user to input a password.
# The loop should only stop if the user types "python123" OR if they have guessed incorrectly 3 times (intruder alert!).
# If they get it right, print: "Access granted."
# If they run out of attempts, print: "Account locked. Try again later."

# Hint: You will need to track two things: the user's current guess and a counter variable that starts at 0 and goes up by 1 every time they guess wrong. Use the and or or logical operators to combine your loop conditions.

Invalid_Attempts=3
Attempts=1
INVALID_pwd = False

n=0
while not INVALID_pwd:
    PASSWORD = input("Please enter your password: ")
    if (PASSWORD == "python123"):
        INVALID_pwd = True
        print("Access Granted!!") 
    else:   
        if (Attempts <3):
            Attempts = Attempts + 1
            print("   Invalid Password. Try again>")
            continue
        else:
            print("   Account locked. Try again later.")
            break
       
        


    


    
