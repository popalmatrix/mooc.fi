# The program starts by asking the user for tomorrow's weather forecast.
try:
    # Get the temperature from the user and convert it to a number.
    nextdayweather = float(input("What is the weather forecast for tomorrow in celsius? "))

    # Get the rain forecast from the user.
    # We add two methods to make the user's input more reliable.
    # 1. '.strip()' removes any extra spaces from the beginning or end of the text.
    #    For example, " yes " becomes "yes".
    # 2. '.lower()' converts all the letters to lowercase.
    #    For example, "YES" or "Yes" both become "yes".
    # Combining them ensures that the input " yes " and "YES" will both be correctly read as "yes".
    rain = input("Will it rain? (yes/no) ").strip().lower()

    # --- Clothing Suggestions Based on Temperature ---
    # The code checks these conditions in order. It will execute only the first block that is true.
    if nextdayweather > 20:
        print("Wear jeans and a T-shirt")
    elif nextdayweather > 10:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
    elif nextdayweather > 5:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
    else:
        print("Wear jeans and a T-shirt")
        print("I recommend a jumper as well")
        print("Take a jacket with you")
        print("Make it a warm coat, actually")
        print("I think gloves are in order")

    # --- Rain Suggestion ---
    # This separate 'if' statement adds the umbrella suggestion if it's going to rain.
    if rain == "yes":
        print("Don't forget your umbrella!")

except ValueError:
    print("Invalid input. Please enter a number for the temperature.")
