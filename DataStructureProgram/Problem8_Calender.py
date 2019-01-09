"""This program takes the month and year as command­line
arguments and prints the Calendar of the month. Store the
Calendar in an 2D Array, the first dimension the week of
the month and the second dimension stores the day of the week.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""
# importing important modules
import math


# function to check whether the entered year is a leap year or not
def is_leap_year(year2):
    if (year2 % 400 == 0) or ((year2 % 4 == 0) and (year2 % 100 != 0)):  # checks whether the year is a century
        # year or not
        return True
    return False


# determining the day of the first date of any month so we can determine from which day we have to start printing the
# calender having @param month, @param day and @param year and @ return number between 0-6
def day(month1, day1, year1):
    y = math.ceil(year1 - (14 - month1) / 12)
    x = math.floor(y + y / 4 - y / 100 + y / 400)
    m = month1 + (12 * int((14 - month1) / 12) - 2)
    d = int((day1 + x + ((31 * m) / 12)) % 7)
    return d


# Function to print the Calendar have @param month and @param year
def calendar(month, year):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]  # Stores the Month in a list

    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # since the index of list starts from 0 and month
    # is 1

    if month == 2 and is_leap_year(year):  # checks if the month entered is February leap year or not
        days[month] = 29  # if yes sets the no. of days in February as 29

    print("        ", months[month - 1] + " ", year, "\n")  # used to display the the calendar of the month
    print(" Su Mo Tu We Th Fr Sa")
    print("-----------------------")

    d = day(month, 1, year)  # gets the number of days
    i = 0
    # print(d)
    while i < d:
        print("   ", end=''),  # prints spaces based on the days
        i += 1
    # print(i)
    i = 1
    while i <= days[month]:
        print("%2d" % i, end=' '),  # prints in 2 decimal format

        if int(i + d) % 7 == 0 or (i == days[month]):  # if week is over returns a new line

            print("\n")
        i += 1  # increments the i count


global month_, year_
try:
    month_ = input("enter the month\n")  # takes the month as an input
    year_ = input("enter the year\n")
except Exception as e:
    print(e)

try:
    calendar(int(month_), int(year_))  # calls the function to display the calendar
except Exception as e:
    print(e)
    print("Invalid input")
