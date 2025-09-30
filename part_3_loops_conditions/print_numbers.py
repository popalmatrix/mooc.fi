# Ask the user to enter the upper limit
limit = int(input("Upper limit: "))

# Start from 1, which is the first power of two (2^0)
number = 1

# Loop continues as long as the current number is less than or equal to the limit
while number <= limit:
    # We print the number *before* multiplying it by 2
    # Why? Because the current value of 'number' is still within the allowed limit
    print(number)

    # Now we double the number for the next iteration
    # This way, the next power of two will be checked against the limit before printing
    number *= 2
