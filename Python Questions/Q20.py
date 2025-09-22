# Exercise 21: Check if a user-entered string contains any digits using a for loop
# Expected Output:

# Enter a string: Pynative123Python
# The string contains at least one digit.

# Enter a string: PYnative
# The string does not contain any digits.

# a=(0,1,2,3,4,5,6,7,8,9,)
# print (type(b), b)
found = False

str = input("Enter the word")

# str = str(input("Enter the Word"))

for ch in str:
    if ch in "0123456789":
        found=True
        break

if found:
    print("it contains numbers")  
else:
    print("it does not contain numbers")

