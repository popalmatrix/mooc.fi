# Write your solution here
# Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number according to the following examples.
number = int(input("Please type in a number: "))

# this checks if the number is less then a specific number then it prints a set of prints
if number < 1000:
    print("This number is smaller than 1000")
if number < 100:
    print("This number is smaller than 100")
if number < 10:
    print("This number is smaller than 10")
if number < 0:
    print("This number is smaller than 0")
print("Thank you!")
