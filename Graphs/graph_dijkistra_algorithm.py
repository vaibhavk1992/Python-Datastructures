import pandas as pd


def minimum_spanning_tree(original_dict, df, vertex_distance_lst):
    if len(original_dict) > 0:
       min_dict_key=min(original_dict, key=original_dict.get)
       min_dict_value=original_dict[min_dict_key]
       extracted_df=df.loc[[min_dict_key]]
       for vertex,values in extracted_df.iteritems():       
           if values[0] !=0:
             if vertex in original_dict.keys():
              if extracted_df.loc[min_dict_key][vertex]+min_dict_value<original_dict[vertex]:
                  original_dict[vertex]=values[0]+min_dict_value    
             if min_dict_key in original_dict.keys():
                  vertex_distance_lst[ min_dict_key]=min_dict_value
                  del original_dict[min_dict_key]
       minimum_spanning_tree(original_dict,df,vertex_distance_lst)
    else:
       print(vertex_distance_lst)
def generate_adjency_matrix(lst):
   df=pd.DataFrame(index=['a','b','c','d','e','f'],columns=['a','b','c','d','e','f'])
   for edges in lst:
     df[edges[0]][edges[1]]=edges[2]
   df=df.fillna(value=0)
   return df
lst=[('a','d',9),('a','b',5),('a','e',2),('d','a',9),('b','a',5),('e','a',2),('b','c',2),('c','b',2),('c','d',3),('d','c',3),('d','f',2),('f','e',3),('f','d',2)]
df=generate_adjency_matrix(lst)
inf_val = float("inf")
original_dict={'a':0,'b':inf_val,'c':inf_val,'d':inf_val,'e':inf_val,'f':inf_val}
vertex_distance_lst={}
minimum_spanning_tree(original_dict,df,vertex_distance_lst)