"""'this program is extension of Problem 5 and in this program it
maintains the List of CompanyShares in a Linked List So new CompanyShares
can be added or removed easily.

@author Amit Kumar
@version 1.0
@since 14/01/2019
"""
# importing important modules
import json
from DataStructureProgram.LinkedList import *

l1 = SingleLinkedList()  # creating object of LinkedList class to access all the method present in that class
company_info = json.load(open("Problem6_company.json", "r"))  # opening and reading the 'company' JSON file and
# converting it to the python Dictionary storing in a variable


# 'add_companies' function adds each companies detail to the LinkedList node
def add_companies():
    for val in company_info:  # traversing the dictionary
        l1.insert_at_end(company_info[val])  # inserting each company details to the LinkedList
    print("\nCompanies detail successfully added to the LinkedList\n")


# 'show_symbols' function displays company name and their symbol for the user reference
def show_symbols():
    print("\n Company Name and their Symbol:")
    print("--------------------------------")
    for val in company_info:  # traversing through the dictionary
        print(company_info[val]["company_name"], "----> ", company_info[val]["company_symbol"])
    print()


# this function delete the node of the LinkedList containing particular company details after getting company symbol
# input from the user
def del_companies():
    show_symbols()  # calling show_symbols function to display symbols
    try:
        symbol = input("Enter the Symbol of companies: ")
        for val in company_info:  # traversing through the Dictionary to delete the user-input company details
            if symbol == company_info[val]["company_symbol"]:
                l1.delete_node(company_info[val])  # deleting the particular company detail from the LinkedList
                print("\nCompany details successfully deleted from the LinkedList\n")

    except Exception as e:  # handling the exception
        print(e)


# 'CompanyShare' as Main class
class CompanyShare:
    while True:
        # displaying main menu
        print("\n-----------Company Share Details-----------")
        print("enter 1.To add company to LinkedList")
        print("enter 2.To delete company from LinkedList")
        print("enter 3.To display companies of LinkedList")
        print("enter 4.For Exit")

        global choice
        try:
            choice = int(input("\nEnter your choice: "))
        except Exception as e:
            print(e, "\n!!! Invalid Input !!!\n")
        try:
            if choice == 1:
                add_companies()  # calling method to add company details
            elif choice == 2:
                del_companies()  # calling method to delete particular company detail
            elif choice == 3:
                l1.display_list()  # calling method to display LinkedList content
            elif choice == 4:
                print("\nClosing.....")
                print("Closed Successfully")
                exit(0)  # terminating the program
            else:
                print("Invalid choice !!! Please Try again")
        except Exception as e:  # handling the exception
            print(e, "\n!!! Invalid Input !!!\n")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    s1 = CompanyShare()  # creating object of 'CompanyShare'
