"""the old code number = input("Please type in a number: ")
  if number>100
    print("The number was greater than one hundred")
    number - 100
    print("Now its value has decreased by one hundred)
     print("Its value is now"+ number)
 print(number + " must be my lucky number!")
 print("Have a nice day!)"""
#Fixed code
# The program asks for a number, which is converted to an integer.
number = int(input("Please type in a number: "))

# The 'if' block handles numbers greater than 100.
if number > 100:
    print("The number was greater than one hundred")
    print("Now its value has decreased by one hundred")

    # The new value is stored in a separate variable, 'new_number',
    # to avoid overwriting the original variable.
    new_number = number - 100
    print(f"Its value is now {new_number}")
    print(f"{new_number} must be my lucky number!")

# The 'else' block handles all other numbers.
else:
    print(f"{number} must be my lucky number!")
    
# The final print statement is now removed from the main body
# and is included in both conditional blocks, so it only runs when needed.
print("Have a nice day!")
