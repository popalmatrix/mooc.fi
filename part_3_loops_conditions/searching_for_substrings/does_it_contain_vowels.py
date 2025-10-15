# The program starts by asking the user to input a string of text.
# The user's entire input is stored in the 'user_input' variable.
user_input = input("Please type in a string: ")

# --- Checking for 'a' ---
# The 'in' operator is used here to check if the single-character string "a" 
# exists anywhere within the longer string stored in 'user_input'.
if "a" in user_input:
    print("a found")
else:
    # If the 'in' check is False (meaning "a" is not in the string), 
    # the code executes the 'else' block.
    print("a not found")

# --- Checking for 'e' ---
# A separate check is performed for the vowel 'e'. The checks are independent,
# so the string can contain 'a' but not 'e', or vice versa.
if "e" in user_input:
    print("e found")
else:
    print("e not found")

# --- Checking for 'o' ---
# Finally, the vowel 'o' is checked in the same way.
if "o" in user_input:
    print("o found")
else:
    print("o not found")

# The program finishes execution after printing the results for 'a', 'e', and 'o'.
