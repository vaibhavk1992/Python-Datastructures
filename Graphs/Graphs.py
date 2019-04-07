import pandas as pd
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
lst=[]
vrtcs=[]
def generate_edges(graph,start,end):
  for k in graph:
    for i in range(len(graph[k])):
       	elmnt=(k,graph[k][i])
        lst.append(elmnt)  
  
  return lst
def generate_vertices(lst):
	for l in range(len(lst)):
		for m in range(len(lst[l])):
		  if lst[l][m] not  in vrtcs:
		     vrtcs.append(lst[l][m])
	return vrtcs


def generate_adjency_numeric_index_matrix(lst):
   df=pd.DataFrame(index=['0','1','2','3'],columns=['0','1','2','3'])
   for edges in lst:
      df[edges[0]][edges[1]]="1"
   df=df.fillna(value="0")
   return df
def generate_adjency_matrix(lst):
   df=pd.DataFrame(index=['a','b','c','d','e','f'],columns=['a','b','c','d','e','f'])
   for edges in lst:
      df[edges[0]][edges[1]]="1"
   df=df.fillna(value="0")
   return df
def generate_adjency_list(lst):
   mydict={}
   for edges in lst:
    if edges[0] in mydict.keys():
      mydict[edges[0]].append(edges[1])  
    else:
      mydict[edges[0]]=[]
      mydict[edges[0]].append(edges[1])  
   return mydict

def generate_bfs(lst,start_elmnt):
   q=[]

   df=generate_adjency_matrix(lst)
   print df
   q.append(start_elmnt)
   while(len(q)>0):
     val=q.pop(0)
     if not df[df[val].str.contains("1")].empty:
       print(val)
     df[val]="0"
     df1=df.loc[[val]]
     for name, values in df1.iteritems():
      if values[0] =="1":
        q.append(name)   
     
def generate_dfs(lst,start_elmnt):
   q=[]
   q.append(start_elmnt)
   while(len(q)>0):
     val=q.pop(len(q)-1)
     if not df[df[val].str.contains("1")].empty:
       print(val)
     df[val]="0"
     df1=df.loc[[val]]
     for name, values in df1.iteritems():
      if values[0] =="1":
        generate_dfs(lst,name)  
     
   
lst=generate_edges(graph,'a','c')

print (generate_vertices(lst))
print ("adjency matrix")
print generate_adjency_matrix(lst)
print ("adjency list")
print generate_adjency_list(lst)
print ("the breadth first traversal of the graph is ")

generate_bfs(lst,"a")
lst=[('1', '0'),('2', '0'), ('2', '1'), ('0', '2'),('3', '2'),('3', '3')]
df=generate_adjency_numeric_index_matrix(lst)
generate_dfs(df,"2")