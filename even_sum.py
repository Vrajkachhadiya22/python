#15. **Write a Python program to print the sum of even numbers up to a given N number.**


# Example with N = 7
N = 7
sum_of_even = sum(i for i in range(2, N+1, 2))
print("Sum of even numbers up to", N, "is", sum_of_even)