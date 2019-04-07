lst=[]
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.data=key
        self.left = None
        self.right = None
        self.isthread=False
    def inorder_traverse(self,root):
        if root:
            self.inorder_traverse(root.left)
            lst.append(root)
            self.inorder_traverse(root.right)
    def construct_tree(self,root):

        if root.left :
            self.construct_tree(root.left)
        if root.right:
            self.construct_tree(root.right)

        else:
            
            lst.pop(0)
            if len(lst)>0:

                root.right=lst.pop(0)
                root.isthread=True
                
        
    def inorder_traverse1(self,root):
       curr=root
       while(curr.left):
           curr=curr.left
       while(curr):
           print (curr.data)
           if curr.isthread==True:
               curr=curr.right
           else:
              if curr.right:
               curr=curr.right
               if curr.left:
                 while(curr.left):
                  curr=curr.left  
               else:
                  continue
                 
              else:
                break

root  = Node(10);
root.left  = Node(8);
root.left.left   = Node(3);
root.right  = Node(2);

root.left.right  = Node(5);

"""
root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.left.left = Node(4);
root.left.right = Node(5);
root.right.left = Node(6);
root.right.right = Node(7);
"""
root.inorder_traverse(root)

root.construct_tree(root)
print ("after traversal")


root.inorder_traverse1(root)
