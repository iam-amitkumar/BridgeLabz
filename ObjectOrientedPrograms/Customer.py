"""This python file is part of Problem 5 having the custom constructor
to initialize the values of Customer of the variables and this file also
contain the data handler of the values(getter and setter methods).

@author Amit Kumar
@version 1.0
@since 13/01/2019
"""


# 'Customer' class for constructor and data-handler
class Customer(object):
    def __int__(self):
        pass

    # overriding user-defined constructor to initialize the values to the user-input
    def __init__(self, Customer_name, amount, noOfShare):
        self.__CustomerName = Customer_name
        self.__amount = amount
        self.__noOfShare = noOfShare

    # data-handler methods to get the and set the value to the variables
    def set_customer_name(self, Customer_name):  # setter method to set the value of 'customer name'
        self.__CustomerName = Customer_name

    def set_amount(self,amount):  # setter method to set the value of 'amount'
        self.__amount = amount

    def set_noOfShare(self, noOfShare):  # setter method to set the value of 'number of share'
        self.__noOfShare = noOfShare

    def get_customer_name(self):  # getter method to get the 'customer name'
        return self.__CustomerName

    def get_amount(self):  # getter method to get the 'amount'
        return self.__amount

    def get_noOfShare(self):  # getter method to get the 'number of share'
        return self.__noOfShare
