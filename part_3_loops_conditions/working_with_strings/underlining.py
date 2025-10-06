# Start an infinite loop. This loop will run forever until it encounters a 'break' statement.
while True:
    # Prompt the user for input and store it in the 'string' variable.
    string = input("Please type in a string: ")

    # Check the exit condition: if the user enters an empty string (just presses Enter).
    if string == "":
        # If the condition is met, the 'break' statement immediately stops the loop.
        break

    # If the program reaches this point, the string is not empty.
    
    # 1. Print the input string itself.
    print(string)
    
    # 2. Print the underline:
    #    - len(string) calculates the exact length of the input string.
    #    - The integer result is multiplied by the hyphen character ("-").
    #    - Python's string multiplication creates the required underline (e.g., 5 * "-" results in "-----").
    print(len(string) * "-")
