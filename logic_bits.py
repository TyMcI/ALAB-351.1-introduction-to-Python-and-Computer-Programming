# Create a short script logic_bits.py that:
#
#   Demonstrates the use of logical operators: for example, ask the user for 
#    two boolean inputs (True/False or 1/0) and show the results of and, or, and not on those inputs.
#   Demonstrates bitwise operators (&, |, ^, ~, <<, >>) on two small integers (for example, 5 and 3). 
#    Print the results in binary form using bin() to show what is happening at the bit level.
#
# Bitwise Operators
#    & (ampersand) ‒ bitwise conjunction --> requires exactly two 1s to provide 1 as the result;
#    | (bar) ‒ bitwise disjunction --> requires at least one 1 to provide 1 as the result;
#    ^ (caret) ‒ bitwise exclusive or (xor) --> requires exactly one 1 to provide 1 as the result.
#    ~ (tilde) ‒ bitwise negation;
#
#
VALID_Bool = False
VALID_Bool2 = False
#
BOOL_1 = True
BOOL_2 = False

#
# VALID_Bool = False
# #
while not VALID_Bool:
    FIRST_bool = input("Enter a First boolean Value (True / False): ")
    if ((FIRST_bool != "True") and (FIRST_bool != "False")):
        print("Invalide entry, Please enter (True or False).")
        continue
    else:
        VALID_Bool = True
        if (FIRST_bool == "True"):
            BOOL_1 = True
        else:
            BOOL_1 = False

while not VALID_Bool2:
    SECOND_bool = input("Enter a Second boolean Value (True / False): ")
    if ((SECOND_bool != "True") and (SECOND_bool != "False")):
        print("    Invalid entry, Please enter (True or False).")
        continue
    else:
        VALID_Bool2 = True
        if (SECOND_bool == "True"):
            BOOL_2 = True
        else:
            BOOL_2 = False     
#
#
# 
print("\n  Bitwise conjunction: ", BOOL_1, "&", BOOL_2, " is -->", BOOL_1 & BOOL_2)
print("  Bitwise disjunction: ", BOOL_1, "|", BOOL_2, " is -->", BOOL_1 | BOOL_2)
print("  Bitwise exclusive or (xor): ", BOOL_1, "^", BOOL_2, " is -->", BOOL_1 ^ BOOL_2)
print("  Bitwise negation: ", BOOL_1, " is -->", not BOOL_1)
print("  Bitwise negation: ", BOOL_2, " is -->", not BOOL_2)
print()


