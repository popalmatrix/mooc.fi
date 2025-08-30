# This program asks for a user's name and handles different responses based on who they are.

# --- Step 1: Get the user's name and format it ---

# The `input()` function prompts the user with a message and waits for them to type.
# Methods are then chained together to format the text for consistent results:
# 1. `.strip()` removes any extra spaces from the beginning or end of the name.
# 2. `.split()` divides the name into a list of words. For a name like "jerry seinfeld", this creates ['jerry', 'seinfeld'].
# 3. `" ".join()` combines those words back into a single string with a single space in between. This fixes issues with multiple spaces.
# 4. `.title()` capitalizes the first letter of each word. For "jerry seinfeld", it becomes "Jerry Seinfeld".
name = " ".join(input("Please tell me your name: ").strip().split()).title()

# --- Step 2: Check the name and perform an action ---

# The `if` statement checks if the formatted name is NOT equal to "Jerry".
# The `!=` operator means "not equal to".
# If the name is anything other than "Jerry", the code inside this block will run.
if name != "Jerry":
    
    # This line asks for the number of soup portions.
    # The `int()` function is crucial, as it converts the text input into a whole number (an integer) that can be used for calculations.
    portions = int(input("How many portions of soup? "))
    
    # This line calculates the total cost. Multiplying a number by a decimal number (a float)
    # automatically makes the result a float.
    cost = 5.90 * portions
    
    # This `print()` statement displays the total cost.
    # The comma (`,`) separates the text string from the `cost` variable.
    print(f"The total cost is {cost}")

# --- Step 3: Print the final message ---

# This print statement is placed OUTSIDE of the `if` block.
# This means it will always be executed, no matter what name is entered.
# It will run whether the `if` condition is true or false.
print("Next please!")
