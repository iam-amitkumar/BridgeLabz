"""PowerOfTwo program printing a table of power of two that
are less than than or equals to 2^N where N is user-input.
Range of N should be 0 =< N <31.
Note: The user should provide the input through command-line
argument.

@author Amit Kumar
@version 1.0
@since 27/12/2018
"""
# importing sys module to take the input through command-line
import sys

num = int(sys.argv[1])  # casting from string type to integer type because type of input through command-line is string

print("Value of N: ", num)
if num >= 0:  # checking whether the user input is in range or not, ie., (N >= 0)
    if num < 31:  # checking whether the user input is in range or not, ie., (N < 31)
        for i in range(0, num+1):  # iterating the value of i from 0 to N
            print("2 ^ ", i, " = ", 2**i)
    else:
        print("Please provide the value of N less than 31")
else:
    print("Value of N should N >= 0")
