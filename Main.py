class Evaluate:
  
  

  def _init_(self, size):

   
    self.top = -1
    self.size_of_stack = size
    self.stack = [None]*size


  def isEmpty(self):
    
    Returns:
    
    return (self.top==-1)


  def pop(self):

   
    Returns:
     
    if not self.isEmpty():

      k=self.stack[self.top]
      self.top-=1
    return k


  def push(self, operand):
   
    self.stack[self.top]=operand


  def validate_postfix_expression(self, expression):
    
    operatorcon=0
    operandcon=0
    flag=0
    for i in expression:

      if(not(i=="-" or i=="+" or i=="*" or i=="/" or i=="^")):

        k=int(i)
      if(i=="-" or i=="+" or i=="*" or i=="/" or i=="^"):

        operatorcon+=1
        flag=1
      elif(isinstance(k,int)):    
        operandcon+=1
        flag=1
      else:
        flag=0
        break
    if(flag==1 and operandcon==(operatorcon+1)):
      return True
    else:
      return False


  def evaluate_postfix_expression(self, expression):
    
    flag=0
    for i in expression:

      if(not(i=="-" or i=="+" or i=="*" or i=="/" or i=="^")):

        self.push(i)
      else:
        self.push(i)
        operator=self.pop()
        secoperator=self.pop()
        if(operator=="+"):

          self.stack[self.top]=int(self.stack[self.top])+int(secoperator)
        elif(operator=="-"):
          self.stack[self.top]=int(self.stack[self.top])-int(secoperator)
        elif(operator=="*"):
          self.stack[self.top]=int(self.stack[self.top])*int(secoperator)
        elif(operator=="/"):
          flag=1
          self.stack[self.top]=int(self.stack[self.top])/int(secoperator)
        else:
          self.stack[self.top]=int(self.stack[self.top])^int(secoperator)
    
    return int(self.stack[self.top])


# Do not change the following code
postfix_expression = input()  # Read postfix expression
tokens = postfix_expression.split()
evaluate = Evaluate(len(tokens))
if evaluate.validate_postfix_expression(tokens):
    print(evaluate.evaluate_postfix_expression(tokens))
else:
    print('Invalid postfix expression
