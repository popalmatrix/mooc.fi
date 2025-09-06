# This line asks the user for the first letter and stores it in the 'letter1' variable.
letter1 = str(input("1st letter: "))

# This line asks the user for the second letter.
letter2 = str(input("2nd letter: "))

# This line asks the user for the third letter.
letter3 = str(input("3rd letter: "))

# The best way to find the middle letter is by using a list and sorting it.
# This approach is cleaner, more reliable, and scales easily if you have more letters.
# First, you put the letters into a list:
# letters = [letter1, letter2, letter3]
# Then, you can sort the list alphabetically:
# letters.sort()
# The middle letter will then always be the item at index 1:
# middle = letters[1]


# This section uses a series of nested if-elif-else statements to find the middle letter.
# It is a good exercise in conditional logic, but it's more complex than needed.
# It checks every possible ordering of the three letters to find the one in the middle.

if letter1 > letter2 and letter1 > letter3:
    # This block executes if letter1 is the largest.
    if letter2 > letter3:
        middle = letter2
    else:
        middle = letter3

elif letter2 > letter1 and letter2 > letter3:
    # This block executes if letter2 is the largest.
    if letter1 > letter3:
        middle = letter1
    else:
        middle = letter3

else:
    # This block executes if letter3 is the largest.
    if letter1 > letter2:
        middle = letter1
    else:
        middle = letter2


# The final line prints the letter that was determined to be in the middle.
# If you were to use the list method, this line would be `print("The letter in the middle is " + letters[1])`
print("The letter in the middle is " + middle)
