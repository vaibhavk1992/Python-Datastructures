class creatneode:
  def __init__(self,val,lst):
   self.data=val
   self.child=lst

def find_index(element):
  result.append(lst1.index(element))

def create_subset(root,lst,index,prev):
  global total_val
  if root:
   print (root.data,lst,index)
   
  if root:
   if index <len(lst): 
    if root.data+ lst[index]<total_val:  
      prev=root
      find_index(lst[index])
      root.child[index]=creatneode(root.data + lst[index],lst[index+1:])
      return create_subset(root.child[index],root.child[index].child,0,prev)
    
    elif root.data+ lst[index]==total_val:
      find_index(lst[index])
      print("Bamm we got somthing")
    
    else: 
        inc=index
        inc=inc+1
        return create_subset(root,lst,inc,prev)
    
   else:
        create_subset(prev,lst,0,prev)

  else:
    root=creatneode(0,lst)
    create_subset(root,lst,index,prev)
    return root
    
def traverse(root):
   
     print (root.child[0].child[0].child[0].data)
     #traverse(root.child
result=[]
lst=[5,10,12,13,15,18]
lst1=[5,10,12,13,15,18]
total_val=30
root=create_subset(None,lst,0,None)
print (result)
#print (root.child[0].child[0].child[0].data)

#traverse(root)