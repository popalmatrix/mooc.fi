# =======================================================================
# PYTHON LEARNING MNEMONICS
# =======================================================================

## 1. Loop Counter Management (for vs. while)

# Goal: Remember which loop type requires manual counter handling.

# ➡️ FOR Loop: The "Free" Loop (Implicit Counter)
# ----------------------------------------------------
# - **Free:** You are **FREE** from manual counter work (it's handled implicitly by the iterator or range()).
# - **Finished:** It's **FINISHED** when the sequence is exhausted (a clear, pre-defined end).

# Example of a 'for' loop using a counter implicitly (via range):
# for i in range(5):
#     # No 'i += 1' needed!
#     print(i)


# ➡️ WHILE Loop: The "Work" Loop (Explicit Counter)
# -----------------------------------------------------
# - **Work:** You have **WORK** to do: You **MUST initialize** the counter AND **update** it (e.g., 'count += 1') inside the loop body.
# - **Wonder:** You have to **WONDER** if it will stop, so you **MUST guarantee** the change happens to avoid an infinite loop.

# Example of a 'while' loop using a counter explicitly:
# count = 0   # <--- Initialization (Work 1/3)
# while count < 5:  # <--- Condition (Wonder)
#     print(count)
#     count += 1  # <--- Update/Increment (Work 2/3)


## 2. Mutability (Changeable vs. Unchangeable)

# Goal: Remember which data types can be changed in place (without creating a new object).

# 🍎 MUTABLE Types: The "Manipulable" Data
# -------------------------------------------
# - **M**anipulate: You can change the object's contents **in place** after creation.
# - Examples: **L**ists, **D**ictionaries, **S**ets.

# Example of Mutable:
# my_list = [1, 2]
# print(id(my_list)) # Print original memory ID
# my_list.append(3) # Change in place
# print(id
