"""LeapYear" program tells us whether the user input year is leap
year or not.

@author Amit Kumar
@version 1.0
@since 27/12/2018
"""
# importing important packages
import utility.Utility

year = input("\nPlease enter the year: ")
# calling a function to check whether the user input year is 4 digit or not
year = utility.Utility.get_four_digit_year(year)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # checking whether the year is leap year or not
    print("\n%s is a leap year!" % year)
else:
    print("\n%s is not a leap year!" % year)
