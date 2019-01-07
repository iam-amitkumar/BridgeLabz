"""Class present in this file contains the important methods for LinkedList like:
create LinkedList
search an element in LinkedList
delete a node in LinkedList
print the LinkedList
append an item in LinkedList, etc.

@author Amit Kumar
@version 1.0
@since 07/01/2019
"""


# Node class
class Node:
    def __init__(self, value):  # constructor
        self.info = value
        self.link = None


# SingleLinkedList class having the methods regarding LinkedList operation
class SingleLinkedList:
    def __init__(self):  # constructor
        self.start = None

# this method search specific element in the LinkedList
    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:  # matching the user-input item with each items of the list
                print(x, " is at position", position)
                return True
            position += 1
            p = p.link
        else:
            print(x, "not found in the list.")
            return False

# this method insert an element at the end of the LinkedList
    def insert_at_end(self, data):
        temp = Node(data)  # new temp node to add to the LinkedList
        if self.start is None:  # checking whether the LinkedList is empty or not
            self.start = temp
            return
        p = self.start
        while p.link is not None:
            p = p.link
        p.link = temp

# create_list method create a user-defined LinkedList after taking the input from the user
    def create_list(self):
        global n
        try:
            n = int(input("Enter the number of nodes: "))
        except Exception as e:
            print(e)

        if n == 0:
            return
        for i in range(n):
            try:
                data = int(input("Enter the elements to be inserted: "))
                self.insert_at_end(data)
            except Exception as e:
                print(e)

# this method remove a specific user-input element from the list
    def delete_node(self, x):
        if self.start is None:
            print("\nList is empty")
            return

        if self.start.info == x:  # deletion of first node
            self.start = self.start.link
            return

        p = self.start  # deletion in between or at the end
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link
        if p.link is None:
            print("Element ", x, "not in list")
        else:
            p.link = p.link.link

# display_list is used to print each item of LinkedList separated by space
    def display_list(self):
        if self.start is None:  # checking whether the LinkedList is empty or not
            print("\nList is empty.")
            return
        else:
            print("\nList is: ")  # printing the elements of the LinkedList if LinkedList is not empty
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

# this method write all the items present in the list to a text file
    def append_list_to_file(self):
        with open("UnorderedList1.txt", "w") as output:  # specific text file
            p = self.start
            while p is not None:
                output.write(str(p.info)+" ")  # writing the items of the list after adding or deleting to the file
                p = p.link
