"""This file contains all the methods regarding LinkedList for
Problem 6(Hashing)

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""


class Node:
    data = None
    next = None


class LinkList:
    head = None
    for i in range(11):
        n = Node()
        if head is None:
            head = n
        else:
            temp = head
            while temp.next is not None:
                temp = temp.next
            temp.next = n

    def insert(self, value):
        new_node = Node()
        temp = self.head
        new_node.data = value
        pos = value % 11
        for i in range(pos):
            temp = temp.next
        if temp.data is None:
            temp.data = new_node
        else:
            temp = temp.data
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def find(self, value, file):
        flag = 0
        prev = None
        pos = value % 11
        temp = self.head
        for i in range(pos):
            temp = temp.next
        hdata = temp
        temp = temp.data
        while temp is not None:

            if value == temp.data:
                print("Value Present")
                self.deletefile(prev, temp, hdata)
                flag = 1
            prev = temp
            temp = temp.next
            self.savefile(value, file)
        if temp is None and flag == 0:
            print("Value is not present")
            self.insert(value)
            self.savefile(value, file)

    def savefile(self, ele, file):
            o = open(file, 'w')
            temp = self.head
            while temp is not None:
                temp1 = temp.data
                while temp1 is not None:
                    f = o.write(" " + str(temp1.data))
                    temp1 = temp1.next
                temp = temp.next
            o.close()

    def deletefile(self, prev, temp, hdata):
        next = temp.next
        if prev is None:
            hdata.data = next
        else:
          prev.next = next

    def show(self):
        temp = self.head
        while temp is not None:
                temp1 = temp.data
                while temp1 is not None:
                    print(temp1.data, end=" ")
                    temp1 = temp1.next
                print()
                temp = temp.next
