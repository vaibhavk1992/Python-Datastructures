#Program for construction of full binary tree
# Python program to construct tree using inorder and
# preorder traversals
root=0
# A binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# UTILITY FUNCTIONS
# Function to find index of vaue in postorder[start...end]
# The function assumes that value is repesent in preOrder[]
def get_inorder_index(postorder,preorder_top,start,end):
    for i in range(start,end+1):
        if preorder_top==postorder[i]:
            return i

"""Recursive function to construct binary of size len from
   preorder traversal pre[] and Postorder traversal pos[].  Initial values
   of postart and poend should be 0 and len -1.  The function doesn't
   do any error checking for cases where postorder and preorder
   do not form a tree """
def construct_tree(preorder,postorder,postart,poend):
    global root
    #if preorder list exist
    if preorder:
     # Pick current node from Preorder traversal
     pre_top = preorder.pop(0)
     node=Node(pre_top)
     # Else find the index of this node in postorder traversal
     po_index = get_inorder_index(postorder, pre_top, postart, poend)

     # If this node has no children then return
     if po_index==postart or po_index<postart:
         return node
     #One time initialisation to set left and right subtree based on the succesor index in postorder
     if root==0:
         root=root+1
         succ=pre[0]
         io_index = postorder.index(succ)
         node.left= construct_tree(preorder,postorder,0,io_index)
         node.right = construct_tree(preorder, postorder,io_index+1, poend)

         return  node
     else:
         # Using index in postorder Traversal, construct left
         # and right subtrees
         node.left = construct_tree(preorder, postorder, postart, po_index-1)
         node.right = construct_tree(preorder, postorder, po_index+1, poend)

         return node

def printInorder(node):
    if node is None:
        return
    # first recur on left child
    printInorder(node.left)
    # then print the data of node
    print node.data,
    # now recur on right child
    printInorder(node.right)

# Driver program to test above function
pre= [1, 2, 4, 8, 9, 5, 3, 6, 7]
post = [8, 9, 4, 5, 2, 6, 7, 3, 1]
po_len=len(post)
root=construct_tree(pre, post,0,po_len-1)
# Let us test the build tree by priting Inorder traversal
print "Inorder traversal of the constructed tree is"
printInorder(root)


#This code is contributed by Vaibhav Kumar12