
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def constructTree(pre,preLN,i_val):
     if pre:
        node_data= pre.pop(0)
        node=Node(node_data)
        #print(node.data)
        #print preLN[i_val]
        if preLN[i_val] <>'L':
            node.left=constructTree(pre,preLN,i_val+1)
            node.right = constructTree(pre, preLN, i_val + 2)
            #print node
        return node
            #node.right = constructTree(pre, preLN[i + 1])
def printInorder(node):
    if node is None:

        return
    # first recur on left child
    printInorder(node.left)
    # then print the data of node
    print node.data,
    # now recur on right child
    printInorder(node.right)


pre = [10, 30, 20, 5, 15]
preLN= ['N', 'N', 'L', 'L', 'L']
root=constructTree(pre,preLN,0)

printInorder(root)