class creatneode:
  def __init__(self,val):
   self.data=val
   self.child=[]

def find_index(element):

  result.append(lst1.index(element))

def create_subset(root,lst,index):
  print(index)
  global total_val   
  if root:
   
   if index <len(lst): 
    
    while(index<len(lst))   :
      
      if root.data+ lst[index]<total_val:  
        print(root.data)
        
        result.append(lst[index])
        root.child.append(creatneode(root.data + lst[index]))
        index=index+1    
        
        create_subset(root.child[-1],lst,index)
        
      elif root.data+ lst[index]==total_val:
      #find_index(lst[index])
        #find_index(lst[index])
        result.append(lst[index])
        print(root.data)
        print(lst[index])
        index=index+1  
        print("Bamm we got somthing")
        return 
      
      else: 
        
        print("root.data",root.data) 
        inc=index
        inc=inc+1
        print ("value more tan max value")
        
        return create_subset(root,lst,inc)
        
   else:
    result.pop()
    return

  else:
    root=creatneode(0)
    create_subset(root,lst,index)
    return root
    
def traverse(root):
   
     print (root.child[0].child[0].child[0].data)
     #traverse(root.child
result=[]
lst=[5,10,12,13,15,18]
lst1=[5,10,12,13,15,18]
total_val=30
root=create_subset(None,lst,0)
print (result)

#print (root.child[0].child[0].child[0].data)

#traverse(root)