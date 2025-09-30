# Ask the user for a limit — this is the minimum total sum we want to reach
limit = int(input("Limit: "))

# Start with a current sum of 0 — nothing has been added yet
current_sum = 0

# Start adding numbers from 1 upwards (1, 2, 3, 4, ...)
number = 1

# The loop will continue as long as the current sum is LESS than the limit
# As soon as the sum is equal to or greater than the limit, the loop stops
while current_sum < limit:
    # Add the current number to the running sum
    current_sum += number

    # Move to the next number for the next iteration
    number += 1

    # 👀 Visualization (for learning purposes):
    # Imagine the loop steps like this if limit = 10:
    # Step 1: number = 1, current_sum = 0 → 0 + 1 = 1
    # Step 2: number = 2, current_sum = 1 → 1 + 2 = 3
    # Step 3: number = 3, current_sum = 3 → 3 + 3 = 6
    # Step 4: number = 4, current_sum = 6 → 6 + 4 = 10
    # Now current_sum == limit, so loop ends

# After the loop ends, current_sum is guaranteed to be >= limit
# We print the final sum that meets or exceeds the user's limit
print(current_sum)
