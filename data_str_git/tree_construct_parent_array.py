"""we are just going to recur it to the left and right subtree based on the index we get from
 of the the run .the index we getting from parent we making it a node then searching
 the particular index s value in check index and returning the index again as node construct tree
"""
lst=[]
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def check_index(parent,data):
    flag=False
    for i in range(len(parent)):
        if parent[i]==data:
             if data in lst:
                 for i in range(len(parent)):
                     if parent[i] == data and flag== False:
                         flag=True
                         continue
                     elif parent[i] == data and flag == True:
                         return i
             else:
                 lst.append(data)
                 return i

def constructTree(parent,data):
        if parent:
            index = check_index(parent, data)
            if  index is None:
                return
            node=Node(index)
            #if node.data==0:
            #    return  node
            node.left=constructTree(parent,node.data)
            node.right = constructTree(parent, node.data)

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


parent = [-1, 0, 0, 1, 1, 3, 5]
root=constructTree(parent,-1)
printInorder(root)
