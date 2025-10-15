# --- 1. Get User Input ---
# Prompt the user to enter the main string (the 'word') and store it.
word = input("Please type in a word: ")
# Prompt the user for the single character to search for and store it.
character = input("Please type in a character: ")
 
# --- 2. Find the Starting Index ---
# The find() method searches the 'word' for the first match of 'character'.
# It returns the character's position (index) if found, 
# OR it returns -1 if the character is NOT found, which prevents the program from crashing.
index = word.find(character)

# --- 3. The Core Logic Check ---
# The IF statement requires two conditions to be True to print the slice:
#
# Condition 1: index != -1
#   Checks if the character was actually found (i.e., the index is not -1).
#
# Condition 2: len(word) >= index + 3
#   Checks that there are enough characters remaining in the word to form a 3-character slice.
#   - len(word) is the total length.
#   - index + 3 is the *minimum required length* from the start of the word.
if index != -1 and len(word) >= index + 3:
    # If BOTH conditions are met:
    # The slice is printed using the format word[start:end].
    # This extracts the 3 characters starting at 'index' and ending right before 'index + 3'.
    print(word[index:index+3])

# If the conditions are not met (char not found or too close to the end), 
# the program skips the 'print' line and exits, printing nothing, as required.
