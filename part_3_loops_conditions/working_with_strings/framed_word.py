"""Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations."""
# 1. Get the user's input string.
word = input("Word: ")
 
# 2. Print the top frame line (30 asterisks).
print("*" * 30)

# --- Manual Centering Calculation ---

# Total inner space available is 30 (total width) - 2 (for the outer asterisks) = 28.
inner_width = 28 
total_padding = inner_width - len(word)

# Calculate the initial, base amount of spaces for both sides 
# using integer division (//). This effectively rounds down, 
# ensuring the left side gets the smaller or equal share.
spaces_at_start = total_padding // 2
spaces_at_end = spaces_at_start
 
# 3. Handle the 'Odd Length' Centering Rule:
# Check if the total padding needed is odd. This happens when the word length is odd or even, 
# but your logic simplifies this: checking if the *word length* is odd is a good proxy 
# (since 28 is even, an even word length means even total padding, and an odd word length 
# means odd total padding).
if len(word) % 2 != 0:
    # If the total required padding is odd (meaning the word length is odd):
    # The left side got the 'rounded down' amount, so we manually add the extra
    # character to the right side (spaces_at_end) to complete the required total padding.
    spaces_at_end += 1
 
# 4. Print the framed middle line.
# Concatenate: Asterisk + Left Spaces + Word + Right Spaces + Asterisk
print("*" + spaces_at_start * " " + word + spaces_at_end * " " + "*")

# 5. Print the bottom frame line.
print("*" * 30)
