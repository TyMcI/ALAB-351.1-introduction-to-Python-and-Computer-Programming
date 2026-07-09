#
#
# Create a script string_fun.py that:
#   Prompts the user for a word.
#   Prints the length of the word.
#   Prints the word in all uppercase.
#   Prints the word repeated 3 times (on the same line or separate lines).
#

# Prompts the user for a word.
Input_Word = input("Please Enter a word: ")


#   Prints the length of the word.
print("Prints the length of the word.", len(Input_Word))

#   Prints the word in all uppercase.
print("Prints UPPER CASE word.", Input_Word.upper())

#   Prints the word repeated 3 times (on the same line or separate lines).
print("\nword 3 times")
for i in range (0,3):
    print(Input_Word)



