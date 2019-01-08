"""Class present in this file contains the important methods for Queue like:
to add data into the Queue
to delete data from the Queue
to check whether the Queue is empty or not
to print all the elements present in the Queue etc.

@author Amit Kumar
@version 1.0
@since 08/01/2019
"""


# EmptyQueueError class
class EmptyQueueError(Exception):
    pass


# Node class
class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


# Queue class contains all the methods of operation can do with Queue
class Queue:
    # constructor
    def __init__(self):
        self.front = None
        self.rear = None
        self.size_queue = 0

    # this method checks whether the queue is empty or not
    def is_empty(self):
        return self.front is None

    # this method return the size of the queue
    def size(self):
        return self.size_queue

    # this method add the user-input data into the queue
    def enqueue(self, data):
        temp = Node(data)
        if self.front is None:
            self.front = temp
        else:
            self.rear.link = temp
        self.rear = temp
        self.size_queue += 1

    # this method delete the user-input data from the queue
    def de_queue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        x = self.front.info
        self.front = self.front.link
        self.size_queue -= 1
        return x

    # this method print the entire element of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue is: ")
        p = self.front
        while p is not None:
            print(p.info, " ", end='')  # printing the elements one by one
            p = p.link
        print()
