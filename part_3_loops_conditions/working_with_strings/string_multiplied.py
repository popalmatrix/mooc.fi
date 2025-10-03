# =================================================================================
# Goal: To demonstrate string repetition in Python.
# The program asks for a string and a number, then repeats the string
# that many times.
# For example, if the user enters "Moo" and 3, the output will be "MooMooMoo".
# =================================================================================

# --- Step 1: Get the string to be repeated ---

# input() shows the message in parentheses to the user and waits for them to type.
# The value from input() is ALWAYS a string (text).
# The str() function here is technically not needed, since input() already
# returns a string, but it makes the intention clear.
# The user's text is stored in the 'string' variable.
string = str(input("Please type in a string: "))

# --- Step 2: Get the number of repetitions ---

# We ask the user for a second input, the amount.
# The input is still a string (e.g., if you type 5, Python sees "5").
# The int() function is CRITICAL: it converts the string "5" into the
# integer number 5, which we can use for multiplication.
# This line will cause an error if the user types something that isn't a
# whole number (like "hello" or "3.14").
amount = int(input("Please type in an amount: "))

# --- Step 3: Perform the repetition and print the result ---

# This is the key concept: String Multiplication (or Repetition).
# In Python, using the '*' operator between a string and an integer
# doesn't do math. Instead, it creates a new string by repeating
# the original string 'amount' times.
# For example: "Hi" * 3 results in the new string "HiHiHi".
# The print() function then displays this final, combined string to the screen.
print(string * amount)
