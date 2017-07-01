# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from itertools import product
user_inp_lst=[]    ##List for storing user input
int_conv_lst=[]    ##Int convered list
mstr_list=[]       ##Master list to store the reversed list
while True:
    try:
        total_rows=input("Enter the total number of rows by the user")
        if not total_rows:
            raise ValueError('Its an empty string')
        else :
            for i in range(int(total_rows)):
                array_inp=input("Enter the user input seprated by space")
                user_inp_lst.append(array_inp)
            for  y in user_inp_lst:
                lst = [int(i) for i in y.split()]
                int_conv_lst.append(lst)            
            for z in int_conv_lst:
                mstr_list.append(list(reversed(z)))
            a=list(zip(*mstr_list))
            for p in product(*a):
                print(p)   
            break    
    except ValueError as e:
        print(e)
   



    
