# Ask the user for the upper limit
limit = int(input("Upper limit: "))

# Ask the user for the base to multiply by (e.g., 2 for powers of two, 3 for powers of three, etc.)
base = int(input("Base: "))

# Start from 1, which is the first "power" of any base (base^0 = 1)
number = 1

# Continue the loop as long as the number is less than or equal to the limit
while number <= limit:
    print(number)         # Print the current value
    number *= base        # Multiply by the base to get the next value
