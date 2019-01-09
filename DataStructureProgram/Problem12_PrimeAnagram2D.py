"""This program is extension of "PrimeNumber2D" program and store only the numbers
in that range that are Anagrams. For e.g. 17 and 71 are both Prime and Anagrams in
the 0 to 1000 range. Further store in a 2D Array the numbers that are Anagram and
numbers that are not Anagram.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""


# this function checks whether the two strings are anagram or not having @param str1 and @param str2
def is_anagram(str1, str2):
    if sorted(str1) == sorted(str2):  # comparing both the strings after sorting
        return True  # return True if both the strings are anagram
    else:
        return False  # return False if the strings are not anagram


arr = []  # initializing an empty array
i = 2
while i < 1000:  # repeating the process if value of i is between 2 to 999
    j = 2
    flag = 0
    while j < i:
        if i % j == 0:
            flag = 1
        j += 1
    if flag == 0:
        arr.append(str(i))  # adding value to the list
    i += 1

i = 0
array = []
count = 0

# printing the list in the pair of number and its anagram value
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if is_anagram(arr[j], arr[i]):
            print(arr[i], " ", arr[j])
        j += 1
    i += 1
