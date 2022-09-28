""" Doubly Linked List Implementation """


class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def insert_after(self, value):
