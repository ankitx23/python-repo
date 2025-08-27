# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below

# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose the income is 45000, and the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000

a= int( input("Enter your Salary : "))

if a <=9999:
    print(" there will be 0% Interest")
elif  a in range (10000,24999):
    b = a*0.1
    print ("the interest will be 10%", b)
else:
    c = a*0.3
    print ("the interest is 30% on ur salary. Which is", c)