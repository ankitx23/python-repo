# Write a Python code to display numbers from a list divisible by 5
# Expected Output:
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

def main():
    numbers = [10, 20, 30, 40, 50]
    for number in numbers:
        if number%5==0:
            print (number)

if __name__== "__main__":
    main()
    