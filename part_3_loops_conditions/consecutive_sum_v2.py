# Ask the user to input a limit value
# The program will keep summing numbers until the total is at least this limit
limit = int(input("Limit: "))

# Start with number 1
number = 1

# Initialize the sum with the first number (1)
sum = 1

# Start building the string with the first number already added
# This avoids needing an if/else structure inside the loop
numbers = "1"

# Keep adding numbers until the running sum is at least the limit
while sum < limit:
    number += 1        # Move to the next number (2, 3, 4, ...)
    sum += number      # Add it to the total sum

    # Add the number to the string, with ' + ' in front
    # f-strings allow inserting variables directly into strings
    numbers += f" + {number}"

# After the loop ends, print the calculation and the result
print(f"The consecutive sum: {numbers} = {sum}")
