"""Please write a program which asks for the names and ages of two persons. The program should then print out the name of the elder."""

# This is a program that finds out who is older between two people.

# --- 1. Get the information for Person 1 ---
# We use the `input()` function to ask for the first person's name.
# The result is a string, which is perfect for a name.
person1 = input("Person 1: ")

# Now we ask for Person 1's age.
# We use an f-string to include their name in the prompt, making it more personal.
# The `int()` function is crucial here: it converts the user's input from a string to a number,
# which allows us to perform mathematical comparisons later.
age1 = int(input(f"Age of {person1}: "))

# --- 2. Get the information for Person 2 ---
# We repeat the same steps for the second person.
person2 = input("Person 2: ")
age2 = int(input(f"Age of {person2}: "))

# --- 3. Compare the ages using a conditional statement ---
# Your comment: "conditional statements for the ages to be calculated of who is the elder or if they are the same age"
# This is the core logic of the program. We use a single `if-elif-else` block to handle three possible outcomes:

# Check if the first person is older than the second.
if age1 > age2:
    # If the condition is true, this code runs.
    # We use an f-string to print a clear message with the correct name.
    print(f"The elder is {person1}")

# If the first condition was false, we check if the second person is older.
elif age2 > age1:
    # If this condition is true, this code block runs.
    print(f"The elder is {person2}")

# If neither of the above conditions was true, it must mean the ages are equal.
# The `else` block acts as a catch-all for this final possibility.
else:
    # This code runs only if `age1` is not greater than `age2` AND `age2` is not greater than `age1`.
    print(f"{person1} and {person2} are the same age")
