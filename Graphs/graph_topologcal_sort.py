"""
THis is done in virtual end python 3.5  an it's utput can varry
"""
import pandas as pd
def stack_elements(key,dictn,lst,df):
    while len(lst)>0:
      #To append the element to stack in recursive manner and pop the element
      if dictn[key]==False:
        dictn[key]=True
        print( key)
        extracted_df=df.loc[[key]]
        for vertex,values in extracted_df.iteritems():    
            if values[0] !=0:
              #if there is any attribute in df whose values!=0 that will be appended to stack
              lst.append(vertex)
      key=lst.pop()
      stack_elements(key,dictn,lst,df)
    return dictn

def generate_adjency_matrix(edges):
   df=pd.DataFrame(index=['0','1','2','3','4','5'],columns=['0','1','2','3','4','5'])
   for vrtcs in edges:
     df[vrtcs[1]][vrtcs[0]]=1	
   df=df.fillna(value=0)
   print df
   return df

edges=[('5','2'),('5','0'),('4','0'),('4','1'),('2','3'),('3','1')]
df=generate_adjency_matrix(edges)
lst=[]
dictn={"0":False,"1":False,"2":False,"3":False,"4":False,"5":False}
for key in sorted(dictn.iterkeys()):

    if dictn[key]==True:
      pass
    else:
    	print ("key",key)
    	lst.append(key)
    	stack_elements(key,dictn,lst,df)
