# PROGRAM GOAL: Print the input string in reverse, character by character.
# METHOD 1: Use positive indices, starting at the last position (Length - 1) and counting down to 0.

input_string = input("Please type in a string: ")

# 1. Initialize the index using the last positive position.
# Since indexing starts at 0, the last index is always len(string) - 1.
positive_index = len(input_string) - 1

# 2. Set the while loop condition.
# We stop when the index is less than 0 (i.e., we have processed index 0).
while positive_index >= 0:
    
    # 3. Access and print the character.
    print(input_string[positive_index])
    
    # 4. Decrement the index.
    # Move one step backward toward the start of the string (index 0).
    positive_index -= 1
