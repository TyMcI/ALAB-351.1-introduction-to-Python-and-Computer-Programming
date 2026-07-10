# Goal: Spot the difference between logical operators (and, or) which evaluate whole truths, and bitwise operators (&, |) which manipulate raw binary data.
# Your Mission
# Let's pretend we are defining user permissions using binary flags.
# READ = 4 (In binary: 100)
# WRITE = 2 (In binary: 010)
# EXECUTE = 1 (In binary: 001)
# If a user has Read and Write permissions, their combined total is 4 + 2 = 6 (Binary: 110).
# Write a quick script to test if a user with a permission score of 6 has the WRITE permission enabled using the bitwise & (AND) operator.
#
READ = 4     #(In binary: 100)
WRITE = 2    #(In binary: 010)
EXECUTE = 1  #(In binary: 001)
#
#
#Permission_score = 7
Permission_score = (int)(input("enter User Permission:  "))
#
#cl

print(format(Permission_score, '08b'))  # binary Padded
print(format(WRITE, '08b'))   # binary padded
#
#
if (Permission_score & WRITE) == WRITE:
    print("Write permissions")
else:
    print("No WRITE permission")

#
print()
print(format(Permission_score, '08b'))  # binary Padded
print(format(READ, '08b'))   # binary padded
if (Permission_score & READ) == READ:
    print("READ permissions")
  
else:
    print("No READ permission")

#
#
print()
print(format(Permission_score, '08b'))  # binary Padded
print(format(EXECUTE, '08b'))   # binary padded
if (Permission_score & EXECUTE) == EXECUTE:
    print("EXECUTE permissions")
  
else:
    print("No EXECUTE permission")

print()