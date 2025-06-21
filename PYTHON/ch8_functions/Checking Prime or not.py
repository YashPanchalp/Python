def is_prime(n):
    # Check if the number is less than 2
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    # Check if the number is 2, which is prime
    if n == 2:
        return True
    # Eliminate even numbers greater than 2
    if n % 2 == 0:
        return False
    # Check for factors from 3 up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example usage:
num = 17
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
