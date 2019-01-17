"""this program Merge Sort of list of String. To Merge
Sort an array, we divide it into two halves, sort the
two halves independently, and then merge the results
to sort the full array using recursion technique.

@author Amit Kumar
@version 1.0
@since 04/01/2019
"""
# importing important modules
import utility.Utility

global input_string

try:
    input_string = utility.Utility.get_integer()
except Exception as e:
    print(e)

int_list = input_string.split()  # converting user-input string into string list
int_list = [int(i) for i in int_list]  # converting the string list into the integer list
print("\nGiven array is", end="\n")
utility.Utility.print_list(int_list)  # print the unsorted list using user-defined function
utility.Utility.merge_sort(int_list)  # sorting the user-defined list through "Merge-Sort" technique.
print("\nSorted array is: ", end="\n")
utility.Utility.print_list(int_list)  # printing the sorted list after sorting using user-defined function
