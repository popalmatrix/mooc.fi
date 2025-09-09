# Initialize an empty string to store the words of the story.
story = ""

# The loop runs indefinitely until a break condition is met.
while True:
    # Prompt the user for a word and store it in the 'word' variable.
    word = input("Please type in a word: ")
    
    # Check if the user has typed the word "end".
    if word == "end":
        # If the word is "end", exit the loop.
        break
    
    # If the word is not "end", add it to the 'story' string.
    # We add a space after each word to separate them.
    story += word + " "

# After the loop breaks, print the completed story.
# The .strip() method is used to remove any trailing whitespace at the end of the story.
print(story.strip())
