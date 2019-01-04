"""Utility module contains all the important or commonly
used functions/methods which can be further used in the
programs by importing this module.

@author Amit Kumar
@version 1.0
@since 26/12/2018
"""
# importing important modules
import cmath


# get_string function get the string value from the user and return it
def get_string():
    user_string = input("Enter your string/sentence: ")
    return user_string


# get_integer function get the integer value from the user and return it
def get_integer():
    user_integer = int(input("Please enter integer value: "))
    return user_integer


# get_float function get the float value from the user and return it
def get_float():
    user_float = float(input("Please enter float value: "))
    return user_float


# this function checks whether the user-input "year" is four digit or not, if not throws warning with @param year
def get_four_digit_year(year):
    if len(year) == 4:  # checking the length of user input string
        return int(year)  # converting to integer from string for further operation
    else:
        print("\nPlease enter only four digit year.")
        exit()


# this function create a user-defined two-dimensional array of integer type and return it
# having @param rows and @param columns and @return the 2D integer array
def int_two_dimensional_array(rows, columns):
    mat = [[0 for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            mat[i][j] = int(input("Enter the element for integer array: "))
    return mat


'''this function create a user-defined two-dimensional array of float type and return it
having @param rows and @param columns and @return the 2D float array'''


def float_two_dimensional_array(rows, columns):
    mat = [[0 for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            mat[i][j] = float(input("Enter the element for float array: "))
    return mat


'''this function create a user-defined two-dimensional array of boolean type and return it
aving @param rows and @param columns and @return the 2D boolean array'''


def boolean_two_dimensional_array(rows, columns):
    mat = [[0 for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            val = int(input("Enter the element boolean: "))
            if val == int(1) or val == int(0):
                mat[i][j] = val
            else:
                print("Please enter only boolean value,i.e., 0 or 1.")
                exit()
    return mat


# this function display returned user-defined array having @param rows, @param columns and @param mat
def display_arr(rows, columns, mat):
    print()
    for i in range(rows):
        for j in range(columns):
            print(mat[i][j], end="   ")
        print("\n")


# this function create user-input List of length n with @param size of the list and @return user-defined list
def user_int_list(list_size):
    user_list = []  # initializing a blank list
    for i in range(0, list_size):
        val = int(input("Enter an integer value: "))  # taking input from the list
        user_list.append(val)  # adding each user-input value to the list
    return user_list


# quadratic equation to find the roots of the equation, function contains @param a, @param b and @param c
def quad_equation(a, b, c):
    determinant = (b ** 2) - (4 * a * c)  # finding determinant of the given values using formula
    if determinant > 0:  # finding the roots if the value of determinant is greater than zero
        root1 = (-b + cmath.sqrt(determinant)) / (2 * a)
        root2 = (-b - cmath.sqrt(determinant)) / (2 * a)
        print('The solution are {0} and {1}'.format(root1, root2))
    elif determinant == 0:  # finding the roots if the value of determinant is equals to zero
        root1 = (-b / (2 * a))
        print('The solution are {0} and {1}'.format(root1, root1))  # both the rots are same if the determinant is zero
    else:  # finding the roots if the value of determinant is less than zero
        real_part = (-b / (2 * a))
        imaginary_part = cmath.sqrt(-determinant) / (2 * a)
        print('\nRoot 1 = {0} + {1}i  Root 2 = {0} + {1}i'.format(real_part, imaginary_part, real_part, imaginary_part))


'''binary_search is function with @param list and @ target and @return binary value this function search for an element 
in the given list binary search only works on sorted list because it divide the list into two halves on the basis of 
mid point and first search the element at mid-point if not found then according to the value it search in one half 
leaving the second half again in that half it divide it into two halves oon the basis of mid point, if found the value
at it then return True else again search in the respective part according to the value and so on. 
If the element not found in the list then return False.'''


def binary_search(li, target):
    lower = 0  # initially initializing the lower value to determine the mid point
    upper = len(li) - 1  # initially initializing the upper value to determine the mid point

    while lower <= upper:
        mid = (upper + lower) // 2  # determining the mid-point to know whether we have to search the list in the
        # first half or second half

        if li[mid] == target:  # if the element found at the mid-point then it will return True
            return True
        elif li[mid] < target:  # if the element is greater than mid-point value then re-initializing the lower limit
            lower = mid + 1
        else:
            upper = mid - 1  # if the element is less than the mid-point value then re-initializing the upper limit
    return False  # returning False if element not found


'''this function is used to sort the list having @param list while comparing the current element from all of its 
previous elements (starting from second element) if previous  elements are greater then shift them to the right. So all
the elements having larger value shifts to the right leaving all the elements with smaller value left to the left side 
and iterating this step to the last element of the list led to the sorting of the whole list.'''


def insertion_sort(list1):
    for index in range(1, len(list1)):

        current_value = list1[index]  # assigning the current index value to the "current value"
        current_position = index  # assigning current index to the "current position"

        while current_position > 0 and list1[current_position - 1] > current_value:
            list1[current_position] = list1[current_position - 1]  # shifting the larger element to the right index
            current_position = current_position - 1  # moving the pointer to its original place, i.e., one index left

            list1[current_position] = current_value  # shifting smaller element to the left index


'''Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are
in wrong order.'''


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


''' merge_sort is a recursive function having @param list that continually splits a list in half. If the list is empty 
# or has one item, it is sorted by definition. If the list has more than one item, we split the list and recursively 
# invoke a merge sort on both halves.'''


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves

        merge_sort(left)  # Sorting the first half
        merge_sort(right)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# function to print the list
def print_list(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
