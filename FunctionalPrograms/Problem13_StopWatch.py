""" that takes two integer command­line arguments x and y
and prints the Euclidean distance from the point (x, y) to
the origin (0, 0) where point x and y is provided through
command-line

@author Amit Kumar
@version 1.0
@since 31/12/2018
"""
# importing important modules
import utility.Utility
import datetime

start = 0
stop = 0
loop_it = True  # to get the option to stop the stop watch after starting it
check_start = False  # to check further that the stopwatch is already started or not
print("\nStopwatch\n----------")
while loop_it:
    print("\nPress a button:\n"
          "1. Press 1 to start the stopwatch\n"
          "2. Press 2 to stop the stopwatch")
    option = utility.Utility.get_integer()  # getting the input from the user to start or stop the stopwatch
    if option == 1:
        start = datetime.datetime.now()  # when the stopwatch get started then storing current time in start variable
        check_start = True  # changing the status of "check_start" to True to assure that the stopwatch is started
    elif option == 2 and check_start is True:  # checking if the user press the button "2" and the stopwatch is started
        stop = datetime.datetime.now()  # getting the current time again assuming that the stopwatch is now stop
        res_time = stop - start  # now getting the time elapsed between start time and stop time
        print("\nElapsed Time : ", res_time)
        exit()
    else:
        print("\nInvalid Option, please provide a valid input.")
        break

