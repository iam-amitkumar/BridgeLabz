"""This program is extension of Problem 1, Creating InventoryManager to manage the
Inventory. The Inventory Manager will use InventoryFactory to create Inventory
Object from JSON. The InventoryManager will call each Inventory Object in its list
to calculate the Inventory Price and then call the Inventory Object to return the
JSON String. The main program will be with InventoryManager.

@author Amit Kumar
@version 1.0
@since 12/01/2019
"""
# importing important modules
from ObjectOrientedPrograms.Problem4_Methods import *


# this function display all the data present in the JSON file after converting it to the Dictionary
def display_inventory():
    global type  # globalizing the variable 'type'
    for i in range(len(data['inventory'])):
        # assigning the type of grain name according the index of dictionary
        if i == 0:
            type = "Rice"
        if i == 1:
            type = "Pulse"
        if i == 2:
            type = "Wheat"

        # printing the details of all the grains after accessing the Dictionary of converted JSON file
        print("\nGrain Type: ", type, "\n-------------------")
        for j in range(len(data['inventory'][type])):  # traversing throughout the Dictionary and accessing the elements
            print("Name: ", data['inventory'][type][j]['Name'])
            print("Weight: ", data['inventory'][type][j]['weight'])
            print("Price per kg: ", data['inventory'][type][j]['Price'])
            print("Total Price: ", (data['inventory'][type][j]['weight']) * (data['inventory'][type][j]
                  ['Price']))
            print()


# this function is using to buy the grain from the Inventory which will reflect the amount purchased in the JSON file
def buy_item():
    print("\nChoose the item to purchase and add to Inventory\nPress 1 to purchase Rice\nPress 2 to "
          "purchase pulses\nPress 3 to purchase wheat\n")  # displaying sub-menu
    try:
        choice = int(input("Enter your opinion: "))
        # assigning the type of grain name according the index of dictionary
        if choice == 1:
            name = "Rice"
        elif choice == 2:
            name = "Pulse"
        elif choice == 3:
            name = "Wheat"
        else:
            print("Invalid choice")
        for j in range(len(data['inventory'][name])):  # traversing throughout the Dictionary and accessing the elements
            print(j + 1, data['inventory'][name][j]['Name'])
        choice = int(input("\nEnter your opinion: "))  # getting the grain name from the user buy
        print("Enter weight of", name, "you want purchase and add to Inventory: ")
        weight = int(input())  # getting the weight of selected grain to buy
        purchase_item(name, weight, choice)  # passing all necessary arguments to the method for further process
    except Exception as e:  # handling the exception for bad input
        print(e)
        print("Invalid Input")


# this function is using to sell the grain from the Inventory which will reflect the amount purchased in the JSON file
def sell_items():
    print("\nChoose the item to sell\nPress 1 to sell Rice\nPress 2 to sell pulses\nPress 3 to sell "
          "wheat\n")  # displaying sub-menu
    try:
        choice = int(input("Enter your opinion: "))
        # assigning the type of grain name according the index of dictionary
        if choice == 1:
            name = "Rice"
        elif choice == 2:
            name = "Pulse"
        elif choice == 3:
            name = "Wheat"
        else:
            print("Invalid choice")
    except Exception as e:  # handling the exception for bad input
        print(e)
        print("Invalid Input")

    for j in range(len(data['inventory'][name])):  # traversing throughout the Dictionary and accessing the elements
        print(j + 1, data['inventory'][name][j]['Name'])
    choice = int(input("\nEnter your opinion: "))  # getting the grain name from the user buy
    print("Enter weight of", name, "you want sell from Inventory: ")
    weight = int(input())  # getting the weight of selected grain to buy
    sell_item(name, weight, choice)  # passing all necessary arguments to the method for further process


def add_new_item():
    # displaying sub-menu
    print("\nChoose the item to add\nPress 1 to add Rice\nPress 2 to add pulses\nPress 3 to add wheat\n")
    try:
        choice = int(input("Enter your opinion: "))
        # assigning the type of grain name according the index of dictionary
        if choice == 1:
            name = "Rice"
            inventory_detail(name)  # passing the grain name to the 'inventory_detail' method to get details of
            # selected grain to write on JSON file
        elif choice == 2:
            name = "Pulse"
            inventory_detail(name)  # passing the grain name to the 'inventory_detail' method to get details of
            # selected grain to write on JSON file
        elif choice == 3:
            name = "Wheat"
            inventory_detail(name)  # passing the grain name to the 'inventory_detail' method to get details of
            # selected grain to write on JSON file
        else:
            print("\nInvalid choice")
    except Exception as e:  # handling the exception for bad input
        print(e)
        print("Invalid Input")


# 'DataManagement' class contains the Main menu options
class DataManagement:
    while True:
        # displaying main menu
        print("\n                MENU\n"
              "-----------------------------------------\n"
              "1. Press 1 to display Inventory\n"
              "2. Press 2 to purchase item and add to the Inventory\n"
              "3. Press 3 to sell item from Inventory\n"
              "4. Press 4 to add new item in Inventory\n"
              "5. Press 5 to Exit \n")
        global option  # globalizing th variable 'option'
        try:
            option = int(input("Enter your opinion: "))
        except Exception as e:  # handling the exception for the user-input
            print(e)  # handling the exception for bad input

        try:
            if option == 1:
                display_inventory()  # calling 'display_inventory' method
            elif option == 2:
                buy_item()  # calling 'buy_item' method
            elif option == 3:
                sell_items()  # calling 'sell_item' method
            elif option == 4:
                add_new_item()  # calling 'add_new_item' method
            elif option == 5:
                print("\nClosing Inventory..... \nInventory Closed.")
                exit(0)
            else:
                print("Invalid Input")
        except Exception as e:  # handling exception for bad input
                print(e)
                print("Invalid Input")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    obj = DataManagement()  # creating object of 'DataManagement' to access all functionality present in that class
