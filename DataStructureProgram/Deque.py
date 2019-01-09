"""Class Deque contains the important methods for Deque like:
to insert an item to the front of the Deque
to insert an item to the rear of the Deque
to remove an item from the front of the Deque
to remove an item from the back of the Deque
to check whether the Deque is empty or not
to return the size of the Deque etc.

@author Amit Kumar
@version 1.0
@since 08/01/2019
"""


class Deque:
    # used to initialise with the items
    def __init__(self):
        self.items = []

    # used to check whether the Deque is empty or not
    def is_empty(self):
        return self.items == []

    # used to insert an item to the front of the Deque
    def insert_front(self, item):
        self.items.append(item)

    # used to insert an item to the rear of the Deque
    def insert_rear(self, item):
        self.items.insert(0, item)

    # used to remove an item from the front of the Deque
    def remove_front(self):
        return self.items.pop()

    # used to remove an item from the back of the Deque
    def remove_rear(self):
        return self.items.pop(0)

    # used to check the size of the Deque
    def size(self):
        return len(self.items)
