# Prompt the user to enter the number of elements in the array
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
arr = []

# Loop to take 'n' inputs from the user and append to the list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Initialize a set to keep track of seen elements
seen = set()

# Variable to store the duplicate number if found
duplicate = None

# Loop through the array to find the duplicate
for num in arr:
    if num in seen:
        duplicate = num  # Duplicate found
        break
    else:
        seen.add(num)  # Add number to seen set if not duplicate

# Display the result
if duplicate is not None:
    print("Duplicate number found:", duplicate)
else:
    print("No duplicate number found")

    
# 🔍 Explanation of Key Parts:
# Uses a set to track numbers already seen while iterating.

# As soon as a number repeats (already in seen), it is identified as a duplicate.

# Stops at the first duplicate found.