# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:34:30 2017

@author: vaibhav
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:47:22 2017

@author: vaibhav
"""

class createnode:
    def __init__(self,val):
        self.data=val
        self.next=None
class createbinarytree:
    def __init__(self,data):
        self.root=data
        self.left=None
        self.right=None
class createlist:
    def __init__(self, data = None):
        self.head = None
        self.top = None
    def push(self,val):        
        self.node=createnode(val)
        if self.head is None:
            self.head=self.node
        else:
            self.node.next=self.head
            self.head=self.node
    def convertedtree(self):
        q=[]
        if self.head is None:
            self.top = None
            return
        self.top=createbinarytree(self.head.data)
        q.append(self.top)
        self.head=self.head.next
        while(self.head):
         self.parent=q.pop(0)
         self.Leftchild=None
         self.Rightchild=None
         self.Leftchild=createbinarytree(self.head.data)
         q.append(self.Leftchild)
         self.head=self.head.next
         if(self.head ):
          self.Rightchild=createbinarytree(self.head.data)
          q.append(self.Rightchild)
          self.head=self.head.next
         self.parent.left=self.Leftchild
         self.parent.right=self.Rightchild

    def inordertraversse(self,top):
           self.m=[]
           self.parent=None
           self.m.append(top)
           while self.m:
            self.parent=self.m.pop(0)
            if self.parent is None:
               continue            
            else:                
                print(self.parent.root)
                self.m.append(self.parent.left)
                self.m.append(self.parent.right)
  
    def popqueue(self):
        
        if self.m:         
         element=self.m.pop(0)
         print("here ",element)        
         return True
        else :
         return False
            
            
    def printlist(self):
        temp=self.head
        while(temp):
          print(temp.data)
          temp=temp.next

conv=createlist();
conv.push(10)
conv.push(20)
conv.push(30)
conv.push(40)
conv.push(50)
conv.push(60)
conv.push(70)
conv.push(80)
conv.printlist()
conv.convertedtree()
print("the inorder traversal ")
conv.inordertraversse(conv.top)
