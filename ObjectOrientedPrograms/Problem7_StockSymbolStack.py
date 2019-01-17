"""This program is extension of Problem 5 and in this program it
maintain the Stock Symbol Purchased or Sold in a Stack implemented using
Linked List to indicate transactions done.

@author Amit Kumar
@version 1.0
@since 14/01/2019
"""
# importing important modules
import json
from DataStructureProgram.Stack import *

s1 = Stack()  # creating object of Stack class to access all the method present in that class
company_sym = json.load(open("Problem7_transaction.json", "r"))  # opening and reading the 'company' JSON file and
# converting it to the python Dictionary storing in a variable


# this function push the symbol of the companies to the created Stack
def push_symbols():
    for val in range(len(company_sym['transaction'])):  # traversing through the Dictionary
        type = str(company_sym['transaction'][val]["buy_sell"])  # converting type of transaction to string for
        # concatenation
        s1.push(company_sym['transaction'][val]["company_symbol"]+" - "+type)  # concatenating company symbol and the
        # type of transaction done and pushing it to the Stack
    print("\nCompanies symbol added to the Stack\n")


# this method pop out the element from the Stack
def pop_symbol():
    popped = s1.pop()  # popping the element
    print("\n'", popped, "' popped(deleted) from the Stack\n")


# 'Symbol' as Main class
class Symbol:
    while True:
        # displaying main menu
        print("\n-----------Company Symbol Stack-----------")
        print("enter 1.To add company symbols to Stack")
        print("enter 2.To delete company symbols from Stack")
        print("enter 3.To display companies symbol of Stack")
        print("enter 4.For Exit")

        global choice
        try:
            choice = int(input("\nEnter your choice: "))
        except Exception as e:  # handling the exception for user-input
            print(e, "\n!!! Invalid Input !!!\n")
        try:
            if choice == 1:
                push_symbols()  # calling 'push_symbols' function
            elif choice == 2:
                pop_symbol()  # calling 'pop_symbol' function
            elif choice == 3:
                print()
                s1.display()  # printing the elements of the Stack
            elif choice == 4:
                print("\nClosing.....")
                print("Closed Successfully")
                exit(0)  # terminating the program
            else:
                print("Invalid choice !!! Please Try again")
        except Exception as e:
            print(e, "\n!!! Invalid Input !!!\n")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    s1 = Symbol()  # creating object of 'Symbol'
