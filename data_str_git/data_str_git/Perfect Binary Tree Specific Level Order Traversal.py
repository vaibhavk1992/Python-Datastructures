###We followed the second approach from gfg.storing the left of one node and right of one node at a time
##and right of a node and left of node the other time
class Node:
    lst=[]
    lst1 = []
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def boundary_traversal(self,root):
        self.lst.append(root)
        prnt=self.lst.pop(0)
        if prnt.left:
            self.lst.append(root.left)
        if prnt.right:
            self.lst.append(root.right)

        while(len(self.lst)>0):
             top=self.lst.pop(0)
             print(top.data)
             next_top = self.lst.pop(0)
             print(next_top.data)
             if top.left and next_top.right and top.right and next_top.left:
                 self.lst.append(top.left)
                 self.lst.append(next_top.right)
                 self.lst.append(top.right)
                 self.lst.append(next_top.left)
             else:
                 print("It's not a binary tree")
                 break

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

root.left.left.left.left  = Node(16)
root.left.left.left.right  = Node(17)
root.left.left.right.left  = Node(18)
root.left.left.right.right  = Node(19)
root.left.right.left.left  = Node(20)
root.left.right.left.right  = Node(21)
root.left.right.right.left  = Node(22)
root.left.right.right.right  = Node(23)
root.right.left.left.left  = Node(24)
root.right.left.left.right  = Node(25)
root.right.left.right.left  = Node(26)
root.right.left.right.right  = Node(27)
root.right.right.left.left  = Node(28)
root.right.right.left.right  = Node(29)
root.right.right.right.left  = Node(30)
root.right.right.right.right  = Node(31)
#root.right.right.left=node("14")
root.boundary_traversal(root)

"""
#Specific Level Order traversal of binary tree is
#1 2 3 4 7 5 6 8 15 9 14 10 13 11 12 16 31 17 30 18 29 19 28 20 27 21 26 22 25 23 24
"""