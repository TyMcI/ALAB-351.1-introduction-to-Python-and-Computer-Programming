#
# Write a script list_operations.py that:
#
#   Creates a list of at least 5 integers (you can choose them arbitrarily or ask the user to input numbers to populate the list).
#   Prints the original list.
#   Uses the built-in sorted() function to print a sorted version of the list without modifying the original list.
#   Uses the list’s .sort() method to sort the list in place, then prints the list to show it is now sorted.
#   Adds a new element to the list (append an integer), then prints the updated list.
#   Removes an element from the list (you can remove by value or index), then prints the list again.
#   Uses the reverse() method to reverse the list, then prints the reversed list.
#
#
INTERGER_list =[]

print("\n Please enter 5 numbers")
for i in range(5):
    USER_interger = int(input("Enter number : "))
    INTERGER_list.append(USER_interger)

#
#  Prints the original list.
#
print("\nPrints the original list.")
print (INTERGER_list)

#
# Uses the built-in sorted() function to print a sorted version of the list without modifying the original list.
#
print("\n Uses the built-in sorted() function to print a sorted version of the list without modifying the original list.")
print (sorted(INTERGER_list))


# sort the list in place, then prints content
#
print("\n Use .sort() method to sort the list in place, then prints content")
INTERGER_list.sort()
print (INTERGER_list)

#
# Adds a new element to the list (append an integer), then prints the updated list.
#
print("\n Adds a new element to the list, then prints the updated list")
INTERGER_list.append(int(input("Enter Additional number : ")))
print (INTERGER_list)
print()
#
# Removes an element from the list (you can remove by value or index), then prints the list again.
#
DEL_num = (int(input("Which number should be deleted 0-5: ")))

del INTERGER_list[DEL_num]
print (INTERGER_list)
print()

#
# Uses the reverse() method to reverse the list, then prints the reversed list.
#
print("\n Uses the reverse() method to reverse the list, then prints the reversed list")
INTERGER_list.reverse()
print (INTERGER_list)
print()