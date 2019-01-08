"""Class present in this file contains the important methods for Stack like:
to push data into the stack
to pop data from the stack
to check whether the Stack is empty or not
to print all the elements present in the Stack etc.

@author Amit Kumar
@version 1.0
@since 08/01/2019
"""


# class EmptyStackError to raise the Exception whenever Stack is empty while trying to pop the data from the Stack
class EmptyStackError(Exception):
    pass


# class Node
class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


# class Stack contains important methods regarding Stack
class Stack:
    # constructor
    head = None

    def __init__(self):
        self.top = None

    # method to check whether the Stack is empty or not
    def is_empty(self):
        return self.top is None

    # method to push the data on the top of the Stack
    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp

    # method to pop/remove the data at the top from the Stack
    def pop(self):
        if self.is_empty():  # checking for empty Stack
            raise EmptyStackError("\nStack is Empty")
        popped = self.top.info
        self.top = self.top.link
        return popped

    # method to print all the elements of the Stack
    def display(self):
        if self.is_empty():  # checking for empty Stack
            print("\nStack is empty")
            return

        print("Stack is: ")
        p = self.top
        while p is not None:
            print(p.info, " ")
            p = p.link

    def element_at(self, index):
        temp = self.head
        for i in range(0, index):
            temp = temp.next
        return temp.data

    def size(self):
        if self.is_empty():
            return 0

        count = 0
        p = self.top
        while p is not None:
            count += 1
            p = p.link
        return count
