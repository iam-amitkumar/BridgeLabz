"""This program read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file.

@author Amit Kumar
@version 1.0
@since 07/01/2019
"""
# importing important modules
from DataStructureProgram.LinkedList import *

# creating object of SingleLinkedList class of DataStructureProgram package to access all the methods
l1 = SingleLinkedList()

try:
    # reading each lines of file as word and appending it to the LinkedList
    with open('UnorderedList1.txt', 'r') as f:
        for line in f:
            for word in line.split():  # splitting the sentence of the file into words
                l1.insert_at_end(word)  # user-defined method to append an item to the list

    l1.display_list()

    try:
        search1 = str(input("\nEnter your string to search: "))

        if l1.search(search1):
            l1.delete_node(search1)
        else:
            l1.insert_at_end(search1)
    except Exception as e:  # handling the exception on user-input for searching the word in the file
        print(e)

    # displaying the list created from the file
    l1.display_list()

    # appending/deleting the searched word by the user
    l1.append_list_to_file()

# handling the exception if file is not fount while reading
except FileNotFoundError:
    print("\nYour file not found on your drive. \nPlease check the name or path of the file.")
