""" PermutationOfString prints all possible permutation of
string given by the user

@author Amit Kumar
@version 1.0
@since 31/12/2018
"""
# importing important modules
import utility.Utility


# declaring the function to print all the possible permutation the of a string provided as @param with
# @param starting index of string and @param last index of string
def permute(a, l, r):
    if l == r:  # checking whether string is of single character or not
        print(''.join(a))  # then printing the given string as it is
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)  # recursion of the function
            a[l], a[i] = a[i], a[l]  # backtrack


string = utility.Utility.get_string()  # getting the string from the user
n = len(string)  # getting the length of the user-input string
a = list(string)  # converting the string to list to get the indexes of the string to swap the letters of it
permute(a, 0, n-1)

