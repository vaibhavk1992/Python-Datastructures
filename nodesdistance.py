# Python Program to find distance between
# n1 and n2 using one traversal

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def findancesstor(root,val1,val2):
   if root:
      if root.data==val1 or root.data==val2:
         return True
      leftbool = findancesstor(root.left, val1, val2)
      rightbool = findancesstor(root.right, val1, val2)
      if leftbool  and rightbool :
         return root
      if leftbool  and not rightbool :
         return root.left
      if not leftbool  and rightbool :
         return root.right
      if not leftbool and not rightbool:
         return False
   else:return

def computedistance(root,n1,n2,counter):
	if root:
		if root.data == n1  or root.data==n2:
			return counter
		leftval=computedistance(root.left,n1,n2,counter+1)
		rightval=computedistance(root.right, n1, n2, counter+1)
		if not leftval and  rightval:
			return  rightval
		if leftval and rightval:
			return  leftval+rightval
		if leftval and not rightval:
			return leftval
	else:
			return

# Driver Code to test above functions
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
#root.right.left.right = Node(8)

n1=4
n2=3
common_node=findancesstor(root,n1,n2)
distance=computedistance(common_node,n1,n2,0)
print("the distance betweeen the two node is ",distance)

#dist = distance(root, 2, 5)

