"""This program Read in the following message: Hello <<name>>, We have your full
name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx.
Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016.
Use Regex to replace name, full name, Mobile#, and Date with proper value.

@author Amit Kumar
@version 1.0
@since 11/01/2019
"""
# Importing important modules
import re


# 'RegularExpression' class
class RegularExpression:

    def __init__(self):
        pass

    # This method take string and replace some part of string using regex methods.
    # check for particular pattern and replace the string with user input and return the proper replaces string.
    @staticmethod
    def regex():

        string = '\nHello <<name>>, We have your full name as <<full name>> in our system.' \
                 '\nYour contact number is 91-xxxxxxxxxx.' \
                 '\nPlease, let us know in case of any clarification Thank you BridgeLabz 01/01/2019. '
        # template list contain some patterns which will get replaced from the 'string' string after taking the input
        # from the user
        template = ['<<name>>', '<<full name>>', 'xxxxxxxxxx', '01/01/2019']
        print()
        # list of strings which will display while asking input from the user
        list_ = ['Enter Your First Name: ', 'Enter Your Full Name: ', 'Enter Your Mobile Number(10 digits only):',
                 "Enter Today's Date[dd/mm/yyy]:"]

        # accessing each elements of the both lists present above for further process
        for i in range(4):
            print(list_[i])   # print list array elements to take input from user
            # sub() method of 're' module check the pattern and replace given string with given pattern
            replaced_string = re.sub(template[i], str(input()), string)
            string = replaced_string  # storing the string in a new variable after replacement of the keywords to return

        return string      # returning resultant string


# this method contains the object of above class to access all the necessary class member
def re_runner():
    try:
        obj = RegularExpression()  # creating object of 'RegularExpression' class
        print("The Modified String with user information are as follows")
        print(obj.regex())  # accessing 'regex' method through reference variable
    except Exception as e:  # handling the exception
        print(e)


# from this python file only program will compile not from the imported file(s)
if __name__ == "__main__":
    re_runner()  # calling 're_runner' function
