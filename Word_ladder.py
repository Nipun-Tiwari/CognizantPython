from collections import deque

def is_one_letter_diff(word1, word2):
    """
    Helper function to check if two words differ by exactly one letter.
    """
    count_diff = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count_diff += 1
            if count_diff > 1:
                return False
    return count_diff == 1

def word_ladder(begin_word, end_word, word_list):
    """
    Finds the shortest transformation sequence length from begin_word to end_word.
    Returns 0 if no such sequence exists.
    """

    # Convert word_list to a set for O(1) lookups
    word_set = set(word_list)

    # If end_word is not in the list, no possible transformation
    if end_word not in word_set:
        return 0

    # Queue for BFS: stores (current_word, current_length)
    queue = deque([(begin_word, 1)])

    # Visited set to avoid cycles
    visited = set([begin_word])

    while queue:
        current_word, length = queue.popleft()

        # If current word is the end word, return the length
        if current_word == end_word:
            return length

        # Check all words in the word_set to find valid transformations
        for word in list(word_set):
            if is_one_letter_diff(current_word, word) and word not in visited:
                visited.add(word)
                queue.append((word, length + 1))
                word_set.remove(word)  # Remove to prevent revisiting

    # If no transformation found
    return 0

# Taking inputs from the user
begin_word = input("Enter the start word: ").strip()
end_word = input("Enter the end word: ").strip()

# Input word list separated by space
word_list_input = input("Enter the word list (space separated): ").strip()
word_list = word_list_input.split()

# Call the word ladder function
result = word_ladder(begin_word, end_word, word_list)

if result == 0:
    print("No possible transformation sequence found.")
else:
    print(f"Length of shortest transformation sequence: {result}")

# 🔍 Explanation of Key Parts:
# Uses Breadth-First Search (BFS) to find the shortest path in the implicit graph where nodes are words and edges exist if words differ by one letter.

# The helper function is_one_letter_diff checks if two words differ by exactly one character.

# Keeps track of visited words to avoid cycles.

# Converts the word list into a set for efficient membership checking and removal.

# ✅ Data Structure Used:
# Set: For O(1) lookups and removals of words in the dictionary.

# Deque (from collections): To implement BFS queue efficiently.

# Queue: For BFS traversal of possible transformations.

# Let me know if you want the code to print the actualtransformation path instead of just the length.