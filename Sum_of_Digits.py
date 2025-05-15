# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Initialize a variable to store the sum
sum_of_digits = 0

# Use a temporary variable to avoid changing the original number
temp = abs(number)  # abs() ensures it works for negative numbers too

# Loop to extract each digit and add it to the sum
while temp > 0:
    digit = temp % 10          # Get the last digit
    sum_of_digits += digit     # Add the digit to the sum
    temp = temp // 10          # Remove the last digit

# Display the result
print("Sum of digits:", sum_of_digits)

#  Explanation of Key Parts:
# % 10: Extracts the last digit of the number.

# // 10: Removes the last digit by integer division.

# abs(): Ensures that the logic works for negative numbers too