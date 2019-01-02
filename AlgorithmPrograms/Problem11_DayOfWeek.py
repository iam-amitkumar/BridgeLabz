"""

"""
import sys


def day_of_week(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    return d0


days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    }


day = int(sys.argv[1])
month = int(sys.argv[2])
year = int(sys.argv[3])

day_conversion = day_of_week(day, month, year)
print(days.get(day_conversion, -1))



