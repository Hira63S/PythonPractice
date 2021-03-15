"""Singly LinkedList Implementation from Scratch """

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # def insert_after(self, value):
    #     current_next = self.next
    #     self.next = ListNode(value, self, current_next)
    #     if current_next:
    #         current_next.prev = self.next
# class SLL:

    # def __init__(self, head, next):


    def insert_after(self, value):
        """ Going to call this on a node and pass in a value to add """

        # we are at a node i.e. 44
        # save the next node info:
        # current_node = self.value
        current_next = self.next
        # this would be 39 node
        # now create a new node;
        new_node = Node(value, current_next)
        self.next = new_node
        curr_node = self.next
        curr_node.next = current_next
        # we create the new node and also connect it to our current next_node.
        # now, we need to move the pointer from point 44-> 39 to 44 -> new_node -> 39
        # if current_next:
            # we can't use previous because this is a singly linked list
            # self.next = current_next

node_node = Node(42, 35)

print(node_node.value, node_node.next)
print(node_node.value)
node_node.insert_after(39)
# print(node_node.value, node_node.next.value, node_node.next.next)
node_next = node_node.next
print(node_next.next)
# print(node_node(42))
