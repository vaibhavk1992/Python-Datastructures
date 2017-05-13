class createnode:
  def __init__(self,data):
      self.data=data
      self.next=None
      self.prev=None

class Unordered_list: 
  def __init__(self):
   self.head=None 
######Insertion at the starting###
  def buildlst(self,data):
    node=createnode(data)
    if self.head is None:
     self.head=node
    else:
     node.next=self.head
     self.head.prev = node
     self.head=node
#######INsertion at the end####
  def buildlstend(self,data):
    node=createnode(data)
    ptr=self.head
    while(ptr.next):
      ptr=ptr.next
    ptr.next=node
    ptr=node.prev



#######INsertion before some node i.e searched node####
  def buildlstpos(self,data,srch_data):
    node=createnode(data)
    ptr=self.head
    while ptr:

                if ptr.data == srch_data:
                    node.prev = ptr.prev
                    node.next = ptr
                    ptr.prev = node
                    node.prev.next = node
                    break  
                else:
                    ptr = ptr.next
#######INsertion at after some node i.e searched node####
  def buildaftrpos(self,data,srch_data):
    node=createnode(data)
    ptr=self.head
    while(ptr):
      if ptr.data==srch_data:
            
            node.next=ptr.next
            ptr.next=node
            node.prev=ptr
            node.next.prev = node  # <--
            break 
      ptr=ptr.next 

##########Deleting the head#########
  def deletehead(self):
   ptr=self.head
   ptr=ptr.next
   ptr.prev=None
   self.head=ptr

##########Deleting the tail#########
  def deletetail(self):
   ptr=self.head
   while ptr.next is not None:
       prev=ptr
       ptr=ptr.next
   prev.next=None
##########Deleting the middle node#########
  def deleteposnode(self,data):
   ptr=self.head
   while ptr:
       if ptr.data==data:
          
          ptr.prev.next=ptr.next
          ptr.next.prev=ptr.prev
          break
       else: 
 
          ptr=ptr.next
########Reversing the list########      
  def Reverselist(self):   
    ptr=self.head
    prev_node=None
    while(ptr):
     next_node=ptr.next
     ptr.next=prev_node
     ptr.prev=next_node
     prev_node=ptr
     ptr=next_node
    self.head=prev_node
########Printitng the list########      
  def printlist(self):
     temp=self.head      
     while(temp):
      print(temp.data)
      temp=temp.next 	
         
A=Unordered_list()
A.buildlst(10)
A.buildlst(20)
A.buildlstend(30)
A.printlist()
A.buildaftrpos(40,20)
print("after the insetion at the start")
A.printlist()
print("before the position built")
A.buildlstpos(50,10)
A.buildlstpos(60,50)
A.printlist()
print("deletion of head")
A.deletehead()
A.printlist()
print("deletion of tail")
A.deletetail()
A.printlist()
print("deletion of a particular node")
A.deleteposnode(50)
print("the final list")
A.printlist()
print("the reverse of the list")
A.Reverselist()
A.printlist()
