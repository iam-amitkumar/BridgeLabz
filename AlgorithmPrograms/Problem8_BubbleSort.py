"""This program Reads in integers prints them in sorted order using Bubble Sort.

@author Amit Kumar
@version 1.0
@since 04/01/2019
"""
# importing important modules
import utility.Utility

global input_string

try:
    input_string = input("Enter the numbers: ")
except Exception as e:
    print(e)

int_list = input_string.split()  # converting user-input string to string list
int_list = [int(i) for i in int_list]  # converting above string list to integer list
print("\nYour numbers: ", int_list)  # printing unsorted integer list
utility.Utility.bubble_sort(int_list)  # sorting the integer list using user-defined bubble_sort function
print("Sorted number: ", int_list)  # printing sorted integer list
