"""'StockReport' is a program to read in Stock Names, Number of Share, Share Price.
Print a Stock Report with total value of each Stock and the total value of Stock
having functions in the Class to calculate the value of each stock and the value
of total stocks.

@author Amit Kumar
@version 1.0
@since 11/01/2019
"""


# Stock class having constructor and data handler methods
class Stock:
    # user-defined constructor to initialize the values to the user-input
    def __init__(self, stock_name, no_of_share, share_price):
        self.__stock_name = stock_name
        self.__no_of_share = no_of_share
        self.__share_price = share_price

# data-handler methods to get the and set the value to the variables
    def stock_name_getter(self):  # getter method to get the 'stock name'
        return self.__stock_name

    def stock_name_setter(self, stock_name):  # setter method to set the value of 'stock name'
        self.__stock_name = stock_name

    def no_of_share_getter(self):  # getter method to get the 'number of price'
        return self.__no_of_share

    def no_of_share_setter(self, no_of_share):  # setter method to set the value of 'number of share'
        self.__no_of_share = no_of_share

    def share_price_getter(self):  # getter method to get the 'share price'
        return self.__share_price

    def share_price_setter(self, share_price):  # setter method to set the value of 'share price'
        self.__share_price = share_price


# 'StockPortfolio' class having method to calculate total value of each stock and method to calculate  grand-total
# value of all the stocks
class StockPortfolio:

    no_of_stock = int(input("\nEnter total number of stocks: "))
    count = 0  # initializing count variable to run the while loop until the total number of stocks given by the user
    objects = []  # creating the blank list to store all the Stock objects having Stock details
    global s1  # globalizing the s1 variable
    print()
    while count < no_of_stock:

        # taking details of stock details from the user
        stock_name = input("Enter the name of Stock: ")
        no_of_share = int(input("Enter the number of share(s): "))
        share_price = int(input("Enter the price of share: "))

        # creating new object of Stock class by calling the constructor
        s1 = Stock(stock_name, no_of_share, share_price)
        s1.stock_name_setter(stock_name)  # setting name of the stock taken from the user
        s1.no_of_share_setter(no_of_share)  # setting number of stocks, input taken from the user
        s1.share_price_setter(share_price)  # setting share price taken from the user

        objects.append(s1)  # appending all the objects created one by one to the list 'objects'
        count += 1
        print()

    # this method calculate individual Stocks total stock value having @param objects and @param index and @return stock
    # value which is calculated total value of individual stock
    def cal_stock_val(objects, index):
        # multiplying price of one share and the number of shares to calculate the value of individual stock
        stock_value = objects[index].no_of_share_getter() * objects[index].share_price_getter()
        return stock_value

    # this method calculate total value of all stocks having @param objects and @return total calculated stocks value
    def cal_total_stocks_value(objects):
        total_stocks_value = 0
        for i in range(len(objects)):
            # multiplying price of one share and the number of shares to calculate the value of individual stock and
            # adding in a variable to get grand total value of all Stocks
            total_stocks_value += objects[i].no_of_share_getter() * objects[i].share_price_getter()
        return total_stocks_value

    print(" >>> Stock Report <<<\n----------------------")
    for i in range(len(objects)):
        print(" Stock Name:", objects[i].stock_name_getter(), "\n", "Number of Share:", objects[i].no_of_share_getter(),
              "\n",
              "Share Price:", objects[i].share_price_getter(), "\n", "Value of", objects[i].stock_name_getter(), ":",
              cal_stock_val(objects, i), "\n")

    print(">>> Value of total stocks:", cal_total_stocks_value(objects), "<<<")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    stock = StockPortfolio()  # creating object of 'StockPortfolio' class
