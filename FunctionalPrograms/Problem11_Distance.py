""" that takes two integer command­line arguments x and y
and prints the Euclidean distance from the point (x, y) to
the origin (0, 0) where point x and y is provided through
command-line

@author Amit Kumar
@version 1.0
@since 31/12/2018
"""
# importing important modules
import sys
import math

global num1, num2

try:
    num1 = int(sys.argv[1])  # taking value of x from the command-line storing it into a variable
    num2 = int(sys.argv[2])  # taking value of y from the command-line storing it into a variable
except Exception as e:
    print(e)

res = math.sqrt((num1**2)+(num2**2))  # finding the distance of point(x,y) from origin using Euclidean distance formula
print("\nDistance of point (", num1, ",", num2,  ") from origin: ", res, "\n")
