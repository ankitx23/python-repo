# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

# Given:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:

# result list: [25, 35, 40, 60, 90]

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# for num in list1:
#     if num % 2 == 1:
#         print(num)

# for num2 in list2:
#     if num2 %2== 0:
#         print (num2)

# print (num+num2)

def merge_list(list1, list2):
    result_list = []

    for num in list1:
        if num%2 == 1:
            result_list.append(num)

    for num in list2:
        if num%2 == 0:
            result_list.append(num)

    return result_list
    

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result_list: ", merge_list(list1, list2))