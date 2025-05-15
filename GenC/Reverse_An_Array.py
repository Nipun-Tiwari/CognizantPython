# Prompt the user to enter the number of elements in the array
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the array elements
arr = []

# Loop to take 'n' inputs from the user and append to the list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Display the original array
print("Original array:", arr)

# Reverse the array using slicing [::-1]
reversed_arr = arr[::-1]

# Display the reversed array
print("Reversed array:", reversed_arr)

# 🔍 Explanation of Key Parts:
# arr[::-1]: This is a Python list slicing technique to reverse the array.
# The first colon : means take all elements.
# The second colon : means apply a step.
# -1 means step backward, i.e., from the end to the start.