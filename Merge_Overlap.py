# Prompt the user to enter the number of intervals
n = int(input("Enter the number of intervals: "))

# Initialize an empty list to store intervals
intervals = []

# Take input intervals from the user
print("Enter intervals in the format: start end")
for i in range(n):
    start, end = map(int, input(f"Interval {i+1}: ").split())
    intervals.append([start, end])

# Sort intervals based on the start time
intervals.sort(key=lambda x: x[0])

# List to hold merged intervals
merged = []

# Loop through the sorted intervals
for interval in intervals:
    # If merged list is empty or current interval doesn't overlap with the last one in merged
    if not merged or merged[-1][1] < interval[0]:
        merged.append(interval)
    else:
        # Overlapping intervals, so merge by updating the end of the last interval
        merged[-1][1] = max(merged[-1][1], interval[1])

# Display merged intervals
print("Merged intervals:")
for interval in merged:
    print(interval)

# 🔍 Explanation of Key Parts:
# Intervals are first sorted by their start time to make merging easier.

# The algorithm iterates through each interval, merging it with the last one in the result if they overlap.

# Overlap condition: current interval’s start is less than or equal to the last merged interval’s end.

# If no overlap, simply append the interval.