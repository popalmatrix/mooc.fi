# Program: Average Food Expenditure (Exact Values)

# ----------------------------------------
# Step 1: Collect input from the user
# ----------------------------------------
# We use .split() and "".join() so that extra spaces 
# in the input do not cause errors.
cafeteria_meals_per_week = int("".join(input("How many times a week do you eat at the student cafeteria? ").split()))
lunch_price = float("".join(input("The price of a typical student lunch? ").split()))
weekly_grocery_cost = float("".join(input("How much money do you spend on groceries in a week? ").split()))

# ----------------------------------------
# Step 2: Calculate cafeteria cost
# ----------------------------------------
# Multiply the number of cafeteria meals by the price of one meal
cafeteria_weekly_total = cafeteria_meals_per_week * lunch_price

# ----------------------------------------
# Step 3: Calculate total weekly food expenditure
# ----------------------------------------
# This is the sum of groceries + cafeteria meals
weekly_total = weekly_grocery_cost + cafeteria_weekly_total

# ----------------------------------------
# Step 4: Calculate average daily expenditure
# ----------------------------------------
# Divide the weekly total by 7 (since there are 7 days in a week)
daily_average = weekly_total / 7

# ----------------------------------------
# Step 5: Display the results
# ----------------------------------------
# Print with clear formatting. 
# No rounding, so the exact decimal values are shown.
print("\n📊 Average Food Expenditure:")
print(f"  • Daily:  {daily_average} euros")
print(f"  • Weekly: {weekly_total} euros")
