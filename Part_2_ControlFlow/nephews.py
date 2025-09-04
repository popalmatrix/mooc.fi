# The goal is to ask for a name and check if it belongs to one of two sets of characters.

# 1. Ask the user for their name and format it correctly.
# The `input()` function gets the user's name as a string.
# The `.title()` method capitalizes the first letter of each word in the string.
# This makes the comparison reliable, as "huey", "Huey", and "HUEY" will all be treated as "Huey".
username = input("Please type in your name: ").title()

# 2. Use a conditional statement to check the name against the lists of nephews.
# We use the `or` operator to check for multiple names in a single condition.
# The `or` operator returns True if at least one of the conditions is True.
if username == "Huey" or username == "Dewey" or username == "Louie":
    print("I think you might be one of Donald Duck's nephews.")
# The `elif` (else if) block is checked only if the first condition was False.
# It checks if the name matches any of Mickey Mouse's nephews.
elif username == "Morty" or username == "Ferdie":
    print("I think you might be one of Mickey Mouse's nephews.")
# The `else` block is the final catch-all. It runs if none of the above conditions were met.
else:
    print("You're not a nephew of any character I know of.")
