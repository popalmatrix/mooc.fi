# --- Configuration ---
# Define the fixed, target length that the final output string must have.
TARGET_LENGTH = 20
# Define the character used to fill the empty space (padding).
PADDING_CHAR = "*"
# ---------------------

# 1. Ask the user for the input string.
text = input("Please type in a string: ")

# 2. Calculate the length of the input string using the len() function.
text_length = len(text)

# 3. Calculate the amount of padding needed.
#    Since we know the input length and the target length (20),
#    we calculate the difference to find the number of asterisks needed.
#    Example: If input is "python" (6 chars), padding_needed = 20 - 6 = 14.
padding_needed = TARGET_LENGTH - text_length

# 4. Create the padding string.
#    Python's string multiplication (*) repeats the character the required number of times.
padding = PADDING_CHAR * padding_needed

# 5. Print the final, formatted string.
#    We use string concatenation (+) to join the padding (asterisks) and the 
#    original text in the correct order, resulting in a string exactly 20 characters long.
print(padding + text)
