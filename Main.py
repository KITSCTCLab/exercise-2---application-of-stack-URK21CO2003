class Evaluate:
  
  """This class validates and evaluate postfix expression.
  Attributes:
      top: An integer which denotes the index of the element at the top of the stack currently.
      size_of_stack: An integer which represents the size of stack.
      stack: A List which acts as a Stack.
  """
    # Write your code here
    

  def _init_(self, size):

    """Inits Evaluate with top, size_of_stack and stack.
    Arguments:
      size_of_stack: An integer to set the size of stack.
    """
    self.top = -1
    self.size_of_stack = size
    self.stack = [None]*size


  def isEmpty(self):
    """
    Check whether the stack is empty.
    Returns:
      True if it is empty, else returns False.
    """
    return (self.top==-1)


  def pop(self):

    """
    Do pop operation if the stack is not empty.
    Returns:
      The data which is popped out if the stack is not empty.
    """
    if not self.isEmpty():

      k=self.stack[self.top]
      self.top-=1
    return k


  def push(self, operand):
    """
    Push the operand to stack if the stack is not full.
    Arguments:
      operand: The operand to be pushed.
    """
    self.top+=1
    self.stack[self.top]=operand


  def validate_postfix_expression(self, expression):
    """
    Check whether the expression is a valid postfix expression.
    Arguments:
      expression: A String which represents the expression to be validated.
    Returns:
      True if the expression is valid, else returns False.
    """
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
    """
    Evaluate the postfix expression
    Arguments:
      expression: A String which represents the the expression to be evaluated
    Returns:
      The result of evaluated postfix expression.
    """
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
    print('Invalid postfix expression')
