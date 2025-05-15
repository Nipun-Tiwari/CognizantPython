# Prompt the user to enter a string to compress
input_str = input("Enter a string to compress: ")

# Initialize an empty result string to store compressed version
compressed_str = ""

# Initialize a count for consecutive characters
count = 1

# Loop through the string characters using index, except the last character
for i in range(len(input_str) - 1):
    # Check if the current character is same as the next character
    if input_str[i] == input_str[i + 1]:
        count += 1  # Increment count if same character
    else:
        # Append the current character and count to compressed string
        compressed_str += input_str[i] + str(count)
        count = 1  # Reset count for next character group

# Append the last character and its count (handle the last group)
compressed_str += input_str[-1] + str(count)

# Display the compressed string
print("Compressed string:", compressed_str)

# 🔍 Explanation of Key Parts:
# The loop compares each character with the next one to count consecutive repeats.

# When the next character differs, it appends the character and count to the result.

# The last character group is added after the loop ends.

# The compressed string format follows the pattern: character + count.