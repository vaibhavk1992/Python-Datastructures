import pandas as pd
result=[]
def minimum_spanning_tree(dictn,df,result,vertex_edge_lst):

    
    #while (len(dictn)>0)
    if len(dictn)>0:

       min_dict_element=min(dictn, key=dictn.get)

       df1=df.loc[[min_dict_element]]
       #print df1
       
       for name,values in df1.iteritems():       
           if values[0] !=0:
              #print dictn[name]
              #print name
              #print df1.loc[min_dict_element][name]
             if name in dictn.keys():
              if df1.loc[min_dict_element][name]<dictn[name]:
                  dictn[name]=values[0]
                  
                  vertex_edge_lst[name]=min_dict_element+name
    
                  #print vertex_edge_lst
                  
                     
             if min_dict_element in dictn.keys():
                  del dictn[min_dict_element]

       if min_dict_element in vertex_edge_lst.keys():
                     result.append(vertex_edge_lst[min_dict_element])
                     
       #print (min_dict_element)
       #print (dictn)
       #print(vertex_edge_lst)
       print result
       minimum_spanning_tree(dictn,df,result,vertex_edge_lst)
    else:
       print  result
def generate_adjency_matrix(lst):
   df=pd.DataFrame(index=['a','b','c','d','e','f'],columns=['a','b','c','d','e','f'])
   for edges in lst:
     df[edges[0]][edges[1]]=edges[2]
   df=df.fillna(value=0)
   return df
lst=[('a','d',1),('a','b',3),('d','a',1),('d','b',3),('d','c',1),('d','e',6),('e','d',6),('e','c',5),('e','f',2),('f','e',2),('f','c',4),('c','d',1),('c','f',4),('c','e',5),('c','b',1),('b','a',3),('b','d',3),('b','c',1)]
df=generate_adjency_matrix(lst)
inf_val = float("inf")
dictn={'a':0,'b':inf_val,'c':inf_val,'d':inf_val,'e':inf_val,'f':inf_val}

vertex_edge_lst={}
minimum_spanning_tree(dictn,df,result,vertex_edge_lst)

