"""The program below has some syntactic issues:

print("Are you ready?")
number = int(input("Please type in a number: "))
while number = 0:
print(number)
print("Now!")
Please fix it so that it prints out the following:

Sample output
Are you ready?
Please type in a number: 5
5
4
3
2
1
Now!"""

print("Are you ready?")
number = int(input("Please type in a number: "))

# The loop continues as long as the number is greater than 0.
while number > 0:
    # First, print the current number.
    print(number)
    # Then, decrease the number by 1.
    number -= 1

# This line is printed after the loop has finished.
print("Now!")
