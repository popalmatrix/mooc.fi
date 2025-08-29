# Program: Number of Groups from Students

# ----------------------------------------
# Step 1: Ask for input
# ----------------------------------------
# We use input() to get text from the user.
# Users may accidentally type extra spaces, e.g., "   11   "
# To clean the input:
# 1. .split() breaks the string into a list of "words" (removes spaces)
#    Example: "   11   ".split() -> ['11']
# 2. "".join(...) joins the list back into a string with no spaces
#    Example: "".join(['11']) -> '11'
# 3. int(...) converts the cleaned string to an integer
number_of_students = int("".join(input("How many students on the course? ").split()))
desired_group_size = int("".join(input("Desired group size? ").split()))

# ----------------------------------------
# Step 2: Decide how many groups are needed
# ----------------------------------------
# "%" is the modulus operator → gives the remainder of division
# In math class: number_of_students % desired_group_size == 0
# means "number_of_students is divisible by desired_group_size"
# - If remainder == 0 → students divide evenly → no extra group
# - If remainder != 0 → some students are left → need one extra group
if number_of_students % desired_group_size == 0:
    number_of_groups = number_of_students // desired_group_size
else:
    number_of_groups = (number_of_students // desired_group_size) + 1

# ----------------------------------------
# Step 3: Print all inputs and the result
# ----------------------------------------
# This shows clearly what the user typed and the calculation result
print(f"How many students on the course? {number_of_students}")
print(f"Desired group size? {desired_group_size}")
print(f"Number of groups formed: {number_of_groups}")
