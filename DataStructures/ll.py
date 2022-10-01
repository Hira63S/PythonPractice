''' Linked List Basics'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList starting out:
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, new_node):
        curr = self.head
        if curr:
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node
'''
    def insert(self,head,data):
    #Complete this method
        # curr = head
        new_node = Node(data)
        head_node = Node(data) # now head has a data and a .next thing
        if head is None:
            head = head_node

        else:
            #$ this is what we call a pointer in the linked list 
            curr_node = head
            while curr_node.next:
                # print(head_node)
                curr_node = curr_node.next

                # print(head_node.data)
            curr_node.next = new_node
            # return head_node
        return head
'''
    def print(self):
        curr = self.head
        while(curr):
            print(curr.value)
            curr = curr.next
            # print(curr.value)

    def delete(self, value):
        # go to the head
        curr = self.head
        # if the value we are at is the correct value
        # set the head to next value and that way this value will be ignored

        if curr.value == value:
            self.head = curr.next
        #
        else:
            while curr:
                if curr.value == value:
                    # if the value is the correct one, break
                    break
                prev = curr
                curr = curr.next
            if curr == None:
                return
            prev.next = curr.next
            curr = None

# test:
# define nodes:
n1 = Node(2)
n2 = Node(3)
n3 = Node(50)
l1 = LinkedList(n1)
l1.print()
# l2 = l1.insert(n2)
l1.insert(n2)
l1.insert(n3)
l1.print()
l1.delete(3)
l1.print()
# l2.print()
# print(l1.new_node)
# l1 = LinkedList.insert(Node(3))
# print()
