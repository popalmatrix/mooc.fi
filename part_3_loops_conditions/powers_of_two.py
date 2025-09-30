# Ask the user to enter the upper limit as an integer
limit = int(input("Upper limit: "))

# Start from 1, which is the first power of two
number = 1

# We use a while loop to keep printing numbers as long as they are <= the limit
# This is a controlled loop because we know exactly when it should stop
while number <= limit:
    print(number)        # Print the current power of two
    number *= 2          # Multiply the number by 2 to get the next power of two
