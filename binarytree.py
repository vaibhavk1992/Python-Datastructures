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
        if(top):
            self.inordertraversse(top.left)
            print(top.root)
            self.inordertraversse(top.right)
            
          
    def test(self):
      print(self.top.root)          
      print(self.top.left)          
      print(self.top.right)          
    def printlist(self):
        temp=self.head
        while(temp):
          print(temp.data)
          temp=temp.next

conv=createlist();
conv.push(10)
conv.push(20)
conv.push(30)
conv.printlist()
conv.convertedtree()
#conv.printlist()
print("the test starts from her")
#conv.test()
conv.inordertraversse(conv.top)
