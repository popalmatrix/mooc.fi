# Program to find the second non-overlapping occurrence of a substring.

# 1. Get User Input
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
 
# 2. Find the First Occurrence
# string.find() returns the starting index of the first match, or -1 if not found.
index1 = string.find(substring)

# Initialize index2 to -1 (default state: second occurrence not found).
index2 = -1

# 3. Search for the Second Occurrence (Conditional on the first existing)
if index1 != -1:
    
    # --- CRITICAL NON-OVERLAPPING LOGIC ---
    # Create a new, shortened string that starts *immediately after* the end of the first match.
    # By slicing the original string, we guarantee the second search won't overlap the first.
    # The slice starts at: (index of first match) + (length of substring).
    # Example: "aaaa" with "aa". index1=0, len=2. New string starts at index 2 (i.e., "aa").
    string = string[index1 + len(substring):]
    
    # Now, search for the substring in this new, shortened string.
    # index2 will store the position of the second match *relative to the start of the new string*.
    index2 = string.find(substring)
 
# 4. Final Output and Index Calculation
if index2 == -1:
    # This covers two failure cases: (1) index1 was -1 (no first match) OR 
    # (2) index1 was found but the search in the shortened string (index2) failed.
    print("The substring does not occur twice in the string.")
else:
    # Success! Calculate the ABSOLUTE index of the second match in the original string.
    # Formula: (Start of the first match) + (Length of the cut-off section) + (Index in the new string)
    absolute_index = index1 + len(substring) + index2
    print("The second occurrence of the substring is at index " + str(absolute_index) + ".")
