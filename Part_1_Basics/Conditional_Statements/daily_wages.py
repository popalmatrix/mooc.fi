"""Daily Wages Calculator (Teachable Version)
This program asks the user for:
1. Hourly wage
2. Hours worked
3. Day of the week

It calculates daily wages as:
- hourly_wage × hours_worked
- On Sundays, the hourly wage is doubled
Finally, it prints the daily wages in the required format.
"""

# Step 1: Ask the user for hourly wage
hourlywage = float(input("What is your hourly wage? "))
# We use float() so the user can enter decimal values (e.g., 15.50)

# Step 2: Ask the user for hours worked today
hoursworked = float(input("How many hours have you worked today? "))

# Step 3: Ask the user for the day of the week
dayoftheweek = str(input("What day of the week is it? "))

# Step 4: Calculate base daily wages (without doubling)
dailywages = hourlywage * hoursworked

# Step 5: Check if today is Sunday
if dayoftheweek.lower() == "sunday":  
    # .lower() converts input to lowercase, so 'Sunday', 'SUNDAY', 'sunday' all work
    dailywages *= 2  # double the daily wages on Sunday

# Step 6: Print the result in the exact format the test expects
print(f"Daily wages: {dailywages} euros")
