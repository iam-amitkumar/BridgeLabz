class EmptyQueueError(Exception):
    pass


class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def insert_front(self, item):
        self.items.insert(0, item)

    def insert_rear(self, item):
        self.items.append(item)

    def delete_front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items.pop()

    def first(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items[0]

    def last(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is Empty")
        return self.items[-1]

    def display(self):
        print(self.items)
