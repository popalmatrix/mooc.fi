# Program: Sum and Mean of Four Numbers (handles extra spaces in input)

# Step 1: Ask the user for four numbers
# Use "".join(input().split()) to remove any accidental spaces
num1 = int("".join(input("Number 1: ").split()))
num2 = int("".join(input("Number 2: ").split()))
num3 = int("".join(input("Number 3: ").split()))
num4 = int("".join(input("Number 4: ").split()))

# Step 2: Calculate the sum of all numbers
# Simply add the four numbers together
sum_total = num1 + num2 + num3 + num4

# Step 3: Calculate the mean (average)
# Mean = sum of values / number of values
mean_value = sum_total / 4

# Step 4: Print the results neatly
# f-string embeds variables directly into the output
print(f"The sum of the numbers is {sum_total} and the mean is {mean_value}")
