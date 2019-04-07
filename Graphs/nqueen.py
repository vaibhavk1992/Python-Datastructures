def check_attacking_pos(i,col,pos):
  """
  To check if the queen to be placed next are in the 
  attacking positions or not
  """
  for j in pos:
    if (i-col==j[0]-j[1] or i+col==j[0]+j[1] or i ==j[0] or col==j[1]) :
      return "False"
  return "True"

def set_queen_pos(i,col,pos):
  """
  To place the queen checkig the attacking pos 
  """
  if col<=5:

   if not  pos:
     pos.append([i,col])
     check_next_queen_pos(i+1,pos) 
   
   elif  check_attacking_pos(i,col,pos)=="False":
      set_queen_pos(i,col+1,pos)

   elif  check_attacking_pos(i,col,pos)=="True":
      pos.append([i,col]) 
      
      check_next_queen_pos(i+1,pos)

  else:
     le=len(pos)
     x=pos.pop(le-1)
     set_queen_pos(x[0],x[1]+1,pos)



def check_next_queen_pos(i,pos):
  """
  To check the next queen 
  """
  if i<=5:
    col=0
    set_queen_pos(i,col,pos)
  else:
    print  pos

pos=[]
check_next_queen_pos(0,pos)

