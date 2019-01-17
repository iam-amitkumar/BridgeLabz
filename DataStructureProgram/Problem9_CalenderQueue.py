"""This program takes the month and year as user-input
and prints the Calendar of the month. All the days and
dates stored in a Queue implemented using Linked List.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""

# importing important modules
from DataStructureProgram.Queue import *

queue = Queue()  # creating object of Queue class to use the methods of class


# function to check whether the entered year is a leap year or not
def isleap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # checking whether the year is leap year or not
        return True  # returning True if the given year is a leap year
    else:
        return False  # returning False if the given year is not a leap year


# this function contains the algorithm to process given @param month and @param year to print all the days and dates
# in the calender format using Queue
def calender_queue(month, year):

    day = ['Sun', ' Mon', ' Tue', ' Wed', ' Thu', 'Fri', ' Sat']  # Stores the Month in a list

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # since the index of list starts from 0 and month

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
        days[1] = 29  # assigning last date of FEb to 29 instead of 28 if the current year is leap year
    row = 6
    column = 7

    print('Your Calender is\n')

    for i in range(0, 6 + 1):
        print(day[i], end=' ')  # print day's for calender
    print()

    for i in range(row):
        for j in range(column):
            if values <= days[m - 1]:  # while d0 is less than j
                if i == 0 and j < d0:  # it will print blank space
                    queue.enqueue(' ')  # used en_queue() method of queue class
                    continue  # to add space

                queue.enqueue(values)  # adding element in queue
                values += 1

    for i in range(row):
        for j in range(column):
            if queue.size() > 0:
                x = queue.de_queue()  # remove element from queue and store it in x variable
                x1 = str(x).ljust(4)  # using ljust() method print formatted calender and takes argument to put space
                print(x1, end=" ")  # printing each rows as a week in a single line
        print()  # changing the line after each week
        print()


global month_, year_  # globalizing the variables use them as local while handling exception
try:
    month_ = int(input('Enter Month:'))
except Exception as e:  # handling exception for 'month' input
    print(e)
    print("Enter integer only ")
try:
    year_ = int(input('Enter year:'))
except Exception as e:  # handling exception for 'year' input
    print(e)
    print("Enter integer only")

try:
    calender_queue(month_, year_)  # calling 'calender' method to print the calender
except Exception as e:
    print(e)
