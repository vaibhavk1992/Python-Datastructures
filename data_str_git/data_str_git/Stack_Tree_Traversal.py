""" Tree Preorder traversal using stack"""
class node:

    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
    def preorder_traverse(self,obj1):
       if obj1 is None:
        return
       lst = []
       lst.append(obj1)
       while(len(lst)>0):
           if obj1 is None:
               return
           print(lst[len(lst)-1].root)
           node = lst.pop(len(lst)-1)
           if node.right is not None:
            lst.append(node.right)
           if node.left is not None:
            lst.append(node.left)
    def postorder_traverse(self,obj1):
       lst1=[]
       while(obj1):
           if obj1.right:
             lst1.append(obj1.right)
           lst1.append(obj1)
           obj1=obj1.left
       while(len(lst1)>0):
           obj2=lst1.pop(len(lst1)-1)
           if  obj2.right:
               lst1.append(obj2)
               obj2=obj2.right

               obj2 = lst1.pop(len(lst1) - 1)
               print(obj2.root)
               print("the lenth of list is ",len(lst1))
               obj2=None
           else:
               print(obj2.root)
               obj2=None

obj1=node("10")
obj1.left=node("11")
obj1.right=node("12")
obj1.left.left=node("13")
obj1.left.right=node("14")
#obj1.right.left=node("15")
#obj1.right.left.right=node("17")
obj1.preorder_traverse(obj1)
print("the postorder traversal is ")
obj1.postorder_traverse(obj1)



