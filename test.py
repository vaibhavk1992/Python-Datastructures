# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:47:22 2017

@author: vaibhav
"""

class createnode:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
    
class createbinarytree:

    def array(self):
        self.q=[]
        self.num=int(raw_input("enter the number of element you want in the list"))
        for i in range(0,self.num):   
          self.num1=int(raw_input("enter the " + `i+1` +"element"))
          self.q.append(self.num1)
    
    def createtree(self):
        self.l=[1,2,3,4,5]
        z=[]
        arr_len=len(self.l)
        k=0
        root_data=self.l[0]
        self.top=createnode(root_data)
        z.append(self.top)
        
        while(k<arr_len):
        
           self.parent=z.pop(0)
           self.x=int(2) * int(k)+int(1)
           if(self.x>=arr_len):
             break;  
           left_data=self.l[self.x]
           self.left_child=createnode(left_data)
           z.append(self.left_child)
           self.y=int(2) * int(k)+int(2)
           if(self.y>=arr_len):
             break;  
           right_data=self.l[self.y]
           self.right_child=createnode(right_data)
           z.append(self.left_child)
           self.parent.left=self.left_child
           self.parent.right=self.right_child         
           
           k=k+1
    def inordertraversse(self,top):
           if(top):
            self.inordertraversse(top.left)
            print(top.root)
            self.inordertraversse(top.right)
            
    def preordertraversse(self,top):
           if(top):
            print(top.root)       
            self.preordertraversse(top.left)
            self.preordertraversse(top.right)
    def postordertraversse(self,top):
           if(top):
            self.postordertraversse(top.left)
            self.postordertraversse(top.right)            
            print(top.root)
            

        

conv=createbinarytree();
#conv.array()
conv.createtree()
print("the inorder traversal is ")
conv.inordertraversse(conv.top)
print("the preorder traversal is ")
conv.preordertraversse(conv.top)
print("the postorder traversal is ")
conv.postordertraversse(conv.top)


