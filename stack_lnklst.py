
class createnode:
  def __init__(self,data):
      self.data=data
      self.next=None
  
class Unordered_list:

  def __init__(self):
   self.top=None 

  def createstack(self,data):
    node=createnode(data)
    if self.top is None:
       self.top=node
    else :
        node.next=self.top
        self.top=node

  def printstack(self) :
    temp=self.top
    while(temp!=None):
     print(temp.data)
     temp=temp.next
  
  def popstack(self):
   temp=self.top
       
   while(temp!=None):
    if(temp==self.top):
      temp=temp.next
      break;
   self.top=temp
 

class stackusingarray():
  def __init__(self,maxsize=5):
   self.list1=[]
   self.maxsize=maxsize
  
  def isfull(self):
   if len(self.list1)==self.maxsize:
     print("Stack Overflow") 
     return True
   else : 
     return False

  def isEmpty(b):
   if len(b.list)==0:
     print("Stack is empty") 
     return True
   else : 
     return False

  def push(self,data):
   if not self.isfull():
    self.list1.append(data)
    print("Appended data :" ,data)
########Pop using normal funcion#    
  def pop(self):     
    return self.list1.pop()

######Pop using reducing the lenght of list####
  def popwithdefination(self):
   for i  in range(len(self.list1)-1):
     print(self.list1[i])
######Reverse a string using stack#####
  def reversestack(self,strng):
   b=list(strng)
   strlen=len(strng)
   var2=""
   for i in range(0,strlen,1):
    var2+=b.pop()
   print(var2)

########Passing an expression#######
  def reverseexpr(self,A):
    splt=list(A)
    empty_list=[]
    strlen=len(splt)
    for i in range(0,strlen,1):
       if (splt[i] == "(" or splt[i]== "["  or splt[i]== "{"):
        empty_list.append(splt[i])
        print(empty_list)
       elif  splt[i]==")"  or splt[i]== "]" or splt[i]== "}":
         scnd_len=len(empty_list)
         print(scnd_len)
         if  scnd_len>0:
          last_scand_element=empty_list.pop() 
         else :
           break
         print(last_scand_element)
         if((last_scand_element=="(" and splt[i]==")") or(last_scand_element=="[" and splt[i]=="]") or(last_scand_element=="{" and splt[i]=="}")):
           continue;
         else:
           print("List is invalid");
           exit();
    if not empty_list and scnd_len>0:
      print("list is valid ")
    else :
      print("List is invalid")
       
a=Unordered_list()
b=stackusingarray()
b.push(30)
b.push(40)
b.push(40)
b.push(40)
b.popwithdefination()
c=b.pop()
print("the last popped out item is ")
strng=raw_input("enter the string you want to reverse:")
b.reversestack(strng)
A="[A+B-{C%D}]"
b.reverseexpr(A)
#a.createstack(20)
#a.createstack(30)
#a.createstack(40)
#a.printstack()
#print("Let's PopOut")
#a.popstack()
#a.printstack()
#print("stack using array")
#a.createarrstack()
#print("pop using array")
#A.poparrstack()
