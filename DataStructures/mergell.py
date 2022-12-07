''' merage two sorted slls '''

'''
class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = next
'''

def mergesortedlist(self, listnode1, listnote2):
    l1 = listnode1
    l2 = listnode2

    while l1 and l2:
        if l1.val < l2.val:
            l1.next = l2
            l1 = l2
        elif l2 < l2:
            l2.next = l1
            l2 = l1
        if l1:
            l1.next = l1
            l1 = l2
        if l2:
            l2.next = l2
            l2 = l1



'''
Merge Sort: divide the right half of the list and further keep dividing the list, compare the left half and right half and then merge them


'''
