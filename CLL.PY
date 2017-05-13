class createnode:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class Unordered_list: 
  def __init__(self):
   self.head=None 
   self.last=None    
   
   
  
#######INsertion at the last###      
  def createlist(self,data):
    node=createnode(data)
    if self.head==None:
      self.head=node
      self.head.next=self.head
      self.last=self.head.next
    else:
        node.next=self.last.next
        self.last.next=node
        self.last=node

#######Insetion at the begiing##
  def insertatbegin(self,data):
    node=createnode(data)

    if self.head==None:
      self.head=node
      self.head.next=self.head
      self.last=self.head.next
    else:
        node.next=self.last.next
        self.last.next=node
        head=self.last

########Insertion after a postion#####
  def insertatpos(self,data,srchd_data):
    node=createnode(data)
    temp=self.last.next
    while(temp!=self.last):
     if(temp.data==srchd_data):
      node.next=temp.next
      temp.next=node
      break
     else: temp=temp.next

########Insetion before a position####     
  def insertbfrpos(self,data,srchd_data):
    node=createnode(data)
    temp=self.last.next
    while(temp.data!=srchd_data):
            prev=temp
            temp=temp.next
    node.next=prev.next      
    prev.next=node
#########deleting the head of a node####
  def delhead(self):
   temp=self.head
   self.last.next=temp.next
   self.head=self.last.next
######Deleting the last node#####
  def dellast(self):
   temp=self.head
   while(temp!=self.last):
       prev=temp
       temp=temp.next
   prev.next=temp.next
   self.head=prev.next



#######Deleting any of the  node part2
  def delany(self,srchd_data):
   temp=self.head
   while(temp.data!=srchd_data):
     prev=temp
     temp=temp.next
   Next_to_temp=temp.next
   prev.next=Next_to_temp
   self.head=Next_to_temp

#######Reversing a lint list#####

  def reverselist(self):
   temp_last=self.last
   self.head.next=temp_last
   temp=self.head
   while(temp!=self.last):
	 prev=temp
	 next_temp=temp.next
	 next_temp.next=prev
	 temp=temp.next
   self.head=self.last
   self.head.next=self.last
######printing the list######     
  def printlist(self):
    temp=self.last.next
    while True:
     print(temp.data)
     temp=temp.next
     if temp==self.last.next:
       break;

a=Unordered_list()
a.createlist(10)
a.createlist(20)
a.createlist(30)
a.createlist(45)
a.printlist()
print("Now insert data at begining")
a.insertatbegin(60)
a.printlist()
print("insertion at some position")
a.insertatpos(70,30)
a.printlist()
print("insertion before some position")
a.insertbfrpos(80,30)
a.printlist()
print("Deletion of head")
a.delhead()
a.printlist()
print("deleting the last node ")
a.dellast()
a.printlist()
print("deleting any of the node")
a.delany(20)
a.printlist()
print("printing the list")
a.reverselist()
a.printlist()
