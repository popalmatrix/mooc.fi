number = int(input("Please type in a number: "))

# Check if the number is negative
if number < 0:
    # If it is, multiply it by -1 to get the absolute value
    absolute_value = number * -1
    print(f"The absolute value of this number is {absolute_value}")
else:
    # If the number is zero or positive, it's already its own absolute value
    absolute_value = number
    print(f"The absolute value of this number is {absolute_value}")
