from DataStructureProgram.Deque import *


def palindrome_checker():
    d1 = Deque()
    global string
    try:
        string = input("Enter String to Check for Palindrome: ")
    except Exception as e:
        print(e)
    lower_string = string.lower()
    string = lower_string

    remove_space = ''
    for i in range(0, len(string)):
        if string[i] == ' ':
            continue

        remove_space += string[i]

    string = remove_space

    for i in string:
        d1.insert_rear(i)
    reverse_string = ''
    for i in range(0, d1.size()):
        reverse_string += str(d1.delete_rear())

    if string == reverse_string:
        return True
    else:
        return False


if palindrome_checker():
    print("\nYour string is Palindrome")
else:
    print("\nYour string is not palindrome")
