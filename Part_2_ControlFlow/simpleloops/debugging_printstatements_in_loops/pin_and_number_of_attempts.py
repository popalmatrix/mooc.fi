# The program starts by initializing a variable 'attempts' to keep track of the number of tries.
attempts = 0

# The 'while True' loop is used to repeatedly ask for a PIN until the correct one is entered.
while True:
    # We increment the 'attempts' counter at the beginning of each loop.
    attempts += 1
    # We ask the user to enter their PIN and store it as a string in the 'pin' variable.
    pin = input("PIN: ")
    
    # We check if the entered PIN matches the correct one, "4321".
    if pin == "4321":
        # If it's correct, we check if this was the first attempt.
        if attempts == 1:
            # If so, we print a special message for the single attempt.
            print("Correct! It only took you one single attempt!")
        else:
            # Otherwise, we print the message showing the total number of attempts.
            # This is the corrected line. Note the use of the 'f' before the string.
            print(f"Correct! It took you {attempts} attempts")
        # The 'break' statement is executed to stop the loop after a correct PIN is entered.
        break
    else:
        # If the PIN is wrong, we print "Wrong" and the loop continues.
        print("Wrong")
