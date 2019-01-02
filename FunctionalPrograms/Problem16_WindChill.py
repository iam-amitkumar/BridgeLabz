"""The program WindChill that takes two double command­line arguments t
and v and prints the wind chill using given formula.

@author Amit Kumar
@version 1.0
@since 01/01/2019
"""
# importing important modules
import sys


def wind_chill_prob(t, v):
    w = 0.0
    if t <= 50 and (t <= 120 and t >= 3):  # applying condition when value of 't' is valid
        w = 35.74+(0.6215*t)+(((0.4275*t)-35.75) * (v ** 0.16))
    else:
        print("Value of 't' should not exceed more than 50\nValue of 'v' should not exceed more than 120 or less "
              "than 3	")
    return w


t1 = int(sys.argv[1])  # getting value of t from command-line argument from user
v1 = int(sys.argv[2])  # getting value of v from command-line argument from user
res = wind_chill_prob(t1, v1)
print("Effective temperature (the wind chill): ", res)