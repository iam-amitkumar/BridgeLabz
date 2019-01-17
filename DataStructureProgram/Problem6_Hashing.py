"""In this program creating a Slot of 10 to store Chain of Numbers that belong
to each Slot to efficiently search a number from a given set of number.

Logic: Firstly store the numbers in the Slot. Since there are 10 Numbers divide
each number by 11 and the reminder put in the appropriate slot. Create a Chain
for each Slot to avoid Collision. If a number searched is found then pop it or
else push it. Use Map of Slot Numbers and Ordered LinkedList to solve the problem.
In the Figure Below, you can see number 77/11 reminder is 0 hence sits in the 0
slot while 26/11 remainder is 4 hence sits in slot 4.

@author Amit Kumar
@version 1.0
@since 09/01/2019
"""
# importing important modules
from DataStructureProgram.LinkedListHashing import *


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
                print("\nValue Present, deleting....")
                self.deletefile(prev, temp, hdata)
                flag = 1
            prev = temp
            temp = temp.next
            self.savefile(value, file)
        if temp is None and flag == 0:
            print("\nValue is not present, adding....")
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

#####################################################################################################################


ll = LinkList()
try:
    num = input("\nEnter the number you want to search: ")
    num = int(num)
    o = open("Problem6_Numbers.txt", 'r')
    read = o.read()
    read = read.lstrip()
    store = ""
    for i in range(len(read)):
        if read[i] != " ":
            store = store + read[i]
        if read[i] == " " or i == len(read) - 1:
            v = int(store)
            ll.insert(v)
            store = ""
    ll.find(num, "Problem6_Numbers.txt")
    print("\nThe values present currently are: ")
    ll.show()
    o.close()
except Exception as e:
    print(e)
