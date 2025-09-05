# This line asks the user for the first letter and stores it in the 'letter1' variable.
letter1 = str(input("1st letter: "))

# This line asks the user for the second letter.
letter2 = str(input("2nd letter: "))

# This line asks the user for the third letter.
letter3 = str(input("3rd letter: "))

# Here we create a list named 'letters' to hold the three letters.
# A list is a type of data structure that can hold multiple items.
letters = [letter1, letter2, letter3]

# The .sort() method is called on the 'letters' list.
# This method sorts the items in the list alphabetically (for letters) or numerically (for numbers).
letters.sort()

# The final line prints the middle letter.
# In a sorted list of three items (at indices 0, 1, and 2), the middle item is always at index 1.
# The `[1]` is used to access or "index" the item at that specific position in the list.
print("The letter in the middle is", letters[1])
