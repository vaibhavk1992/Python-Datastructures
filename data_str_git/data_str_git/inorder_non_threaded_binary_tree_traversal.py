# To create a tree from scratch
class node:
    """To create nodes each time an instance has been
    created"""

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

    def parent_search(self, root, child_node):
        if  root :
            if root.left and root.left.data== child_node:
                return root
            if root.right and root.right.data== child_node:
                return root
            elif root:
                return self.parent_search(root.left, child_node) or self.parent_search(root.right, child_node)


    def inorder_non_theaded_tree(self,root):
            leftdone=False
            current=root
            while(current):

                x = self.parent_search(root, current.data)
                if leftdone==False:
                     while(current):
                        if current.left:
                          current=current.left
                        else:
                          break
                     leftdone=True
                     print(current.data)
                elif current.right:
                    current=current.right
                    leftdone=False
                elif current==x.left:
                    current=x
                    print(current.data)
                elif current==x.right:
                    if x==self.parent_search(root,x.data).right:
                        print("adskakgh")
                        break
                    else:
                        current=self.parent_search(root,x.data)
                        print(current.data)


"""To insert the data manually"""
root = node(24)
root.right = node(27)
root.right.right = node(29)
root.right.right.right = node(34)

root.left = node(10)
root.left.left = node(4)
root.left.left.right = node(6)
root.left.right = node(13)
root.left.right.right = node(14)
root.left.right.right.right = node(22)
root.left.left.left = node(3)
root.left.left.left.left = node(2)
root.inorder_non_theaded_tree(root)

"""
root = node(10)
root.left = node(20)
root.left.left = node(90)
root.left.right = node(100)
root.left.left.left = node(80)
root.left.left.right = node(180)
root.right = node(30)
root.right.left = node(40)
root.right.left.left = node(70)
root.right.left.right = node(700)
root.right.right = node(50)
root.inorder_non_theaded_tree(root)


"""