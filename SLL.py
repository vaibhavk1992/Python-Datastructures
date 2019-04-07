class Node:

 def __init__(self,data):

    self.data=data

    self.next=None

class Init:

 def __init__(self):

  self.head=None

#######Inseertion at beg##############

 def Insertatbegnode(self,data):

  temp=Node(data)

  if self.head is None :

     self.head=temp

  else :

     temp1=self.head

     temp.next=temp1

     self.head=temp

#######Inseertion at end ##############   

 def Insertatendnode(self,data):

    temp=Node(data)

    if self.head is None :

     self.head=temp

    else :

     temp1=self.head

     while(temp1.next):

        temp1=temp1.next

     temp1.next=temp

#######Searching ##############   

 def checknode(self,data):
    temp=self.head
    if self.head is None:
     print("list is empty")
    else :
     while(temp):
        if temp.data==data:
          print("it is present")
          break
        
        temp=temp.next
#######Inseertion at Mid ##############   

 def Insertatmidnode(self,data,var11):
    
    check_mid=1

    temp=self.head

    if var11 % 2==0:

      mid=var11/2

    else:

      mid=(var11+1)/2
      
    while(temp):
      
      if check_mid == mid:
         temp1=Node(data)
         temp2=temp.next
         temp.next=temp1
         temp1.next=temp2

      check_mid=check_mid+1

      temp=temp.next
#######Printing the list##############    

 def  Printlist(self):

   temp1=self.head

   while(temp1):

       print(temp1.data)

       temp1=temp1.next

      

########Checking  the count###########

 def Checkcount(self):

   

    temp=self.head

    count=0

    while(temp.next):

      count=count+1

      temp=temp.next

    return count

##########NOde Swap####################


 def swapnodes(self,first1,second1):
  
     first=self.head

     second=self.head
     first_var_cap=None
     second_var_cap=None
     while(first.data!=first1):

         first_var_cap=first
         
         first=first.next
     
     while(second.data!=second1):

         second_var_cap=second
         
         second=second.next

 
    
     if first_var_cap is None:
       self.head=second
       
     else:
        first_var_cap.next=second
     
     if second_var_cap is None:
       self.head=first
       
     else:
        second_var_cap.next=first

      
     temp=first.next
     first.next=second.next
     second.next=temp
############Reversing a link list######

 def reverselst(self):
  ptr=self.head
  prev=None
  while(ptr):
   next=ptr.next
   ptr.next=prev
   prev=ptr
   ptr=next

  print("it only print once")
  self.head=prev
  
############Deletion of a specific a link list######

 def nodedeletion(self,data):
  ptr=self.head

  while(ptr):
   if ptr.data ==data:
      ptr=ptr.next
   else :
     print(ptr.data)
     prev=ptr
     ptr=ptr.next
     

############Deletion of first node######

 def nodedeletionatstart(self):
  ptr=self.head

  while(ptr.next is not None):
   ptr=ptr.next
   print(ptr.data)

############Deletion of last node######

 def nodedeletionatlast(self):
  ptr=self.head

  while(ptr.next ):
   print(ptr.data)
   ptr=ptr.next
   
    


A=Init();

A.Insertatbegnode(10);

A.Insertatbegnode(20);

A.Insertatbegnode(30);

A.Insertatbegnode(40);

A.Insertatendnode(50);

A.Insertatendnode(60);

var11=A.Checkcount();

A.Insertatmidnode(70,var11);
A.Printlist();
#A.checknode(70);
print("here i'm going to swap the nodess")
#A.swapnodes(20,70)
print("here i'm going to sreverse list")
A.reverselst();
A.Printlist();
print("delte the nodes at a position")
A.nodedeletion(30)
print(" delete the nodes at the start")
A.nodedeletionatstart()
print("delete the node at end ")
A.nodedeletionatlast();

 

