# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).

# For example:
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

for i in range(1,20):
    if i/i==i and i%2==1:
        print("the number is prime", i)
i+=1
