class node:
    lst=[]
    str1=''
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None

    def traverse(self,obj1):
        if obj1 :
            print(obj1.root)
            if obj1.left:
                self.lst.append(obj1.left)
            self.traverse(obj1.right)

    def wh(self,obj1):

         self.lst=[]
         self.lst.append(obj1)
         self.lst.append(None)
         while(len(self.lst)>0):
             pop_node=self.lst.pop(0)
             if (pop_node==None):
                 self.lst.append(None)
                 pop_node = self.lst.pop(0)
                 if (pop_node == None):
                     break
             self.traverse(pop_node)

obj1=node("10")
obj1.left=node("11")
obj1.right=node("12")
obj1.left.left=node("13")
obj1.left.right=node("14")
obj1.right.left=node("15")
obj1.right.left.right=node("17")
obj1.right.left.right.right=node("99")
obj1.traverse(obj1)
obj1.wh(obj1)

