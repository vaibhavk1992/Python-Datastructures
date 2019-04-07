# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:44:35 2017

@author: vaibhav
"""
import sys
class queue:
    
    front=0
    rear=0
    list_maxsize=5
    my_list=[]
    def overflow(self):
     if self.front==self.rear:
         return True;
    def insertintolst(self,rear_element):
    
      if self.rear==self.list_maxsize:
        self.my_list=([rear_element] + self.my_list)
        self.rear=1
      elif self.rear<self.list_maxsize :
         self.my_list.insert(self.rear,rear_element)         
         self.rear=self.rear+1
      if self.overflow():
        print("queue overflowed")
        print(self.my_list)
        sys.exit()
    def printqueue(self)     :
          print(self.my_list)
          
    def delqueue(self):
        self.my_list.pop(self.front)
        self.front=self.front+1

    
A=queue();
A.insertintolst(10)
A.insertintolst(20)
A.insertintolst(30)
A.insertintolst(40)
A.insertintolst(50)
A.printqueue()
A.delqueue()
print("After deletion")
A.printqueue()
A.insertintolst(60)
A.insertintolst(70)
A.printqueue()

#A.printqueue()

#A.delqueue()
#A.printqueue()