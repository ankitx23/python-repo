# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.

# Expected Output:
# original number 121
# Yes. given number is palindrome number

# original number 125
# No. given number is not palindrome number

a= input ("Enter a number \n")

b = "".join(reversed(a))

print(a,b)

if a == b:
    print ("the number is palindrome")
else:
    print ("the number is not palindrome")


