# """Program that asks the user for a number of days
# and prints out the equivalent number of seconds."""

# Step 1: Ask the user for the number of days
# Use split() and join() to remove any extra spaces
# Then convert the cleaned string to an integer
days = int("".join(input("How many days? ").split()))

# Step 2: Calculate how many seconds are in one day
seconds_in_a_day = 24 * 60 * 60  # 24 hours * 60 minutes * 60 seconds

# Step 3: Calculate total seconds for the given number of days
total_seconds = days * seconds_in_a_day

# Step 4: Print the result
print(f"Seconds in that many days: {total_seconds}")
