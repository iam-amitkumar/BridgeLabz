"""This program read a List of Numbers from a file and arrange it ascending Order in a
Linked List. Take user input for a number, if found then pop the number out of the
list else insert the number in appropriate position.

@author Amit Kumar
@version 1.0
@since 08/01/2019
"""
# importing important modules
from DataStructureProgram.LinkedList import *

global f, search1
l1 = SingleLinkedList()


def insert_element_in_order(ele):
    l1.insert_at_end(ele)
    return l1.bubble_sort()


try:
    # reading each lines of file as word and appending it to the LinkedList
    with open('/home/admin1/PycharmProjects/BridgeLabzz/DataStructureProgram/OrderedList.txt', 'r') as f:
        for line in f:
            for num in line.split():  # splitting the sentence of the file into words
                l1.insert_at_end(int(num))  # user-defined method to append an item to the list
# handling the exception if file is not fount while reading
except FileNotFoundError:
    print("\nYour file not found on your drive. \nPlease check the name or path of the file.")
finally:
    f.close()  # closing the opened file

    l1.bubble_sort()  # sorting the LinkedList through bubble-sort technique
    l1.display_list()  # printing the LinkedList after sorting

try:
    search1 = int(input("\nEnter your number to search: "))
except Exception as e:  # handling the exception on user-input for searching the word in the file
    print(e)

if l1.search(search1):  # checking whether the the number searched by the user is present in the list or not
    l1.delete_node(search1)  # if the number is present then deleting the number from the LinkedList
else:
    insert_element_in_order(search1)  # if the number not found in the LinkedList then adding that number in the
    # LinkedList in sorted form

l1.display_list()  # printing the LinkedList after adding/removing the number in/from the LinkedList
l1.append_list_to_file_problem2()  # adding/removing the number in/from the file
print("\nText file Updated")
