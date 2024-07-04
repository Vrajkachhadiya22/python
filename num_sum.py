#14. **Write a Python program to print the sum of digits in a number.**


# Example with number 123
num = 123
sum_of_digits = sum(int(digit) for digit in str(num))
print("Sum of digits in", num, "is", sum_of_digits)