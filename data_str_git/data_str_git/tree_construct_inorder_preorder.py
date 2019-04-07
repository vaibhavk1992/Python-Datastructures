class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_inorder_index(inorder,preorder_top,base_index,end_index):

    for i in range(base_index,end_index+1):
        if preorder_top==inorder[i]:

            return i


def construct_tree(preorder, inorder,base_index,end_index):
    print(base_index,end_index)
    if preorder:
     preorder_top = preorder.pop(0)
     preorder_node = Node(preorder_top)

     if base_index==end_index:
        return preorder_node

     inorder_index=get_inorder_index(inorder,preorder_top,base_index,end_index)

     preorder_node.left=construct_tree(preorder,inorder,base_index,inorder_index-1)

     preorder_node.right = construct_tree(preorder, inorder, inorder_index+1, end_index)
     print(inorder_index)
     return preorder_node


def printInorder(node):
    if node is None:
        return

    # first recur on left child
    printInorder(node.left)

    # then print the data of node
    print node.data,

    # now recur on right child
    printInorder(node.right)


inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
ino_len=len(inorder)
node=construct_tree(preorder, inorder,0,ino_len-1)
printInorder(node)