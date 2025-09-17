# Exercise 18: Check if a given year is a leap year
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.


# AD
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.

# Write a code find if a given year is a leap year.

a = int(input("enter a year: "))

if a % 4 ==0:
    print(f"the year {a} is Leap year")
else:
    print(f"{a} is not a leap year")