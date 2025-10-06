# Get user input for dimensions and convert them immediately to integers.
width = int(input("Width: "))
height = int(input("Height: "))
 
# Initialize the counter variable 'n'. This will track how many rows have been printed.
n = 0

# Start the 'while' loop. The loop continues as long as the counter 'n' 
# is less than the desired 'height'.
while n < height:
    # Print the row: Python's string multiplication creates the row of '#' 
    # characters with the correct 'width' in a single step.
    print("#" * width)
    
    # Increment the counter 'n' by 1. This is crucial—it ensures that the 
    # loop eventually reaches 'height' and stops, preventing an infinite loop.
    n += 1
