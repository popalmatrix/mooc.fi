# The program starts by asking the user for two strings.

# 1. Ask the user for the first string and store it in 'string1'.
# The input() function gets text from the user, and it's always a string (str).
string1 = str(input("Please type in string 1: "))
# The str() conversion here is technically optional, as input() returns a string by default.

# 2. Ask the user for the second string and store it in 'string2'.
string2 = str(input("Please type in string 2: "))

# --- Length Calculation ---

# 3. Use the built-in len() function to find the number of characters in each string.
string1len = len(string1)
string2len = len(string2)

# --- Comparison Logic (If/Elif/Else) ---

# 4. Check if the first string is longer than the second.
if string1len > string2len:
    # If the condition is True, print a message using an f-string for easy variable insertion.
    print(f"{string1} is longer")

# 5. Otherwise, check if the second string is longer than the first.
# The 'elif' (else if) only runs if the first 'if' was False.
elif string1len < string2len:
    print(f"{string2} is longer")

# 6. If neither of the above conditions were True, it means the lengths must be equal.
# The 'else' block catches all remaining possibilities.
else:
    print("The strings are equally long")
