# Extra-spaces-safe version: handles numbers with spaces in between
# Example input: "  1  2  " → becomes "12"

# Ask for inputs (removing *all* spaces)
num1 = int("".join(input("What is the 1st number: ").split()))
num2 = int("".join(input("What is the 2nd number: ").split()))

# Calculate
sum_total = num1 + num2
product_total = num1 * num2

# Output
print(f"The sum of the numbers: {sum_total}")
print(f"The product of the numbers: {product_total}")
