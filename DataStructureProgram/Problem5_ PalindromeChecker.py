"""This program have an algorithm to input a string of
characters and check whether it is a palindrome. This
problem use a deque to store the characters of the string.
We will process the string from left to right and add each
character to the rear of the deque.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""
# importing importing modules of DataStructure
from DataStructureProgram.Deque import *


def is_palindrome(word):
    queue = Deque()  # creating object of Deque class

    for ch in word:
        queue.insert_rear(ch)  # adds all the characters from back

    is_equal = True

    while queue.size() > 1 and is_equal:
        first = queue.remove_front()  # removes the characters from the front of the queue
        last = queue.remove_rear()  # removes the characters from the rear of the queue
        if first != last:
            is_equal = False

    return is_equal


word_ = input("\nEnter the word ")

if is_palindrome(word_):
    print("\n'", word_, "' is Palindrome")
else:
    print("\n'", word_, "' is not Palindrome")


# from DataStructureProgram.Deque import *
#
#
# # this method create object of Deque class, take a string from user and return True or False basis on the result
# def palindrome_checker():
#     d1 = Deque()  # creating object of the Deque class
#     global string  # making variable "string" global to use it in try block
#     try:
#         string = input("Enter String to Check for Palindrome: ")
#     except Exception as e:  # handling exception for user-input
#         print(e)
#     lower_string = string.lower()  # converting the user-input string to lower case
#     string = lower_string  # assigning converted user-input sentence to the variable "string"
#
#     remove_space = ''
#     for i in range(0, len(string)):  # removing blank space from the string
#         if string[i] == ' ':
#             continue
#
#         remove_space += string[i]
#
#     string = remove_space
#
#     for i in string:
#         d1.insert_rear(i)  # queuing the letters of the string to the queue from rear side
#     reverse_string = ''
#     for i in range(0, d1.size()):
#         reverse_string += str(d1.delete_rear())  # trimming the letters of the deque and adding them to the string
#         # "reverse_string", i.e., reversing the string
#
# # comparing the the reversed string with the original string
#     if string == reverse_string:
#         return True  # returning True if both strings matched
#     else:
#         return False  # returning False if both strings not matched
#
#
# if palindrome_checker():
#     print("\nYour string is Palindrome")
# else:
#     print("\nYour string is not palindrome")
