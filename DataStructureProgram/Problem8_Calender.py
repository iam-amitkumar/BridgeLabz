import sys
from DataStructureProgram.Queue import *

queue = Queue()


def isleap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:  # checking whether the year is leap year or not
        return True
    else:
        return False


def calender_queue(month, year):
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if isleap_year(year):     # check leap year
            days[1] = 29
        row = 6
        column = 7

        print('Calender ', month, ',', year, '\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')       # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:       # while d0 is less than j
                    if i == 0 and j < d0:       # it will print blank space
                        queue.enqueue(' ')      # used enqueue() method of queue class
                        continue                # to add space

                    queue.enqueue(values)       # add element in queue
                    values += 1

        for i in range(row):

            for j in range(column):
                if queue.size() > 0:
                    x = queue.de_queue()    # remove element from queue and store it in x variable
                    x1 = str(x).ljust(2)    # using ljust() method print formatted calender
                    print(x1, end=" ")
            print()


global m1, y1
try:
    m1 = int(input('Enter Month: '))
except Exception as e:
    print(e)
    print("Enter integer only ")
try:
    y1 = int(input('Enter Year: '))
except Exception as e:
    print(e)
    print("Enter integer only")
print()
calender_queue(m1, y1)
