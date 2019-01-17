"""In this program a JSON file is created having Inventory Details for
Rice, Pulse and Wheat with properties name, weight, price per kg. With
the help of 'json' module reading the JSON file.

@author Amit Kumar
@version 1.0
@since 10/01/2019
"""
# Importing important modules
import json


# Inventory class
class Inventory:
    # run_inventory method read the JSON file and convert it to the Dictionary object printing each type of grains
    # with their every keys and values and printing them
    @staticmethod
    def run_inventory():
        global dataStore, type  # declaring variables as a global variable
        f = open('Problem1.json', 'r')  # opening the JSON file and reading it
        dataStore = json.load(f)  # after reading the whole JSON file converting it to the Dictionary object

        for i in range(len(dataStore)):  # this loop access all the keys and values present in the dictionary
            if i == 0:  # here we are assigning the variable 'type' as Rice if the index of the Dictionary is 0(zero)
                type = "Rice"
            if i == 1:
                type = "Pulse"
            if i == 2:
                type = "Wheat"

            # printing each properties of each grain after Dictionary which we get after converting the JSON file
            print("\nGrain Type: ", type, "\n-------------------")
            for j in range(len(dataStore[type])):
                print("Name: ", dataStore[type][j]['name'])
                print("Weight: ", dataStore[type][j]['weight'])
                print("Price per kg: ", dataStore[type][j]['price'])
                print("Total Price: ", (dataStore[type][j]['weight'])*(dataStore[type][0]['price']))
                print()


# from this python file only program will compile not from the imported file
if __name__ == '__main__':
    obj = Inventory()  # creating object of Inventory class
    obj.run_inventory()  # accessing 'run_inventory' method through object reference variable
