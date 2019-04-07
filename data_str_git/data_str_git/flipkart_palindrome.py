str_inp=['a','b','b','','a']
for i in range(0,len(str_inp),1):
  for j in range(len(str_inp)-i-1,0,-1):
   if i < j:
    print("i",i)
    print("j",j)
    if str_inp[i]==str_inp[j]:

        break
    else:
        print("the number is not palindrome")
        exit()
   else:
       break
print("the numbe is palidrome")