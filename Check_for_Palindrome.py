# Check_for_Palindrome

# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Convert the string to lowercase to ensure the comparison is case-insensitive
normal = user_input.lower()

# Reverse the string using slicing [::-1]
reversed_str = normal[::-1]

# Check if the original (normalized) string is equal to the reversed one
if normal == reversed_str:
    print("palindrome.")
else:
    print("not palindrome.")

#  Explanation of Key Parts:
# lower(): Used to make the comparison case-insensitive. For example, Radar should be the same as radar.

# [::-1]: Efficient way to reverse a string using slicing.