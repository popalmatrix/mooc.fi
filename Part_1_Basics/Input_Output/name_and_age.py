# """Please write a program which asks the user for their name and year of birth. 
# The program then prints out a message as follows:"""

from datetime import date   # import date class so we can get the current year

# Ask the user for their name
# "split()" breaks text into words, removing all extra spaces
# "join()" puts it back together with single spaces
# "title()" makes the first letter of each word uppercase (e.g. "john doe" -> "John Doe")
name = " ".join(input("What is your name? ").split()).title()

# Ask the user for their birth year
# Same trick with "split()" and "join()" removes any extra spaces around the number
# Convert the cleaned string into an integer
year = int(" ".join(input("Which year were you born? ").split()))

# Get the current year from the system (so the code always works in future years)
#current_year = date.today().year <this can replace the code under
#since the code requires 2021 we will make current year 2021
current_year = 2021

# Calculate age by subtracting birth year from current year
age = current_year - year

# Print a nice message using f-string (formatted string)
print(f"Hi {name}, you will be {age} years old at the end of the year {current_year}")
