# Prompt the user to enter the number of elements in the array
n = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
arr = []

# Loop to take 'n' inputs from the user and append to the list
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

# Check if the array is empty (edge case)
if n == 0:
    print("Array is empty, no largest element.")
else:
    # Initialize largest with the first element of the array
    largest = arr[0]

    # Loop through the array to find the largest element
    for num in arr:
        if num > largest:
            largest = num  # Update largest if current number is greater

    # Display the largest element
    print("The largest element in the array is:", largest)

# 🔍 Explanation of Key Parts:
# The program takes user input for array size and elements.

# It initializes largest to the first element and updates it while traversing the array.

# Edge case handled when array length is zero.

