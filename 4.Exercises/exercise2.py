#exercise: identify if the parentheses are balanced using a stack

############
#Solution 1:
class Stack():
  
  def __init__(self):
    self.a = []
  
  def is_empty(self):
    return self.a == []
  
  def push_item(self,value):
    self.a.append(value)
  
  def pop_item(self):
    if self.is_empty():
      print('Stack is empty')
    return self.a.pop()
  
  def display(self):
    print(self.a)
  
  def balanced(self):
    print(self.is_empty())
   
x=Stack()
b=input()

for i in b:
      if i=='(':
        x.push_item('(')
       
      elif i==')':
        x.pop_item()
        
x.balanced()

###########
#Solution 2: