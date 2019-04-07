def make_sets(vertice):
    return set(vertice)
def  list_iterator(vertices):
    lst=[]
    for vertice in vertices:
      s=make_sets(vertice)
      lst.append(s)
    return lst
def kruskal_algo(edges,lst):
    print (lst)
    for ed in edges:
      #to assign variable as blank and if there is no match from the list then by pass the condition
        x=''
        y=''
        
  
      	for j in range(len(lst)):	
         if ed[0] in lst[j] and ed[1] in lst[j]:
          """
          Bypass the check if the edges are present in the same
          """
          pass
          """
          remove the element as soon as there is match in the list so that it can be included  in the union
          """ 
         elif ed[0] in lst[j]:
              x=lst[j]
              lst.remove(lst[j])
              break        
        for k in range(len(lst)):	
         if ed[0] in lst[k] and ed[1] in lst[k]:
          pass
         elif ed[1] in lst[k]:
              y=lst[k] 
              lst.remove(lst[k])
              break
        
        if x==y or x=='' or y=='':
              pass
        else:       
              print ed[0]+ed[1]
              lst.append(x.union(y))         
        
vertices= ['A', 'B', 'C', 'D', 'E', 'F']
lst=list_iterator(vertices)
edges=[('A','D'),('B','C'),('C','D'),('E','F'),('B','D'),('A','B'),('C','F'),('C','E'),('D','E')]
kruskal_algo(edges,lst)