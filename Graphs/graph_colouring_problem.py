graph = { 1 : [2,3,4],
          2 : [1,3],
          3 : [1,2,4],
          4 : [1,3]}

graph_colours=['red','orange','blue','yellow']
final_lst={}

"""
Substract the list of already present colours on the vertices with the colours list
"""
def assign_colours(temp_array):
  final_colourslist = list(set(graph_colours) - set(temp_array))
  return final_colourslist[0]


"""
For each vertices check the adjacent neighbours and if neighbours havecolours assign it to a temp array
"""
for key,value in  graph.items():
  temp_array=[]
  for vertices in value:
    if vertices in final_lst.keys():
        temp_array.append(final_lst[vertices])
  color=assign_colours(temp_array)

  final_lst[key]=color
print(final_lst)

