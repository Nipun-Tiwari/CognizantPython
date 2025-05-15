# Prompt the user to enter the size of the matrix (n x n)
n = int(input("Enter the size of the square matrix (n): "))

# Initialize an empty matrix
matrix = []

# Take input for each row of the matrix
print("Enter the elements of the matrix row by row (space separated):")
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    # Validate the input row length
    while len(row) != n:
        print(f"Please enter exactly {n} elements.")
        row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

# Display the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Rotate the matrix by 90 degrees clockwise
# Approach: Transpose the matrix and then reverse each row
rotated = []

# Transpose and reverse rows
for i in range(n):
    new_row = []
    for j in range(n - 1, -1, -1):
        new_row.append(matrix[j][i])
    rotated.append(new_row)

# Display the rotated matrix
print("Matrix after 90 degree rotation:")
for row in rotated:
    print(row)

# 🔍 Explanation of Key Parts:
# Transpose: Swap rows with columns — element at [j][i] in original becomes [i][j] in transpose.

# Reverse rows after transpose to achieve 90-degree clockwise rotation.

# Input validation ensures each row has exactly n elements.

