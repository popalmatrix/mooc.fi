"""Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below."""
# 1. Get the string input (the str() call is optional but harmless)
text = str(input("Please type in a string: "))

# 2. Check if the string is long enough (must have at least 2 characters)
if len(text) < 2:
    print("The string is too short to compare the second and second-to-last characters.")

# 3. Proceed with the comparison using correct Python indexing
#    text[1] accesses the second character
#    text[-2] accesses the second-to-last character
elif text[1] == text[-2]:
    # When they are the same, print the actual character (text[1] or text[-2])
    print(f"The second and the second to last characters are {text[1]}")
    
else:
    # When they are different
    print("The second and the second to last characters are different")
