''' Binary Tree '''
'''
Traversing traversal:
Inorder - left root -> main root -> right child
Preorder - visit the root, then left and right
Postorder
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tr.root, "")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")
            return False
    def preorder_print(self, start, traversal):
        # start at the main root and
        # Right -> left -> Right
        # ars = []
        if start:
            traversal += (str(start.val) + '-')
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
            # ars.append(root.val)
            # if root.left:
            #     ars.append(root.left.val)
            # if root.right:
            #     ars.append(root.right.val)




# binary tree traversals
tr = BinaryTree(1)
tr.root.left = Node(2)
tr.root.right = Node(3)
tr.root.left.left = Node(4)
tr.root.left.left = Node(42)
tr.root.left.right = Node(69)
tr.root.right.left = Node(32)
tr.root.right.right = Node(43)
print(tr.root.left.val)
print('tree is here')
# print()
print(tr.print_tree("preorder"))
