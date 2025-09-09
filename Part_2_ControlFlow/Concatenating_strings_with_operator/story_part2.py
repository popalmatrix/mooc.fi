# Initialize two variables: one for the story and one to hold the word from the previous loop iteration.
story = ""
previous_word = ""

# This 'while' loop will continue until a 'break' statement is executed.
while True:
    # All of the code in this block is indented once, making it the body of the 'while' loop.
    word = input("Please type in a word: ")

    # We use an 'if' statement to check if the current word is the same as the previous one.
    # The code that runs if this is true is indented another level.
    if word == previous_word:
        # This 'break' statement is inside the 'if' block. It stops the 'while' loop
        # and prevents the repeated word from being added to the story.
        break
    
    # We use a separate 'if' statement to check for the 'end' condition.
    # This 'if' is at the same indentation level as the one above, indicating they are
    # separate checks within the main loop.
    if word == "end":
        # The 'break' statement here stops the 'while' loop when the word "end" is typed.
        break

    # This line runs if neither of the 'if' conditions above were met.
    # It concatenates the new word and a space to the 'story' string.
    story += word + " "
    
    # This line updates the 'previous_word' variable to be the current word.
    # This is at the same indentation level as the other actions in the main loop body.
    # This is crucial for the next iteration of the loop to be able to check for a repeated word.
    previous_word = word

# The 'print' function is outside the loop's indentation, so it only executes once the loop is finished.
# We use the .strip() method to remove any extra spaces from the end of the story.
print(story.strip())
