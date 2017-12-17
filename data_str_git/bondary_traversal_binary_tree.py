"""Here first we traverssed the left part of the treee then the leaves
 then the right part of the tree"""
class node:
    lst=[]
    flag=True
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def top_to_bottom(self,root):
        if root and self.flag==True:
            print(root.data)
            self.flag=False
            self.top_to_bottom(root.left)
        elif root and self.flag==False:
            print(root.data)
            self.top_to_bottom(root.left)
            if root.right:
                self.lst.append(root.right)


    def leaf_traversals(self):
        while(len(self.lst)>0):
            current=self.lst.pop(0)
            if current.right:
                self.lst.append(current.right)
            while(current.left):
                current=current.left
            print(current.data)
    def bottom_to_up_leafs_append(self,root,d1):
        if d1==0:
            self.bottom_to_up_leafs_append(root.right,d1+1)

        elif root :
            if root.left :
              self.lst.append(root.left)
            self.bottom_to_up_leafs_append(root.right,d1+1)

    def bottom_to_up(self,root,d):
        if d==0:
            self.bottom_to_up(root.right,d+1)

        elif root :
            self.bottom_to_up(root.right,d+1)
            print(root.data)

root=node("10")
root.left=node("11")
root.left.left=node("12")
root.left.right=node("15")
root.left.right.left=node("16")
root.left.right.right=node("17")
root.left.right.right=node("18")
root.right=node("12")
root.right.left=node("13")
root.right.left.left=node("40")
root.right.right=node("14")
root.right.right.left=node("20")
root.top_to_bottom(root)
root.leaf_traversals()
root.bottom_to_up_leafs_append(root,0)
root.leaf_traversals()
root.bottom_to_up(root,0)
