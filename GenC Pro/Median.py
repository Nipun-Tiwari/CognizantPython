def find_median_sorted_arrays(nums1, nums2):
    # Merge the two sorted arrays into one sorted list
    merged = []
    i = j = 0
    n1, n2 = len(nums1), len(nums2)

    # Merge step (like merge in merge sort)
    while i < n1 and j < n2:
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Append remaining elements
    while i < n1:
        merged.append(nums1[i])
        i += 1
    while j < n2:
        merged.append(nums2[j])
        j += 1

    # Calculate median
    total_len = len(merged)
    mid = total_len // 2

    if total_len % 2 == 0:
        # Even length: median is average of two middle elements
        median = (merged[mid - 1] + merged[mid]) / 2
    else:
        # Odd length: median is middle element
        median = merged[mid]

    return median

# Take inputs from user for two sorted arrays
n1 = int(input("Enter number of elements in first sorted array: "))
nums1 = list(map(int, input("Enter elements of first sorted array (space separated): ").split()))

n2 = int(input("Enter number of elements in second sorted array: "))
nums2 = list(map(int, input("Enter elements of second sorted array (space separated): ").split()))

# Find and print median
median = find_median_sorted_arrays(nums1, nums2)
print("Median of the two sorted arrays is:", median)


# 🔍 Explanation of Key Parts:
# Merges the two sorted arrays using a two-pointer technique.

# Calculates the median based on whether the merged length is even or odd.

# This approach has O(n + m) time complexity where n and m are the lengths of the arrays.