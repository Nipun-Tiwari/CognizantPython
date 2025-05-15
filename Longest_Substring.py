# Prompt the user to enter a string
s = input("Enter a string: ")

# Dictionary to store the last seen index of each character
last_seen = {}

# Initialize variables
start = 0         # Start index of current substring window
max_length = 0    # Length of longest substring found
max_start = 0     # Starting index of longest substring found

# Loop through each character by its index
for i, char in enumerate(s):
    # If character is seen and is inside the current window, move start to one after last occurrence
    if char in last_seen and last_seen[char] >= start:
        start = last_seen[char] + 1

    # Update the last seen index of the current character
    last_seen[char] = i

    # Update max_length and max_start if longer substring found
    if i - start + 1 > max_length:
        max_length = i - start + 1
        max_start = start

# Extract the longest substring without repeating characters
longest_substring = s[max_start:max_start + max_length]

# Display the result
print("Longest substring without repeating characters:", longest_substring)
print("Length:", max_length)

# 🔍 Explanation of Key Parts:
# Uses a sliding window approach with two pointers (start and i) to track current substring.

# last_seen dictionary remembers the last index of each character to avoid repeats.

# When a repeated character is found inside the current window, shift start pointer.

# Keeps track of the maximum length and substring start index to extract the longest substring at the end.