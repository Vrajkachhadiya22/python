Sure! It looks like you need help with various Python programming tasks from the provided document. Let's go through some of the tasks and I'll provide you with the necessary Python code.

### Practical No. 1

1. **Write a Python program to display "Python First Program".**

```python
print("Python First Program")
```

2. **Write a Python program to display the sum of two numbers.**

```python
# Example with numbers 3 and 5
a = 3
b = 5
sum = a + b
print("Sum of", a, "and", b, "is", sum)
```

3. **Write a program in Python to swap two number type variables without using a temporary variable.**

```python
# Example with numbers 3 and 5
a = 3
b = 5
a, b = b, a
print("After swapping: a =", a, "b =", b)
```

4. **Write a program in Python to find out the maximum and minimum number out of three inputted numbers.**

```python
# Example with numbers 3, 5, and 7
a = 3
b = 5
c = 7
max_num = max(a, b, c)
min_num = min(a, b, c)
print("Maximum number is", max_num)
print("Minimum number is", min_num)
```

5. **Write a Python program to check if an inputted number is odd or even.**

```python
# Example with number 5
num = 5
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
```

6. **Write a Python program to check if the number provided by the user is an Armstrong number.**

```python
# Example with number 153
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
```

7. **Write a Python program to check whether the number is positive, negative, or zero.**

```python
# Example with number -5
num = -5
if num > 0:
    print(num, "is positive")
elif num == 0:
    print("Zero")
else:
    print(num, "is negative")
```

8. **Write a Python program to check if the number provided by the user is a palindrome or not.**

```python
# Example with number 121
num = 121
temp = num
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if num == reverse:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")
```

9. **Write a program in Python to implement the Fibonacci series up to a user-entered number.**

```python
# Example with n = 10
n = 10
a, b = 0, 1
while a < n:
    print(a, end=" ")
    a, b = b, a + b
```

10. **Write a Python program to find whether the given year is a leap year or not.**

```python
# Example with year 2024
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
```

11. **Write a program to implement the factorial series up to a user-entered number.**

```python
# Example with n = 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 5
for i in range(1, n+1):
    print("Factorial of", i, "is", factorial(i))
```

12. **Write a Python program to convert decimal to binary, octal, and hexadecimal.**

```python
# Example with number 10
num = 10
print("Binary of", num, "is", bin(num))
print("Octal of", num, "is", oct(num))
print("Hexadecimal of", num, "is", hex(num))
```

13. **Write a program to input marks of 5 subjects of a student and display the total marks scored, percentage scored, and the class of result.**

```python
marks = [85, 78, 92, 74, 88]
total_marks = sum(marks)
percentage = (total_marks / 500) * 100

if percentage >= 70:
    classification = "Distinction"
elif percentage >= 60:
    classification = "First Class"
elif percentage >= 50:
    classification = "Second Class"
elif percentage >= 40:
    classification = "Pass Class"
else:
    classification = "Fail"

print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Class of Result:", classification)
```

14. **Write a Python program to print the sum of digits in a number.**

```python
# Example with number 123
num = 123
sum_of_digits = sum(int(digit) for digit in str(num))
print("Sum of digits in", num, "is", sum_of_digits)
```

15. **Write a Python program to print the sum of even numbers up to a given N number.**

```python
# Example with N = 7
N = 7
sum_of_even = sum(i for i in range(2, N+1, 2))
print("Sum of even numbers up to", N, "is", sum_of_even)
```

These examples cover the first set of practical problems. If you need more assistance or solutions for the remaining tasks, let me know!