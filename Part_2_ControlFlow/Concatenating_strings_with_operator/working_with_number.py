# Part 1: Initializing Variables
# We start by creating variables to store the data we'll collect from the user.
# It's important to set them to an initial value (like 0) so we can add to them later.
# 'numbers' will count the total number of entries.
# 'sum' will store the running total of all the numbers.
# 'positives' will count only the numbers that are greater than zero.
numbers = 0
sum = 0
positives = 0

print("Please type in integer numbers. Type in 0 to finish.")

# Part 2: The Main Loop
# The 'while True' statement creates an infinite loop. This loop will keep
# running forever until it hits a 'break' statement, which we'll define below.
while True:
    try:
        # We ask the user for input and immediately convert it to an integer.
        # The `try-except` block handles cases where the user types non-integer input.
        number = int(input("Number: "))
        
        # This is our 'escape hatch'. When the user types 0, this 'if' statement
        # becomes true, and the 'break' command tells the program to exit the loop.
        if number == 0:
            break
        
        # These lines are only executed if the number is NOT 0.
        # We use the `+=` operator as a shortcut. It means "add the value on the right
        # to the variable on the left". For example, `numbers += 1` is the same as `numbers = numbers + 1`.
        
        # Increment the total count of numbers typed in.
        numbers += 1
        
        # Add the current number to our running total.
        sum += number
        
        # Check if the number is positive. If it is, we increment the 'positives' counter.
        if number > 0:
            positives += 1
            
    except ValueError:
        # If the `int()` conversion fails, this block of code runs.
        # It informs the user of the error and continues the loop.
        print("Invalid input. Please enter an integer.")

# Part 3: Handling the ZeroDivisionError
# We use an `if-else` statement to prevent the error. This is a crucial step!
# We check if 'numbers' is greater than 0. If it is, we know it's safe to perform
# the division for the mean.
if numbers > 0:
    # Print the results.
    print("Numbers typed in", numbers)
    print("The sum of the numbers is", sum)

    # To get the mean (average), we divide the sum by the total count.
    # Python automatically handles floating-point division, so you'll get a decimal answer.
    print("The mean of the numbers is", sum / numbers)

    # The count of negative numbers is the total numbers minus the positive ones.
    print("Positive numbers", positives)
    print("Negative numbers", numbers - positives)
else:
    # If the `if` condition is false (meaning 'numbers' is 0), this 'else' block runs.
    # This prevents the program from crashing and provides a helpful message.
    print("No numbers were entered.")
