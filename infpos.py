###########Program for INFIX TO Postfix#####
import string
class infixtopostfix:
  postfix_array=[]  
  stack_array=[]
  def push_pstfx(self,val): 
   self.postfix_array.append(val)

  def push_stack(self,val3): 
   self.stack_array.append(val3)

  def printarray(self):
   print("the postfix array is ",self.postfix_array)
   print("the stack  array is ",self.stack_array)

  def check_precedence(self,val3): 
      len_push_stack=len(self.stack_array)-1
      for len_push_stack in range (len_push_stack,-1,-1):

        if((self.stack_array[len_push_stack]=='^' and (val3=='+' or val3=='-' or val3=='*' or val3=='/')) or 
         (self.stack_array[len_push_stack]=='*' and (val3=='+' or val3=='-' or val3=='*' or val3=='/'))or
         (self.stack_array[len_push_stack]=='/' and (val3=='+' or val3=='-' or val3=='*' or val3=='/'))or
         (self.stack_array[len_push_stack]=='+' and (val3=='+' or val3=='-' ))or
         (self.stack_array[len_push_stack]=='-' and (val3=='+' or val3=='-' ))
         ):
          var5=self.stack_array[len_push_stack]
          self.push_pstfx(var5)
          self.stack_array.pop()
          if len_push_stack==0 :
            self.push_stack(val3)             
          else :
             continue
       
        
        else:
          self.push_stack(val3)
          break;

  def pop_to_left_brace(self):
    pop_brace_stack_len=len(self.stack_array)-1
    while self.stack_array[pop_brace_stack_len]!='(':
      var7=self.stack_array[pop_brace_stack_len]
      self.push_pstfx(var7)
      self.stack_array.pop()
      pop_brace_stack_len=pop_brace_stack_len-1
    self.stack_array.pop()

  def getexpression(self,user_input):
   spltd_exp=list(user_input)
   spltd_exp_len=len(spltd_exp)
   lc_list=list(string.ascii_lowercase)
   uc_list=list(string.ascii_uppercase )
   num_list=list(string.digits )
   lc_list_len=len(lc_list)
   uc_list_len=len(uc_list)
   num_list_len=len(num_list)
   oprtr_list=['+','-','/','^','*']
   oprtr_list_len=len(oprtr_list)

   for i in range(0,spltd_exp_len,1):
    for j in range(0,lc_list_len,1):
      if spltd_exp[i]==lc_list[j] :
        val1=spltd_exp[i]
        self.push_pstfx(val1)

    for k in range(0,uc_list_len,1):
      if  spltd_exp[i]==uc_list[k]: 
          val2=spltd_exp[i]  
          self.push_pstfx(val2)

    for q in range(0,num_list_len,1):
      if  spltd_exp[i]==num_list[q]: 
          val9=spltd_exp[i]  
          self.push_pstfx(val9)

    for l in range(0,oprtr_list_len,1):
      if  spltd_exp[i]==oprtr_list[l]:
          val3=spltd_exp[i]  
          if not self.stack_array:
            self.push_stack(val3) 
          else :
            self.check_precedence(val3)
      elif spltd_exp[i]=='(':
            self.push_stack('(')
      elif spltd_exp[i]==')': 
            self.pop_to_left_brace()

   final_len_stack_arr=len(self.stack_array)-1
   for final_len_stack_arr in range (final_len_stack_arr,-1,-1):
    var6=self.stack_array[final_len_stack_arr]
    self.push_pstfx(var6)
    self.stack_array.pop() 
 
A=infixtopostfix()
user_input=input("Enter the expression",)
A.getexpression(user_input)
A.printarray()

