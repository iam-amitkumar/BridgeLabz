"""This program is an part of Problem 4 which contains a class and
important methods like:
i. inventory_detail
ii. sell_item
iii. purchase_item


@author Amit Kumar
@version 1.0
@since 12/01/2019
"""
# importing important modules
import json

data = json.load(open("Problem4.json", "r"))   # opening the JSON file and reading it and after reading the whole JSON
# file converting it to the Dictionary object


# this method add the particular grain type after getting all the details regarding that grain
def inventory_detail(inventory_name):
    global weight_, price, name  # globalizing the variables
    try:
        print("Enter the", inventory_name, " name:")
        name = input()
        print("Enter the price:")
        price = int(input())
        print("Enter weight you want to add: ")
        weight_ = int(input())
        print("\nSaving Data.....\n"
              "Data successfully Saved\n")
    except Exception as e:  # handling the exception of bad input
        print(e)

    amount = int(price * weight_)  # finding the total amount and casting it in integer
    obj1 = Inventory(name, price, weight_, amount, inventory_name)  # creating object of Inventory through constructor
    obj1.update_inventory()  # writing newly created object of grain


# this method is used to sell the selected grain with user-input of @param item, @param weight and @param choice
def sell_item(item, weight, choice):

    last_weight = data["inventory"][item][choice-1]['weight']  # storing initial weight to a new variable
    if data["inventory"][item][choice-1]['weight'] - weight > 0:  # checking whether the amount user buying is available
        # or not
        data["inventory"][item][choice-1]['weight'] -= weight  # if available then deduct the sold value from the
        # JSON file
    else:
        print("\nYou don't have sufficient amount of ", item)

    with open("Problem4.json", "w") as inventory_data:  # writing the modified data to JSON file with proper indentation
        json.dump(data, inventory_data, indent=2, sort_keys=True)
    print("\nWeight of", data["inventory"][item][choice-1]['Name'], item, "updated from", last_weight, "to",
          last_weight - weight)
    print("\n>> Total amount :", weight * data["inventory"][item][choice - 1]['Price'], '<<\n')


# this method is used to purchase the selected grain with user-input of @param item, @param weight and @param choice
def purchase_item(item, weight, choice):

    last_weight = data["inventory"][item][choice-1]['weight']  # storing initial weight to a new variable
    data["inventory"][item][choice-1]['weight'] += weight  # adding the purchased value to the JSON file to the
    # respective grain

    with open("Problem4.json", "w") as inventory_data:  # writing the modified data to JSON file with proper indentation
        json.dump(data, inventory_data, indent=2, sort_keys=True)
    print("\nWeight of", data["inventory"][item][choice-1]['Name'], item, "updated from", last_weight, "to",
          last_weight + weight)
    print("\n>> Total amount :", weight * data["inventory"][item][choice - 1]['Price'], '<<\n')


# 'Inventory' class
class Inventory:
    # custom constructor to initialize the values
    def __init__(self, name, price, weight, amount, inventory_name):
        self.name = name
        self.price = price
        self.weight = weight
        self.amount = amount
        self.inventory_name = inventory_name

    # this method write data to JSON file
    def update_inventory(self):
        data["inventory"][self.inventory_name].append({
            "Name": self.name,
            "Price": self.price,
            "weight": self.weight,
        })
        with open("Problem4.json", "w") as inventory_data:  # writing the data to the JSON file with proper indentation
            json.dump(data, inventory_data, indent=2, sort_keys=True)
