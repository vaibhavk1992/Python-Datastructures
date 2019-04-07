import pandas as pd

def define_chessboard():
    df=pd.DataFrame(index=[0,1,2,3,4,5,6,7],columns=[0,1,2,3,4,5,6,7])
    for i in list(df.columns.values):
      df[i]=0
    return df

def valid_moves(move):
    lst=[]
    if (move[0]+2) in range(0,8) and (move[1]+1)in range(0,8):
       lst.append((move[0]+2,move[1]+1))

    if (move[0]+1) in range(0,8) and (move[1]+2) in range(0,8):
       lst.append((move[0]+1,move[1]+2))

    if (move[0]-1)in range(0,8) and (move[1]+2)in range(0,8):
       lst.append((move[0]-1,move[1]+2))
    
    if (move[0]-2) in range(0,8) and (move[1]+1)in range(0,8):
       lst.append((move[0]-2,move[1]+1))
    
    if (move[0]-2)in range(0,8) and (move[1]-1)in range(0,8):
       lst.append((move[0]-2,move[1]-1))
    
    if (move[0]-1)in range(0,8) and (move[1]-2)in range(0,8):
       lst.append((move[0]-1,move[1]-2))
    
    if (move[0]+1)in range(0,8) and (move[1]-2)in range(0,8):
       lst.append((move[0]+1,move[1]-2))
    
    if (move[0]+2)in range(0,8) and (move[1]-1)in range(0,8):
       lst.append((move[0]+2,move[1]-1))

    #print (lst)
    return lst

def reposition_move(df,cordinates_list):
    global counter
    flag=False
    print ("cordinates_list,",cordinates_list)
    if len(cordinates_list)>0:
    #    cordinates_list.pop(0)
        for pos in cordinates_list:	
          if df.iloc[pos[0],pos[1]]==0:
              df.iloc[pos[0],pos[1]]=counter
              #dictn[counter]=valid_moves(pos)
              #counter=counter+1
              #print("ksdkk",pos,)
              flag=True
              knight_moves(pos,df)
        if flag==False:
              counter=counter-1
              print ("counter",counter,dictn[counter][0])
		      
		      #print("counter",counter)
              reposition_move(df,dictn[counter])

    else:
        counter=counter-1
        print ("counter",counter)
        if dictn[counter]:
        	pos1=dictn[counter][0]
        	df.iloc[pos1[0],pos1[1]]=0
        #dictn[counter]=dictn[counter][1:]
        #print("counter",counter)
        reposition_move(df,dictn[counter])

def get_possible_moves(move,df):
    global counter
    global  dictn
    valid_move=valid_moves(move)
    for pos in valid_move:
      if df.iloc[pos[0],pos[1]]==0:
        dictn[counter]=valid_move[valid_move.index(pos):]
        counter=counter+1
        df.iloc[pos[0],pos[1]]=counter
        print ("~~~~~~~~~~~~~~")
        print("df,",df,dictn)
        print ("~~~~~~~~~~~~~~")
        return (pos[0],pos[1]),df
    
    return None,None

def knight_moves(move,df):
	df1=df
	#print (move)
	#print (df)
	coordinate,df=get_possible_moves(move,df)
	#print("dictn",counter,dictn)
	if coordinate:
		#print df
		#print dictn
		knight_moves(coordinate,df)
	else:
		 print("################")
		 
		 print ("dicnt",dictn)
		 print ("move",move,counter)
		 
		 df1.iloc[move[0],move[1]]=0
		 print(df1)
		 print("################")
		 dictn[counter-1]=dictn[counter-1][1:]	 
		 reposition_move(df1,dictn[counter-1])

counter=0
dictn={}
df=define_chessboard()
knight_moves((0,0),df)