# To create a tree from scratch
class node:
    """To create nodes each time an instance has been
    created"""
    lst1=[]
    lst2 =[]
    def __init__(self, key):
         self.data = key
         self.left = None
         self.right = None
    #def lst_apppend(self,value):

    def issame1(self,root1):
         if root1:
           if root1.left or  root1.right:
             return self.issame1(root1.left) or self.issame1(root1.right)
           if not root1.left or root1.right:
            self.lst1.append(root1.data)

    def issame2(self,root2):
         if root2:
           if root2.left or  root2.right:
             return self.issame2(root2.left) or self.issame2(root2.right)
           if not root2.left or root2.right:
            self.lst2.append(root2.data)


    def check_tree(self):
        print (self.lst1)
        print (self.lst2)
        if self.lst1==self.lst2:

            print("leaf nodes are equal")
        else:
            print("No leaf nodes are equal")
"""To insert the data manually"""
##First Tree
root1 = node(10)
root1.left = node(20)
root1.left.right = node(40)
root1.right = node(30)
root1.left.left = node(50)
root1.right.left = node(70)
root1.right.right = node(90)

##Second Tree
root2 = node(10)
root2.left = node(20)
root2.left.right = node(40)
root2.right = node(30)
root2.left.left = node(50)
root2.right.left = node(70)
root2.right.right = node(90)

root1.issame1(root1)
root2.issame2(root2)
root3=node(40)
root1.check_tree()

