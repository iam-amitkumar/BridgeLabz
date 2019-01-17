"""This python file is part of Problem 5 having the data handler of
the values(getter and setter methods) of Transaction.

@author Amit Kumar
@version 1.0
@since 13/01/2019
"""


# 'transaction' class for data-handler
class Transaction(object):
    # data-handler methods to get the and set the value to the variables
    def set_customer_name(self, customer_name):  # setter method to set the value of 'customer name'
        self.__customerName = customer_name

    def set_company_symbol(self, company_symbol):  # setter method to set the value of 'company symbol'
        self.__companySymbol = company_symbol

    def set_buy_sell(self, buy_sell):  # setter method to set the value of 'set_buy_sell'
        self.__buySell = buy_sell

    def set_total_share(self, total_share):  # setter method to set the value of 'set_total_share'
        self.__totalShare = total_share

    def set_total_price(self, total_price):  # setter method to set the value of 'set_total_price'
        self.__totalPrice = total_price

    def set_time(self, time):  # setter method to set the value of 'set_time'
        self.__time = time

    def get_customer_name(self):  # getter method to get the 'customer name'
        return self.__customerName

    def get_company_symbol(self):  # getter method to get the 'company symbol'
        return self.__companySymbol

    def get_buy_sell(self):  # getter method to get the 'get_buy_sell'
        return self.__buySell

    def get_total_share(self,):  # getter method to get the 'total share'
        return self.__totalShare

    def get_total_price(self):  # getter method to get the 'get_total_price'
        return self.__totalPrice

    def get_time(self):  # getter method to get the 'get_time'
        return self.__time
