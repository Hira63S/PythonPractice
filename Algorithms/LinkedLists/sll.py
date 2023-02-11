''' Singly Linked List'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class linkedList:
    def __init__(self, val):
        self.val = val
        self.node = Node(self.val)
