# 1. Get the user's input string.
string = input("Please type in a string: ") # Assume input is "test"
 
# 2. Initialize the counter 'length'. 
# This variable tracks the desired length of the substring.
length = 1

# The while loop runs as long as the desired length (length) is less than or equal 
# to the total length of the string (4).
while length <= len(string):
    
    # 3. Print the substring using slicing.
    # The slice string[0:length] extracts characters from index 0 up to (but not including) 'length'.
    
    # --- VISUALIZATION ---
    # Iteration 1: length = 1. Slice: string[0:1] -> "t"
    # Iteration 2: length = 2. Slice: string[0:2] -> "te"
    # Iteration 3: length = 3. Slice: string[0:3] -> "tes"
    # Iteration 4: length = 4. Slice: string[0:4] -> "test"
    # ---------------------
    
    print(string[0:length])
    
    # 4. Increment the counter. This advances the loop.
    length += 1
    
# When length becomes 5, the loop condition (5 <= 4) is False, and the program ends.

"""#reverse order for better understanding
    # =========================================================================
# PROGRAM 1: SHORTEST to LONGEST (Ascending Order)
# Example Output: t, te, tes, test
# =========================================================================

print("\n--- Running Program 1: Shortest to Longest ---")
string_asc = input("Please type in a string: ")

# Program 1 Logic:
# FEATURE:         | Program 1 (Shortest -> Longest)
# -----------------|-----------------------------------------------------
# length Start:    | length = 1
# while Condition: | while length <= len(string_asc):
# Counter Change:  | length += 1 (Increment)
# Effect on Slice: | The ending index 'length' GROWS, making the substring longer.

length = 1
while length <= len(string_asc):
    print(string_asc[0:length])
    length += 1
"""    

"""
# =========================================================================
# PROGRAM 2: LONGEST to SHORTEST (Descending Order)
# Example Output: test, tes, te, t
# =========================================================================

print("\n--- Running Program 2: Longest to Shortest ---")
string_desc = input("Please type in a string: ")

# Program 2 Logic:
# FEATURE:         | Program 2 (Longest -> Shortest)
# -----------------|-----------------------------------------------------
# length Start:    | length = len(string_desc)
# while Condition: | while length > 0:
# Counter Change:  | length -= 1 (Decrement)
# Effect on Slice: | The ending index 'length' SHRINKS, making the substring shorter.

length = len(string_desc)
while length > 0:
    print(string_desc[0:length])
    length -= 1"""
