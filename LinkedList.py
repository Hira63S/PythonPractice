"""
LinkedList
"""
class ListNode:

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_before(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_after(self,value):
        current_prev = self.prev
        self.prev = ListNode(value, self, current_next)
        if current_prev:
            current_prev.next = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
def DoublyLinkedList(data, prevNode, nextNode):
