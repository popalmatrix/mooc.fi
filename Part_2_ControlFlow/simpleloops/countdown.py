# First, we initialize a variable named 'number' and give it a starting value of 5.
# This variable will be used to track our countdown.
number = 5

# This print statement is OUTSIDE the while loop. This means it will only
# be executed once, right at the start of the program, before the countdown begins.
print("Countdown!")

# We use a 'while True' loop. This creates an infinite loop that will
# run continuously until a specific condition is met to stop it.
while True:
    # This print statement is INSIDE the loop. This is crucial because it means
    # it will run during every cycle of the loop, printing the current value of 'number'.
    print(number)

    # This line subtracts 1 from the current value of 'number'. This is the
    # core logic that makes the countdown work.
    number = number - 1

    # This 'if' statement checks for our stopping condition.
    # It asks, "Has the number reached 0 yet?"
    if number == 0:
        # If the condition is met, the 'break' statement is triggered.
        # The 'break' keyword immediately exits the loop, and the program
        # continues to the first line of code that is outside of the loop.
        break

# This print statement is also OUTSIDE the loop.
# It is only executed AFTER the loop has been completely exited by the 'break' command.
# This is why you only see "Now!" at the very end of the program, after the numbers
# have all been printed.
print("Now!")
