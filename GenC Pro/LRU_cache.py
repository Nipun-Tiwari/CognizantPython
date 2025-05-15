from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        # Maximum capacity of the cache
        self.capacity = capacity
        # OrderedDict keeps the order of insertion/access
        self.cache = OrderedDict()

    def get(self, key):
        # Return value if key is present, else -1
        if key not in self.cache:
            print(f"Get({key}): -1 (Not found)")
            return -1
        else:
            # Move the accessed key to the end to mark it as recently used
            self.cache.move_to_end(key)
            print(f"Get({key}): {self.cache[key]}")
            return self.cache[key]

    def put(self, key, value):
        # If key exists, update the value and mark it recently used
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            print(f"Put({key}, {value}): Updated existing key.")
        else:
            # Insert new key-value pair
            self.cache[key] = value
            print(f"Put({key}, {value}): Added new key.")

        # If capacity exceeded, remove least recently used item (first item)
        if len(self.cache) > self.capacity:
            removed_key, removed_value = self.cache.popitem(last=False)
            print(f"Cache capacity exceeded. Removed least recently used item: ({removed_key}, {removed_value})")

    def display(self):
        # Display current state of the cache
        print("Cache state (Least Recently Used -> Most Recently Used):")
        for key, value in self.cache.items():
            print(f"{key}: {value}")

# Driver code with user interaction
capacity = int(input("Enter capacity of LRU Cache: "))
cache = LRUCache(capacity)

while True:
    print("\nOptions:")
    print("1. Put (Add/Update)")
    print("2. Get")
    print("3. Display Cache")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        key = input("Enter key to put: ")
        value = input("Enter value: ")
        cache.put(key, value)
    elif choice == '2':
        key = input("Enter key to get: ")
        cache.get(key)
    elif choice == '3':
        cache.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# 🔍 Explanation of Key Parts:
# Uses Python’s OrderedDict which maintains the order of keys by insertion or access.

# get(key): Returns value and marks the key as recently used by moving it to the end.

# put(key, value): Adds or updates key-value pair and removes the least recently used item if capacity is exceeded.

# popitem(last=False) removes the oldest (least recently used) item.

# ✅ Data Structure Used:
# OrderedDict: Allows O(1) access, insertion, deletion, and preserves the order needed for LRU eviction.