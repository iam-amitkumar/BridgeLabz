"""Hello_User program an program which gives the output after
replacing the word "<<UserName>>" from pre-written string
with the user input name.

@author Amit Kumar
@version 1.0
@since 26/12/2018
"""
# Importing important modules
import utility.Utility

a = "Hello <<UserName>>, How are you?"
name = utility.Utility.get_string()  # calling get_string functions
res = a[0:6]+name+a[18:32]  # concatenation substring before <<UserName>> + user input name + substring after
# <<UserName>>
print(res)
