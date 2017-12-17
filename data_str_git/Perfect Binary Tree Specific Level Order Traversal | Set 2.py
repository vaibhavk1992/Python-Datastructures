###We followed the second approach from gfg.storing the left of one node and right of one node at a time
##and right of a node and left of node the other time
# Python program for special order traversal

# A binary tree ndoe
class Node:
    #Create  queue and enqueue  left and right child of root
    s=[]
    q=[]
    #variable to traverse the reversed array
    elements=0
    # A constructor for making a new node
    def __init__(self,key):
        self.data=key
        self.left=None
        self.right=None

    # Given a perfect binary tree print its node in
    # specific order
    def printSpecificLevelOrder(self,root):
        self.s.append(root)
        #Pop the element from the list
        prnt=self.s.pop(0)
        self.q.append(prnt.data)
        if prnt.right:
            self.s.append(root.right)
        if prnt.left:
            self.s.append(root.left)
        # Traversal loop
        while(len(self.s)>0):
             # Pop two items from queue
             first=self.s.pop(0)
             self.q.append(first.data)
             second = self.s.pop(0)
             self.q.append(second.data)
             # Since it is perfect Binary tree,
             # one of the node is needed to be checked
             if first.left and second.right and first.right and second.left:
                 # If first and second have grandchildren,
                 # enqueue them in reverse order
                 self.s.append(first.left)
                 self.s.append(second.right)
                 self.s.append(first.right)
                 self.s.append(second.left)

        # Give a perfect binary tree print its node in
        # reverse order
        for elements in reversed(self.q):
            print(elements)

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

root.left.left.left.left = Node(16)
root.left.left.left.right = Node(17)
root.left.left.right.left = Node(18)
root.left.left.right.right = Node(19)
root.left.right.left.left = Node(20)
root.left.right.left.right = Node(21)
root.left.right.right.left = Node(22)
root.left.right.right.right = Node(23)
root.right.left.left.left = Node(24)
root.right.left.left.right = Node(25)
root.right.left.right.left = Node(26)
root.right.left.right.right = Node(27)
root.right.right.left.left = Node(28)
root.right.right.left.right = Node(29)
root.right.right.right.left = Node(30)
root.right.right.right.right = Node(31)
root.printSpecificLevelOrder(root)

