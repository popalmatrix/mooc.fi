# We first prompt the user for a year and store it in a variable called 'initial_year'.
# We also create a separate variable 'year' and assign it the same value.
# We do this so we can keep the original year the user typed in for the final output,
# while using the 'year' variable to perform our calculations.
initial_year = int(input("Year: "))
year = initial_year

# We use a 'while True' loop, which will run indefinitely until a 'break' statement is reached.
# This is a good choice because we don't know ahead of time how many years we need to check
# before finding a leap year.
while True:
    # In each loop, we increment the 'year' variable by 1.
    # This moves us to the next year, which we'll then check to see if it's a leap year.
    year += 1
    
    # This is the core logic for identifying a leap year.
    # It uses a combination of the modulo operator (%) and logical operators (and, or).
    #
    # The first condition, (year % 4 == 0 and year % 100 != 0), checks two things:
    # 1. Is the year evenly divisible by 4? (e.g., 2024, 2028).
    # 2. Is it NOT evenly divisible by 100? (e.g., 1900, 2100 are not leap years, even though they're divisible by 4).
    # The 'and' operator means both of these conditions must be true.
    #
    # The second condition, (year % 400 == 0), is an exception to the first.
    # It checks if the year is evenly divisible by 400 (e.g., 2000, 2400).
    #
    # The 'or' operator combines these two main conditions. This means if either the first
    # condition is true (divisible by 4 but not 100) OR the second condition is true (divisible by 400),
    # then the year is a leap year.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Once we find a leap year, this code block is executed.
        # We print the final message using an f-string to insert the initial year
        # and the newly found leap year. This fulfills the requirement for the exact output format.
        print(f"The next leap year after {initial_year} is {year}")
        
        # Finally, the 'break' statement stops the 'while True' loop from running.
        # This exits the program gracefully once the next leap year has been found and printed.
        break
