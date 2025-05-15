# Prompt the user to enter a non-negative integer
number = int(input("Enter a number: "))

# Check for invalid input (factorial not defined for negative numbers)
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Initialize the result to 1 (since factorial starts with 1)
    factorial = 1

    # Loop from 1 to the given number to compute factorial
    for i in range(1, number + 1):
        factorial *= i  # Multiply current value with i

    # Display the result
    print(f"The factorial of {number} is: {factorial}")

# Explanation of Key Parts:
# range(1, number + 1): Includes all numbers from 1 to number for multiplication.

# factorial *= i: Accumulates the result step-by-step.

