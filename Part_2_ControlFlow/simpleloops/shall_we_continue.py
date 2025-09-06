# The program uses a 'while True' loop. This is an infinite loop that
# will run over and over until it is specifically told to stop.
while True:
    # This print statement is INSIDE the loop. This means it will run
    # every time the loop repeats. So, you'll see "hi" over and over.
    print("hi")
    
    # This line asks the user for input and stores it in a variable.
    user_response = input("Shall we continue?")
    
    # This 'if' statement checks the user's input.
    if user_response == "no":
        # The 'break' statement is what makes the loop stop. It's used to
        # exit the loop when a specific condition is met.
        break
    
# This print statement is OUTSIDE the loop. It is only executed
# AFTER the loop has been completely exited by the 'break' statement.
# This is why you only see "okay then" once, at the very end.
print("okay then")
