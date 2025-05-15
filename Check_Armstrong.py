# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Store the original number for comparison later
original = number

# Convert the number to string to count the number of digits
num_str = str(number)
num_digits = len(num_str)

# Initialize the result to 0
sum_of_powers = 0

# Loop through each digit in the number string
for digit_char in num_str:
    digit = int(digit_char)                     # Convert character back to integer
    sum_of_powers += digit ** num_digits        # Raise digit to the power of total digits and add to sum

# Compare the sum of powers with the original number
if sum_of_powers == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

# 🔍 Explanation of Key Parts:
# Armstrong Number Definition: A number is Armstrong if the sum of its digits each raised to the power of the number of digits equals the number itself.
# str(number): Converts the number to a string so we can easily count digits and loop through them.

# digit ** num_digits: Each digit is raised to the total number of digits.
