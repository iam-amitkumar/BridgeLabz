"""Adding the Prime Numbers that are Anagram in the Range of
0 ­ 1000 in a Stack using the LinkedList and Print the Anagrams
in the Reverse Order.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""
# importing important modules
from DataStructureProgram.Stack import *


# this function checks whether the given two parameters are anagram or not
def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):  # comparing both the strings after sorting
        return True  # return True if both the strings are anagram
    else:
        return False  # return False if the strings are not anagram


s1 = Stack()  # creating the object of the class Stack to use all the methods of that class
arr = []  # initializing empty list
i = 2

# adding all the prime numbers to the list
while i < 1000:
    j = 2
    flag = 0
    while j < i:
        if i % j == 0:
            flag = 1
        j += 1
    if flag == 0:
        arr.append(str(i))  # appending value in the list
    i += 1

# pushing all the anagram pair of the list in the stack
i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if is_anagram(arr[i], arr[j]):  # checking whether the numbers passed to the function is anagram or not
            s1.push(arr[i])  # if both numbers are anagram then pushing both the numbers in the stack
            s1.push(arr[j])
        j += 1
    i += 1

s1.display()  # printing the stack after pushing all the anagrams in the stack
