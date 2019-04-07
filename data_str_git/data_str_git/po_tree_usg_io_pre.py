class buildtree:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
    def traverse(self,obj1):
      if  obj1:
          print(obj1.root)
          self.traverse(obj1.left)
          self.traverse(obj1.right)

#    def buildtree1(self,obj1,obj2,obj3):
 #       self.root=obj1
  #      self.root.left=obj2
   #     self.root.right=obj3
    def build_postorder(self,obj1):
        io_lst=['D','B','E','A','F','C']
        pre_lst = ['A', 'B', 'D', 'E', 'C', 'F']
        for i in range(len(pre_lst)):
            self.buildtree1(pre_lst[i],''.join([''.join(io_lst[i]) for i in range(io_lst.index('A'))]),''.join([''.join(io_lst[i]) for i in range(io_lst.index('A')+1,len(io_lst))]))
            break
obj1=buildtree()
#obj1.left=buildtree(20)
#obj1.right=buildtree(30)
#obj1.traverse(obj1)
obj1.build_postorder(obj1)
obj1.traverse(obj1)