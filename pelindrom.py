#Write a Python program to check if the number provided by the user is a palindrome or not.

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
