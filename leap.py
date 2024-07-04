#10. **Write a Python program to find whether the given year is a leap year or not.**


# Example with year 2024
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")