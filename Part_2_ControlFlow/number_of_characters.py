# This program asks the user for a word and then, if it has more than one
# letter, prints out how many letters it contains.

# The `input()` command prompts the user with the given text.
# The user's typed response is then stored in the `word` variable.
word = input("Please type in a word: ")

# The `if` statement checks a condition. In this case, it uses the `len()` function.
# The `len()` function returns the number of characters in the string `word`.
# The condition `len(word) > 1` is true only if the word has more than one letter.
if len(word) > 1:
    # This block of code is **indented**, which means it will only be executed
    # if the condition in the `if` statement is true.

    # We use an f-string (formatted string literal) to easily combine text
    # with the value of the `len(word)` and `word` variables.
    print(f"There are {len(word)} letters in the word {word}")

# This `print()` command is not indented, so it is outside of the `if` block.
# This means it will always be executed, regardless of the word's length.
print("Thank you!")
