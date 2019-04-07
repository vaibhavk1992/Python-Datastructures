
"""
import random
my_list = [0,1,2,3,4,5] * 10  + [6,7,8,9,10] * 90
for i in range(10):

 print(random.choice(my_list))


"""


a=1
b=2
m=10
x=3
lst=[]
for i in range(10):
  x=(a*x+b)%m
  lst.append(x)
print(lst)
if len(lst) != len(set(lst)):
    print("it has duplicates but possibly random numbers")
else:
    print("those were random numbers")
