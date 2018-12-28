"""Hello_User program an program which gives the output after
replacing the word "<<UserName>>" from pre-written string
with the user input name.

@author Amit Kumar
@version 1.0
@since 27/12/2018
"""
# importing important modules
import utility.Utility

num = utility.Utility.get_integer()
NthSum = 0.0
for i in range(1, num+1):  # iterating the value of i from 1 to N
    NthSum = NthSum + (1/i)  # adding all the inverted natural number up to N
print("\n", num, "Harmonic Number: ", NthSum)
