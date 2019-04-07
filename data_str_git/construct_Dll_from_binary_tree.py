head=None
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class ll_node:
    def __init__(self, key1):
        self.data = key1
        self.next = None
        self.prev = None
        
def traverse(root):
  if root:
    traverse(root.left)
    #print(root.data)
    node=ll_node(root.data)
    #print(node.prev)
    construct_dll(node)
    traverse(root.right)

def construct_dll(node):
  global head
  if not head:
    head=node
  else:
    temp=head
    while(temp.next):
      temp=temp.next
    temp.next=node
    node.prev=temp
    #print(node.prev)
    
def traverse_dll() :  
   temp=head
   while(temp):
     #print("the prev",temp.prev.data)
     print(temp.data)
     temp=temp.next

root=Node(10)
root.left=Node(12)
root.right=Node(15)
root.left.left=Node(25)
root.left.right=Node(30)
root.right.left=Node(36)
traverse(root)
traverse_dll()
