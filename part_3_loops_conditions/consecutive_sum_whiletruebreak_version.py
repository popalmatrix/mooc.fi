# Ask the user to enter the limit
limit = int(input("Limit: "))

# Initialize variables
current_sum = 0   # The total sum we're building
number = 1        # Start adding from 1

# This loop runs forever — until we manually break out of it
while True:
    current_sum += number  # Add the current number to the sum
    number += 1            # Move to the next number

    # Check if we've reached or passed the limit
    if current_sum >= limit:
        break  # Exit the loop when the condition is met

# Print the final sum that is equal to or just above the limit
print(current_sum)
