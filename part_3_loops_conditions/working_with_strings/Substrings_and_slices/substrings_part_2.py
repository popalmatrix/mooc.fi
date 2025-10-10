# =========================================================================
# PROGRAM GOAL: Print all substrings that END at the last character,
# from shortest to longest (e.g., "t", "st", "est", "test").
# This version uses the concise string[start:] slicing syntax.
# =========================================================================

# 1. Get the user's input string.
string = input("Please type in a string: ") # Assume input is "test" (Length 4)
 
# 2. Initialize the starting index.
# We set 'start' to the index of the last character (length - 1). 
# For "test", start = 3.
start = len(string) - 1

# 3. The WHILE loop controls the movement of the starting index.
# The loop runs as long as 'start' is a valid index (>= 0).
while start >= 0:
    
    # 4. Print the substring using concise slicing: string[start:]
    # When the END index is omitted (e.g., string[start:]), Python automatically 
    # assumes you mean to go all the way to the end of the string.
    print(string[start:])
    
    # --- SLICE VISUALIZATION for "test" ---
    # start=3: string[3:] -> "t" (Shortest)
    # start=2: string[2:] -> "st"
    # start=1: string[1:] -> "est"
    # start=0: string[0:] -> "test" (Longest)

    # 5. Decrement the start index.
    # Moving 'start' backward (3 -> 2 -> 1 -> 0) increases the length of the 
    # printed substring in each successive iteration.
    start -= 1

# When 'start' becomes -1, the loop terminates.
