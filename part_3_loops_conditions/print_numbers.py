"""Please write a program which prints out all the even numbers between two and thirty, using a loop. Print each number on a separate line."""

# --- Step 1: Initialization ---
# We create a variable called 'number' and give it a starting value of 2.
# This is our starting point because it's the first even number we want to print.
number = 2

# --- Step 2: The Loop Condition ---
# We start a 'while' loop. This loop will continue to run as long as the
# condition inside the parentheses is true.
# The condition 'number < 31' means the loop will run for numbers 2, 4, 6... up to 30.
# When 'number' becomes 32, the condition will be false and the loop will stop.
while (number < 31):
    
    # --- Step 3: The Action ---
    # Inside the loop, we print the current value of our 'number' variable.
    # The first time through, it will print 2. The second time, 4, and so on.
    print(number)
    
    # --- Step 4: The Increment ---
    # This is the most important step for this problem. We increase the value
    # of 'number' by 2. This is shorthand for 'number = number + 2'.
    # By adding 2 each time, we ensure that we are always moving to the next even number.
    number += 2

# Once the loop finishes, the program ends.
