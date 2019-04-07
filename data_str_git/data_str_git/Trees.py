# To create a tree from scratch
class node:
    """To create nodes each time an instance has been
    created"""

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def traversal(self, root):
        """To traverse the tree's root ,left and rightmost node"""
        if root:
            print(root.data)
            abc=self.traversal(root.left)

            self.traversal(root.right)



"""To insert the data manually"""
root = node(10)
root.left = node(20)
root.right = node(30)
root.left.left = node(50)
root.traversal(root)


#