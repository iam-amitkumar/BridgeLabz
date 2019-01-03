"""This program is program that outputs the binary (base 2) representation of
the decimal number typed as the input. It is based on decomposing the number into
a sum of powers of 2.

@author Amit Kumar
@version 1.0
@since 03/01/2019
"""
# importing important modules
import utility.Utility
import util.Util

print()  # putting one white-space line before printing anything on the console
deci = utility.Utility.get_integer()  # calling the function
print("Binary representation of ", deci, ": ", util.Util.to_binary(deci))  # printing the output
