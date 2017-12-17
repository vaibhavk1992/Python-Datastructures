class node:
    lst=[]
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def call_counter(self,counter):
        return counter+1
    def boundary_traversal(self,root,counter):
      if root :
          if counter<3:

           x=self.call_counter(counter)
           print(type(x))
           self.boundary_traversal(root.left,x)
           self.boundary_traversal(root.right, x)
          #self.boundary_traversal(root.right,"ad")


root = node("10")
root.left=node("11")
root.left.left=node("120")
root.left.left.left=node("130")
# root.left.right=node("15")
root.right = node("12")
#root.right.left = node("13")
#root.right.right = node("14")
# root.right.right.left=node("14")
root.boundary_traversal(root,0)