# The program finds and prints ONLY the 3-character substring at every match of 'character'.

# 1. Get User Input
word = input("Please type in a word: ")
character = input("Please type in a character: ")
 
# --- Setup Variables ---
word_length = len(word)
MIN_LENGTH = 3

# Initialize the starting index (i).
# 'index' controls the loop and represents the current position we are checking.
index = 0
 
# --- 2. The Main Loop (No Infinite Loop Risk) ---
# The loop continues as long as there are AT LEAST 3 characters remaining from the current 'index'.
# This is the LOOP CONDITION that prevents the infinite loop and the IndexError.
while index + MIN_LENGTH <= word_length:
    
    # 3. The Match Check
    # Check if the character at the current starting position (index) matches the target character.
    if word[index] == character:
        
        # 4. The Action 
        # If a match is found, print the 3-character slice.
        print(word[index:index+3])
        
    # 5. Progression (THE ANTI-INFINITE LOOP STEP)
    # This line is crucial: it moves the 'index' closer to the word_length limit.
    # Because 'index' increases every time, the loop condition (index + 3 <= word_length) 
    # will eventually become false, and the loop will terminate.
    index += 1
