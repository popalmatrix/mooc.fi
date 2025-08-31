"""Program: Convert Fahrenheit to Celsius
This program asks the user for a temperature in Fahrenheit,
converts it to Celsius, and prints the result.
If the Celsius temperature is below 0, it also prints a warning message.
"""

# Ask the user for temperature in degrees Fahrenheit (input is a string, so we convert to int)
fahrenheit = int(input("Please type in a temperature (F): "))

# Apply the conversion formula: Celsius = (Fahrenheit - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9

# Conditional statement to check if the temperature is above or below freezing
if celsius >= 0:
    # Case 1: Celsius is zero or positive
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

elif celsius < 0:  
    # "elif" means "else if". This part only runs if the first 'if' was False
    # In this case, it checks if Celsius is below zero
    print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")  # Extra message for cold temperatures
