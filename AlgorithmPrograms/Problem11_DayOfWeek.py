"""DayOfWeek program takes Day, Month, Year in number format and
returns a number 0-6 where 0 is for Sunday, 1 for AMonday and so on
after processing the the given input using given formulae.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""
# importing important modules
import sys


# function to return number from 0 to 6 from Sunday to Saturday respectively using some formulae
def day_of_week(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    return d0


# Assigning days of the week for the returned number b y above function
days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    }


# storing values to the variables for further calculation taken through  command-line argument
day = int(sys.argv[1])
month = int(sys.argv[2])
year = int(sys.argv[3])

day_conversion = day_of_week(day, month, year)
print(days.get(day_conversion, -1))  # printing day of the week after passing values to the function



