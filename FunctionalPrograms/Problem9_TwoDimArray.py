""" TwoDimArray program take the values from the user and print matrix
of integer, float and boolean type.

@author Amit Kumar
@version 1.0
@since 29/12/2018
"""
import utility.Utility

int_rows = int(input('enter number of rows for integer matrix :'))
int_columns = int(input('enter number of columns for integer matrix :'))
float_rows = int(input('\nenter number of rows for float matrix: '))
float_columns = int(input('enter number of columns for float integer matrix: '))
boolean_rows = int(input('\nenter number of rows for boolean matrix: '))
boolean_columns = int(input('enter number of columns for boolean matrix: '))
print()

# user defined integer matrix
int_mat = utility.Utility.int_two_dimensional_array(int_rows, int_columns)
print()
# user defined float matrix
float_mat = utility.Utility.float_two_dimensional_array(float_rows, float_columns)
print()
# user defined boolean matrix
boolean_mat = utility.Utility.boolean_two_dimensional_array(boolean_rows, boolean_columns)
print()

# display integer matrix
print("Integer Array: ")
utility.Utility.display_arr(int_rows, int_columns, int_mat)
# display float matrix
print("Float Array: ")
utility.Utility.display_arr(float_rows, float_columns, float_mat)
# display boolean matrix
print("Boolean Array: ")
utility.Utility.display_arr(boolean_rows, boolean_columns, boolean_mat)
