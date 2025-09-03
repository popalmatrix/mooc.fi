# The goal is to compare two words alphabetically and print the one that comes last.

# 1. Ask the user for two words.
# The `input()` function prompts the user to type in a word.
# The user's input is automatically stored as a string, so we can omit the `str()` function.
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

# 2. Use a conditional statement to compare the words.
# Strings can be compared using the same operators as numbers.
# Python compares them character by character based on their ASCII values.
# For example, "banana" > "apple" is True because 'b' comes after 'a'.
# Similarly, "cat" > "car" is True because 't' comes after 'r'.

# We use an `if-elif-else` block to handle the three possible outcomes.
# Check if the first word comes after the second alphabetically.
if word1 > word2:
    # If the condition is true, `word1` is the "greater" word.
    print(f"The word that comes alphabetically last is: {word1}")

# If the first condition is false, check if the second word comes after the first.
elif word2 > word1:
    # If this condition is true, `word2` is the "greater" word.
    print(f"The word that comes alphabetically last is: {word2}")

# If neither word is greater, they must be the same.
else:
    # This block handles the case where the two words are identical.
    print("You gave the same word twice")
