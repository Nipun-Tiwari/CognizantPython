# Prompt the user to enter a string
text = input("Enter a string to count vowels and consonants: ")

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define a set of vowels for quick lookup
vowels = set("aeiouAEIOU")

# Loop through each character in the string
for char in text:
    # Check if the character is an alphabet letter
    if char.isalpha():
        if char in vowels:
            vowel_count += 1  # It's a vowel
        else:
            consonant_count += 1  # It's a consonant

# Display the results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)

# 🔍 Explanation of Key Parts:
# char.isalpha(): Ensures that only letters are counted (ignores digits, spaces, punctuation).

# set("aeiouAEIOU"): A set is used for efficient O(1) lookups to check if a character is a vowel.