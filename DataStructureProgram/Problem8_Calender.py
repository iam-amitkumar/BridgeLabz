"""This program takes the month and year as user-input
and prints the Calendar of the month. Store the Calendar
in an 2D Array, the first dimension the week of the month
and the second dimension stores the day of the week.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""


# function to check whether the entered year is a leap year or not
def isleap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # checking whether the year is leap year or not
        return True  # returning True if the given year is a leap year
    else:
        return False  # returning False if the given year is not a leap year


# this function contains the algorithm to process given @param month and @ param year to print all the days and dates
# in the calender format
def calender(month, year):

    day = ['Sun', ' Mon', ' Tue', ' Wed', ' Thu', 'Fri', ' Sat']  # Stores the Month in a list

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # since the index of list starts from 0 and month
    # is 1

    values = 1
    d = 1  # initializing the value of 'd' for first date of every month

    m = month
    y = year

    # determining the day of the first date of any month so we can determine from which day we have to start printing
    # the calender, final output of the set of these formulae is 0-6, i.e., Sun - Sat
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7

    if isleap_year(year):  # checks if the month entered is February leap year or not
        days[month] = 29  # if yes sets the no. of days in February as 29
        days[1] = 29  # assigning last date of FEb to 29 instead of 28 if the current year is leap year
    row = 6
    column = 7
    two_d_array = [[0 for j in range(column)] for i in range(row)]  # create empty 2d array for calender

    print("\n            Calender \n--------------------------------")

    for i in range(0, 6 + 1):
        print(day[i], end=' ')  # print day's for calender
    print()

# storing the calender in the form of 2-D array
    for i in range(row):
        for j in range(column):
            if values <= days[m - 1]:  # storing the calender from 1 to last date of calender in the 2-D array
                if i == 0 and j < d0:  # while d0 is less than j
                    two_d_array[i][j] = ' '  # it will print blank space
                    continue

                two_d_array[i][j] = values  # add days into calender
                values += 1  # increment counter to reach upto last date of respective month

# print the calender in a proper format
    for i in range(row):
        for j in range(column):
            if two_d_array[i][j] != 0:
                x = two_d_array[i][j]  # ljust() method returns the string
                x1 = str(x).ljust(4)  # left justified in a string of length width and takes argument to put space
                # between each date
                print(x1, end=" ")  # printing each rows as a week in a single line

        print()  # changing the line after each week
        print()


########################################################################################################################
global month_, year_  # globalizing the variables use them as local while handling exception
try:
    month_ = int(input('\nEnter Month: '))
except Exception as e:  # handling exception for 'month' input
    print(e)
    print("Enter integer only ")
try:
    year_ = int(input('Enter year: '))
except Exception as e:  # handling exception for 'year' input
    print(e)
    print("Enter integer only")

try:
    calender(month_, year_)  # calling 'calender' method to print the calender
except Exception as e:
    print(e)
