# The program starts by initializing a variable 'attempts' to keep track of the number of tries.
attempts = 0

# The 'while True' loop is used to repeatedly ask for a PIN until the correct one is entered.
while True:
    # All code here is part of the 'while' loop. Python uses this indentation level to know
    # that these lines should be executed repeatedly until the loop is broken.
    
    # We increment the 'attempts' counter at the beginning of each loop.
    attempts += 1
    
    # We ask the user to enter their PIN and store it as a string in the 'pin' variable.
    pin = input("PIN: ")
    
    # We check if the entered PIN matches the correct one, "4321".
    if pin == "4321":
        # This code block is indented one level further. This tells Python it should only
        # run if the 'if' condition (pin == "4321") is true.
        
        # We check if this was the first attempt. This is a nested 'if' statement.
        if attempts == 1:
            # This code is indented even further because it's part of the inner 'if'.
            # It only runs if the PIN is correct AND it's the first try.
            print("Correct! It only took you one single attempt!")
        else:
            # This 'else' is at the same indentation level as its 'if' statement.
            # It runs if the PIN is correct, but it wasn't the first attempt.
            print(f"Correct! It took you {attempts} attempts")
            
        # This 'break' statement is at the same level as the inner 'if' and 'else'.
        # This placement ensures it runs only after the correct PIN message is printed,
        # and its job is to exit the main 'while True' loop.
        break
    else:
        # This 'else' is at the same indentation level as the first 'if' statement.
        # This tells Python that this code block should be executed as the alternative
        # when the 'if' condition (pin == "4321") is false.
        
        # This line is indented to show it's part of the 'else' block.
        print("Wrong")
