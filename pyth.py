
class createnode:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class Unordered_list: 
  def __init__(self):
   self.head=None 
   self.last=None    
   
   
  
      
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

  def insertatbegin(self,data):
    node=createnode(data)

    if self.head==None:
      self.head=node
      self.head.next=self.head
      self.last=self.head.next
    else:
        node.next=self.last.next
        self.last.next=node
        self.last=node
        head=self.last

  def insertatpos(self,data,srchd_data):
    node=createnode(data)
    temp=self.last.next
    while(temp!=self.last):
     if(temp.data==srchd_data):
      node.next=temp.next
      temp.next=node
      break
     else: temp=temp.next
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
