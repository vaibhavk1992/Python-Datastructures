class node:
    lst=[]
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None

    def dualstack_po_traversal(self,obj1):
        lst1=[]
        lst2=[]
        lst1.append(obj1)
        while(len(lst1)>0):
            poped_node=lst1.pop(len(lst1)-1)
            lst2.append(poped_node.root)
            if poped_node.left:
                lst1.append(poped_node.left)
            if poped_node.right:
                lst1.append(poped_node.right)
        print(lst2)
        for i in reversed(lst2):
            print(i)
obj1=node("10")
obj1.left=node("11")
obj1.right=node("12")
obj1.left.left=node("13")
obj1.left.right=node("14")
obj1.right.left=node("15")
obj1.right.left.right=node("17")
#obj1.right.left.right.right=node("99")
obj1.dualstack_po_traversal(obj1)

