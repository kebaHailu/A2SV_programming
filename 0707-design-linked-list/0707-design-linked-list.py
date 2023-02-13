class Node:
    def __init__(self, val=0):

        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):

        self.head = None
        self.size = 0

    def get(self, index):

        if index >= self.size:
            return -1
        if index == 0:
            return self.head.val
        else:
            temp = self.head
            for i in range(index-1):
                temp = temp.next
            return temp.next.val

    def addAtHead(self, val):

        if self.size == 0:
            self.head = Node(val)
        else:
            temp = self.head
            self.head = Node(val)
            self.head.next = temp
        self.size += 1

    def addAtTail(self, val):

        if self.size == 0:
            self.head = Node(val)
        elif self.size == 1:
            self.head.next = Node(val)
        else:
            temp = self.head
            for i in range(self.size-1):
                temp = temp.next
            temp.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):

        if index > (self.size):
            return
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        temp2 = temp.next
        temp.next = Node(val)
        temp = temp.next
        temp.next = temp2
        self.size += 1

    def deleteAtIndex(self, index):

        if self.size == 0:
            return
        if index > (self.size - 1):
            return
        if index < 0:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        temp = self.head
        for i in range(index-1):
            temp = temp.next
        temp.next = temp.next.next
        self.size -= 1