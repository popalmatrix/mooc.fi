# Ask the user for a string and store it in the variable 'word'
word = input("Please type in a string: ")
 
# Check also that the word is at least two characters long,
# so that the second (index 1) and second to last (index -2) characters exist.
# The 'and' operator ensures both conditions must be true:
# 1. len(word) > 1: Guarantees the string is long enough to have a second character.
# 2. word[1] == word[-2]: Compares the character at index 1 (the second) 
#                         with the character at index -2 (the second to last).
if len(word) > 1 and word[1] == word[-2]:
    # If the characters are the same, print a message and show the character itself.
    # We use string concatenation (+) to join the message and the character.
    print("The second and the second to last characters are " + word[1])
# The 'else' block handles all other cases:
# - The string is too short (len(word) is 0 or 1).
# - The characters exist, but they are not the same.
else:
    print("The second and the second to last characters are different")
