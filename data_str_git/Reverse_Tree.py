class node:
    lst=[]
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
    def traverse(self,obj1):
       if obj1 is None:
           return
       print(obj1.root)
       self.traverse(obj1.left)
       self.traverse(obj1.right)
    def printlevel(self,obj1,current_level,level):

        if obj1 is None:
            return
        if current_level==level:

            self.lst.append(obj1.root)
            return
        else:

            self.printlevel(obj1.left,current_level-1,level)
            self.printlevel(obj1.right, current_level - 1, level)
obj1=node("10")
obj1.left=node("11")
obj1.right=node("12")
obj1.left.left=node("13")
obj1.left.right=node("14")
obj1.right.left=node("15")
obj1.right.left.right=node("17")
obj1.right.left.right.right=node("99")


#obj1.traverse(obj1)
for i in range(5,0,-1):


        obj1.printlevel(obj1,i,1)

        #del obj1.lst[:]
print(' '.join(obj1.lst))
