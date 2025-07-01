""" a=input("enter the value a:")
def divs(a):
    if a % 2 ==0:
        return "even"
    else:
        return "odd"
 """
class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
           self.values = [x] + self.values
    def pop(self):
           return self.values.pop(0)
    def pop_value(self, x):
        if x in self.values:
            self.values.remove(x)
            return f"{x} removed from stack"
        else:
            return f"{x} not found in stack"
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.values)
print("Stack before:", s.values)
print(s.pop_value(20))  
print("Stack after:", s.values)
