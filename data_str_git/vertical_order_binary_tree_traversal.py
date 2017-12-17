"""is for root,-1 for left of root,+1 for right of root.collect those values for each node and make hashmap
"""
class node:
    dict1={}
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def check_if_exists(self,hd,root):
      if not self.dict1:
          self.dict1[hd] = [root.data]
      else:
            if hd in self.dict1.keys():
                self.dict1[hd].append(root.data)
            else:
                self.dict1[hd] = [root.data]

    def vertical_order_tree(self,root,hd):
        if root:
                self.check_if_exists(hd,root)
                self.vertical_order_tree(root.left,hd-1)
                self.vertical_order_tree(root.right,hd+1)


root=node("10")
root.left=node("11")
root.left.left=node("12")
root.left.right=node("15")
root.right=node("12")
root.right.left=node("13")
root.right.right=node("14")
root.right.right.left=node("14")
root.vertical_order_tree(root,0)
#print(root.dict1)
for k,v in sorted(root.dict1.items()):
   str=''
   int_list=map(int,v)
   for i in range(len(int_list)):
      str+=`int_list[i]` +' '
   print(str)
