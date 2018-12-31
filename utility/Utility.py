"""Utility module contains all the important or commonly
used functions/methods which can be further used in the
programs by importing this module.

@author Amit Kumar
@version 1.0
@since 26/12/2018
"""


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


# this function create a user-defined two-dimensional array of float type and return it
# having @param rows and @param columns and @return the 2D float array
def float_two_dimensional_array(rows, columns):
    mat = [[0 for i in range(columns)] for j in range(rows)]

    for i in range(rows):
        for j in range(columns):
            mat[i][j] = float(input("Enter the element for float array: "))
    return mat


# this function create a user-defined two-dimensional array of boolean type and return it
# having @param rows and @param columns and @return the 2D boolean array
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


# this function create user-input List of length n with @param size of the list
def user_int_list(list_size):
    user_list = []  # initializing a blank list
    for i in range(0, list_size):
        val = int(input("Enter an integer value: "))  # taking input from the list
        user_list.append(val)  # adding each user-input value to the list
    return user_list

