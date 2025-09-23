# Exercise 4: Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.

def removelements(word, n):
    print('Original String: ', word)
    x = word[n:]
    return x

print(removelements("ANKITYADAV",6))


