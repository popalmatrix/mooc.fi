# The program asks the user to input a year and then determines if it's a leap year.

# Ask the user for a year and convert the input to an integer.
# The 'input()' function gets a string from the user.
# The 'int()' function converts that string into a whole number.
whatyear = int(input("Please type in a year: "))

# A leap year is a year containing an extra day (February 29th)
# to keep the calendar year synchronized with the astronomical year.
# The rules for determining a leap year are specific and must be checked in a particular order.

# The first and most critical condition is to check if the year is divisible by 400.
# If a year is a multiple of 400, it is a leap year. This is the exception to the next rule.
# The '%' operator is the modulo operator; it gives the remainder of a division.
# If `whatyear % 400 == 0`, it means the year is perfectly divisible by 400.
if whatyear % 400 == 0:
    print(f"The year {whatyear} is a leap year.")
# Use an 'elif' (else if) to check the next condition if the first one is false.
# The second rule states that if a year is divisible by 100, it is NOT a leap year.
# This rule applies to years like 1900 or 2100.
elif whatyear % 100 == 0:
    print(f"The year {whatyear} is not a leap year.")
# The third condition is the most common one. If a year is divisible by 4, it IS a leap year.
# This check is performed only if the year is not divisible by 100.
# The 'elif' ensures that we only get to this point if the previous conditions were not met.
elif whatyear % 4 == 0:
    print(f"The year {whatyear} is a leap year.")
# If none of the above conditions are met, the year is not a leap year.
# The 'else' block catches all other years that don't fit the leap year rules.
else:
    print(f"The year {whatyear} is not a leap year.")
