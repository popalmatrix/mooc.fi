# The program first asks the user for a password and stores it.
userpass = input("Password: ")

# The 'while True' loop is used to keep asking the user to verify the password.
while True:
    # This line prompts the user to type in the password a second time.
    repeatedpass = input("Repeat Password: ")

    # This 'if' statement checks for the correct password.
    if repeatedpass == userpass:
        # If the passwords match, the 'break' statement is triggered.
        # This immediately exits the loop.
        break
    
    # This line is not inside an 'if' block. It will run every time the loop
    # completes a full cycle and doesn't hit the 'break' statement.
    # This happens only when the passwords DO NOT match.
    print("They do not match!")

# This print statement is outside the loop and only runs after the loop has ended.
print("User account created!")
