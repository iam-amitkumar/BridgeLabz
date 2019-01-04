"""This program reads in strings from standard input
and prints them in sorted order using insertion sort
algorithm

@author Amit Kumar
@version 1.0
@since 04/01/2019
"""
# importing important modules
import utility.Utility
import string

u_string = input("Enter the number of string you want to enter: ")
list1 = u_string.split()  # converting user-input string into string list
input_list = [word.strip(string.punctuation) for word in list1]  # trimming commas/punctuation present in the user list
user_string = ' '.join(input_list)  # converting trimmed list into string separated by space to print as unsorted string
print("\nYour string: \n%s" % user_string)

utility.Utility.insertion_sort(input_list)  # sorting the trimmed list using user-defined insertion_sort method
res = ' '.join(input_list)  # converting sorted list into string separated by space

print("\nYour sorted string: \n%s" % res)
