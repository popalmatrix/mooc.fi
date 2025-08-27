# =============================================
# Original (broken) code
# =============================================
"""
number = int(input("Please type in the first number: "))
number = int(input("Please type in the second number: "))
number = int(input("Please type in the third number: "))

product = number * number * number  # ❌ Problem: only uses the last input three times

print("The product is", product)
"""
# Explanation:
# 1. Each input overwrites the previous 'number'.
# 2. Multiplying 'number * number * number' only uses the last input.
# 3. The product is wrong because the first two numbers are lost.

# =============================================
# Corrected code with space handling
# =============================================

# Step 1: Initialize the product
product = 1  # multiplication identity

# Step 2: Multiply by each user input
# Use "".join(...split()) to remove extra spaces
num = int("".join(input("Please type in the first number: ").split()))
product *= num

num = int("".join(input("Please type in the second number: ").split()))
product *= num

num = int("".join(input("Please type in the third number: ").split()))
product *= num

# Step 3: Print the final product
print(f"The product is {product}")

# Explanation of improvements:
# 1. Extra spaces in the input (e.g., "  5  ") are removed automatically.
# 2. 'product' accumulates the multiplication correctly.
# 3. Reusing 'num' is safe because we only need the running product.
