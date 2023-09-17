def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Input a number
num = int(input("Enter a number: "))

# Check if the input is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")