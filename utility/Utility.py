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

