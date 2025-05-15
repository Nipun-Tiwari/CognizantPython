# Prompt the user to enter a number
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    # Assume the number is prime until proven otherwise
    is_prime = True

    # Only check up to the square root of the number for efficiency
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False  # Found a divisor, not prime
            break

    # Display result based on the flag
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

# Explanation of Key Parts:
# num <= 1: 0 and 1 are not prime numbers.

# range(2, int(num ** 0.5) + 1): Efficient way to check for factors — no need to go beyond the square root of the number.

# Early break: Stops checking as soon as a factor is found, improving performance.