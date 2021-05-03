#this __ini__(self) is #called a method, a #constructor method, what #does it do actually?


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
  
  def peek(self):
    if self.is_empty():
      print('Stack is empty')
    return self.a[-1]
  
  def size(self):
    return len(self.a)
  
  def display(self):
    print(self.a)
  
  def balanced(self):
    if self.is_empty:
      print('The parentheses are balanced')
    else:
      print('The parentheses are not balanced')




x=Stack()
a=list(input(''))()
for i in a:
  if i!="(" or i!=")":
    
print(a)
print(type(a))


#print(x.is_empty())
#x.push_item(1)
#x.push_item(2)
#x.push_item(5)
#x.push_item(8)
#x.display()
#x.pop_item()
#x.display()
#print(x.is_empty())

#https://www.youtube.com/watch?v=z2Vs8iRMmEs