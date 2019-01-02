"""
@author Amit Kumar
@version 1.0
@since 01/01/2019
"""
# import important modules
import utility.Utility
print("Please enter the value of a(a should not be 0): ")
a = utility.Utility.get_float()
print("Please enter the value of b: ")
b = utility.Utility.get_float()
print("Please enter the value of c: ")
c = utility.Utility.get_float()
print(utility.Utility.quad_equation(a, b, c))
