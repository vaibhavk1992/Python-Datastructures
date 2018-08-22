class creatneode:
  """
  Initialise the node
  """
  def __init__(self,val):
   self.data=val
   self.child=[]


def create_subset(root,lst,index):
  """
     Traverse the list and check if root.data+lst[idex]<target_val then append the 
     child to root
     If root.data+lst[idex]==target_val then also append it
     if root.data+lst[idex]>target_val then just increment the list  and if 
     index <len(lst) then perform the operations else return none
  """
  global total_val   
  if root:
   
   if index <len(lst): 
    
    while(index<len(lst))   :
      
      if root.data+ lst[index]<total_val: 
        root.child.append(creatneode(root.data + lst[index]))
        index=index+1    
        create_subset(root.child[-1],lst,index)
        
      elif root.data+ lst[index]==total_val:
        root.child.append(creatneode(root.data + lst[index]))
        index=index+1  
        return 
      
      else: 
        inc=index
        inc=inc+1
        return create_subset(root,lst,inc)
        
   else:
    return

  else:
    root=creatneode(0)
    create_subset(root,lst,index)
    return root

def final_result(path):
     """
     For the list whose path's sum is equal to the target value 
     """
     print([x - path[i - 1] for i, x in enumerate(path)][1:])

def traverse(node, path = []):
    """
     Traverse the complete tree
     """
    path.append(node.data)
    if len(node.child) == 0:
        if path[-1]==total_val:
          final_result(path)
        path.pop()
    else:
        for child in node.child:
            traverse(child)
        path.pop()

lst=[5,10,12,13,15,18]
total_val=30
root=create_subset(None,lst,0)
traverse(root)