# Prompt the user to enter how many terms of the Fibonacci series to generate
n = int(input("Enter the number of terms: "))

# Check for invalid input
if n <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the first two terms of the Fibonacci series
    fib_series = []       # List to store the Fibonacci sequence
    a, b = 0, 1           # First two terms: 0 and 1

    # Generate the series up to n terms
    for i in range(n):
        fib_series.append(a)  # Append current term to the list
        a, b = b, a + b        # Update 'a' to next term, 'b' to sum of previous two

    # Display the Fibonacci series
    print("Fibonacci series:", fib_series)
    
# 🔍 Explanation of Key Parts:
# a, b = b, a + b: This is a Pythonic way to update two values at once — a becomes b, and b becomes the sum of a and b.

# fib_series list: Used to store and display the entire series.