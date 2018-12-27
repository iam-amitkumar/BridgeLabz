"""Utility python file contains all important functions
which will get imported in further programs.

@author Amit Kumar
@version 1.0
@since 26/12/2018
"""


# get_string method takes a word/string from the user and return it
def get_string():
    string = input("Please enter a word/sentence: ")
    return string


# get_integer method takes a integer value from the user and return it
def get_integer():
    number = int(input("Please enter a number: "))
    return number


# get_four_digit_year method can be used to take the year input containing only 4 digits otherwise shows warning
def get_four_digit_year(year):
    if len(year) == 4:  # checking length of year whether it is four digit or not
        year = int(year)  # if the year is four digit assigning it to the "year"
        return year
    else:
        print("\nPlease enter only four digit year")  # else displaying warning message to again enter the year
        quit()
