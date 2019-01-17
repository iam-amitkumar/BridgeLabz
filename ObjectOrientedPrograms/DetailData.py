"""This python file is part of Problem 5 having all the
important methods necessary for question 5.

@author Amit Kumar
@version 1.0
@since 13/01/2019
"""
# importing important modules
import datetime
import json
from ObjectOrientedPrograms.Customer import *
from ObjectOrientedPrograms.Company import *
from ObjectOrientedPrograms.Transaction import *

customer_info = json.load(open("customer.json", "r"))  # opening and reading the 'customer' JSON file and
# converting it to the python Dictionary storing in a variable

name_keys = list(customer_info["customers"])
# company_info = {}
company_info = json.load(open("company.json", "r"))  # opening and reading the 'company' JSON file and
# converting it to the python Dictionary storing in a variable
transaction_obj = json.load(open("transaction.json", "r"))  # opening and reading the 'transaction' JSON file and
# converting it to the python Dictionary storing in a variable


# this method write the customer information to the customer JSON file after taking the @param customer object contains
# all the information about customer
def save(customer_obj):
    for data in name_keys:
        if customer_info["customers"][data]["cname"] == customer_obj.get_customer_name():
            print("Data already found in Database! Please insert a new data.\n")
            break
        else:
            customer_info["customers"][customer_obj.get_customer_name()] = ({
                'cname': customer_obj.get_customer_name(),
                'noOfShare': customer_obj.get_noOfShare(),
                'amount': customer_obj.get_amount(),
            })
            with open('customer.json', 'w') as data:  # writing the data to the customer.json file
                json.dump(customer_info, data, indent=2)
    print("\nPerson Detail Added Successfully!\n")


# this function is search for the given company and return None if the company name given as argument not found
def searchCompany(symbol):
    try:
        companylist = json.load(open('company.json', 'r'))
        name_keys = list(companylist.keys())
        count = 0
        for data in name_keys:
            if companylist[data]["company_symbol"] == symbol:
                count += 1
                company_name = companylist[data]["company_name"]
                company_symbol = companylist[data]["company_symbol"]
                total_share = companylist[data]["total_share"]
                share_Price = companylist[data]["share_Price"]
        try:
            new_obj = {
                "company_name": company_name,
                "company_symbol": company_symbol,
                "total_share": total_share,
                "share_Price": share_Price
            }
        except Exception as e:
            print("\n", e)
        if count == 0:
            return None
        else:
            return new_obj

    except SyntaxError:
        print("error in name")


# this function is search for the given customer and return None if the customer name given as argument not found
def searchCustomer(name):
    try:
        customerlist = json.load(open('customer.json', 'r'))
        name_keys = list(customerlist["customers"].keys())
        count = 0
        for data in name_keys:
            if data == name:
                count += 1
                customername = customerlist["customers"][data]["cname"]
                no_of_share = customerlist["customers"][data]["noOfShare"]
                amount = customerlist["customers"][data]["amount"]
        try:
            new_obj = {
                "cname": customername,
                "noOfShare": no_of_share,
                "amount": amount,
            }
        except Exception as e:
            print("\n", e)
        if count == 0:
            return None
        else:
            return new_obj

    except SyntaxError:
        print("error in name")


def buy(share_no, customer, company):
    customer_available_amount = int(customer_info["customers"][customer]["amount"])
    spending_amount = int(int(company_info[company]["share_Price"]) * share_no)
    if share_no <= int(company_info[company]["total_share"]):
        if spending_amount <= customer_available_amount:

            transaction = Transaction()

            transaction.set_customer_name(customer_info["customers"][customer]["cname"])
            transaction.set_company_symbol(company_info[company]["company_symbol"])
            transaction.set_buy_sell("Buy")
            transaction.set_total_share(share_no)
            transaction.set_total_price((int(company_info[company]["share_Price"]) * share_no))

            now = datetime.datetime.now()
            today = now.strftime("%Y-%m-%d %H:%M")
            transaction.set_time(today)
            transaction_obj["transaction"][transaction.get_customer_name()] = ({
                'customer_name': transaction.get_customer_name(),
                'company_symbol': transaction.get_company_symbol(),
                'buy_sell': transaction.get_buy_sell(),
                'total_share': transaction.get_total_share(),
                'total_Price': transaction.get_total_price(),
                'time': transaction.get_time()
            })
            with open('transaction.json', 'w+') as data:
                json.dump(transaction_obj, data, indent=2)
            print("\nTransaction Successful")

            company_info[company]['total_share'] -= share_no

            with open("company.json", "w") as company_data:
                json.dump(company_info, company_data, indent=2)

            customer_info["customers"][customer]["amount"] -= spending_amount
            customer_info["customers"][customer]["noOfShare"] += share_no

            with open("customer.json", "w") as company_data:
                json.dump(customer_info, company_data, indent=2)

        else:
            print("\n>>> Transaction Failed <<<\n>>> You don't have sufficient amount <<<")
    else:
        print("\nCompany don't have sufficient Share(s)\nPlease reduce your amount of Share(s)")


def sell(share_no, name, company_name):
    if share_no <= customer_info["customers"][name]["noOfShare"]:
        customer_info["customers"][name]["noOfShare"] -= share_no
        customer_info["customers"][name]["amount"] += (company_info[company_name]["share_Price"] * share_no)
        with open("customer.json", "w") as company_data:
            json.dump(customer_info, company_data, indent=2, sort_keys=True)

        company_info[company_name]["total_share"] += share_no
        with open("company.json", "w") as company_data:
            json.dump(company_info, company_data, indent=2, sort_keys=True)

        list_ = []
        transaction = Transaction()

        transaction.set_customer_name(customer_info["customers"][name]["cname"])
        transaction.set_company_symbol(company_info[company_name]["company_symbol"])
        transaction.set_buy_sell("Sell")
        transaction.set_total_share(share_no)
        transaction.set_total_price((int(company_info[company_name]["share_Price"]) * share_no))

        now = datetime.datetime.now()
        today = now.strftime("%Y-%m-%d %H:%M")
        transaction.set_time(today)
        transaction_obj["transaction"][transaction.get_customer_name()] = ({
            'customer_name': transaction.get_customer_name(),
            'company_symbol': transaction.get_company_symbol(),
            'buy_sell': transaction.get_buy_sell(),
            'total_share': transaction.get_total_share(),
            'total_Price': transaction.get_total_price(),
            'time': transaction.get_time()
        })

        list_.append(transaction_obj)
        with open('transaction.json', 'w') as data:
            json.dump(list_[0], data, indent=2)

        print("\n>>>         Transaction Successful         <<<")
        print("You have successfully sold your", share_no, "to", company_name)
        print("Your Shares deducted and equivalent money added to your account\n")
    else:
        print("\nYou don't have sufficient amount of share(s) to sell\n")


def buy_shares():
    name = input("\nEnter customer name: ")
    customer = searchCustomer(name)
    if customer is not None:
        DetailData.display_company_symbol()
        symbol = input("Choose and enter company symbol from above chart to Buy Shares : ")
        for data in company_info:
            if company_info[data]["company_symbol"] == symbol:
                company_name = company_info[data]["company_name"]
        company = searchCompany(symbol)
        if company is not None:
            # display only selected company details
            for data in company_info:
                if company_info[data]["company_symbol"] == symbol:
                    print("\nYour selected company details: \nName: ", company_info[data]["company_name"], "\nSymbol: ",
                          company_info[data]['company_symbol'],
                          "\nShare Price: ", company_info[data]['share_Price'], "\n")

            # display only selected available customer amount
            for data in name_keys:
                if customer_info["customers"][data]["cname"] == name:
                    print("--- Available amount of", name, "for transaction: ", customer_info["customers"][data]["amount"], "---\n")
            share_no = int(input("Enter the number of Shares you want to buy (take reference from above chart) : "))
            buy(share_no, name, company_name)
        else:
            print("\n!!! Company Not Found !!!")
    else:
        print("\n!!! Customer Not Found !!!")


def sell_share():
    name = input("\nEnter customer name: ")
    customer = searchCustomer(name)
    if customer is not None:
        DetailData.display_company_symbol()
        symbol = input("Choose and enter company symbol from above chart to sell Shares : ")
        for data in company_info:
            if company_info[data]["company_symbol"] == symbol:
                company_name = company_info[data]["company_name"]
        company = searchCompany(symbol)
        if company is not None:
            print("\n--- Available shares of", name, "is", customer_info["customers"][name]["noOfShare"], " ---\n")
            share_no = int(input("Enter the number of Shares you want to sell : "))
            sell(share_no, name, company_name)
        else:
            print("\n!!! Company Not Found !!!")
    else:
        print("\n!!! Customer Not Found !!!")


class DetailData:
    @staticmethod
    def add_customer():
        print("Customer Information")
        name = input("enter customer name : ")
        amount = int(input("enter a amount : "))
        no_of_share = int(input("Enter the Number Of Share : "))
        customer_obj = Customer(name, amount, no_of_share)
        customer_obj.set_customer_name(name)
        customer_obj.set_amount(amount)
        customer_obj.set_noOfShare(no_of_share)
        save(customer_obj)

    @staticmethod
    def add_company():
        print("Customer Information")
        company_name = input("enter company name : ")
        company_symbol = input("enter a company Symbol : ")
        share_price = int(input("Enter the Price Of Share : "))
        total_share = int(input("Enter the total Number Of Share : "))
        company_obj = Company(company_name, company_symbol, share_price,total_share)
        company_obj.set_company_name(company_name)
        company_obj.set_company_symbol(company_symbol)
        company_obj.set_share_price(share_price)
        company_obj.set_total_share(total_share)
        for data in range(len(company_info)):

            if data == company_obj.get_company_name():
                print("Data already found in Database! Please insert a newly data.\n")
                break
            else:
                company_info[company_obj.get_company_name()] = ({
                    "company_name": company_obj.get_company_name(),
                    "company_symbol": company_obj.get_company_symbol(),
                    "share_Price": company_obj.get_share_price(),
                    "total_share": company_obj.get_total_share()
                })
                with open('company.json', 'w') as data:
                    json.dump(company_info, data, indent=2)
        print("\nCompany Detail Added Successfully!\n")

    @staticmethod
    def display_customer():
        customer_info_ = json.load(open("customer.json", "r"))
        name_keys_ = list(customer_info["customers"])
        for data in name_keys_:
            print("Name: ", customer_info_["customers"][data]["cname"], "\nNumber of Share: ",
                  customer_info_["customers"][data]["noOfShare"], "\nAmount: ",
                  customer_info_["customers"][data]["amount"], "\n")
        print()

    @staticmethod
    def display_company():
        for data in company_info:
            print("Name: ", company_info[data]["company_name"], "\nSymbol: ", company_info[data]['company_symbol'],
                  "\nShare Price: ", company_info[data]['share_Price'], "\n")
        print()

    @staticmethod
    def transaction():
        print("Enter 1.Buy Share")
        print("Enter 2.Sell Share")
        try:
            choice = int(input("\nEnter your choice : "))
        except Exception as e:
            print(e, " Invalid Input")

        if choice == 1:
            buy_shares()
        elif choice == 2:
            sell_share()
        else:
            print("\nInvalid Input\n")

    @staticmethod
    def display_company_symbol():
        print("\n Symbol Reference Chart of Companies\n"
              "--------------------------------------")
        for data in company_info:
            print("Name: ", company_info[data]["company_name"], "\nSymbol:", company_info[data]["company_symbol"], "\n")
