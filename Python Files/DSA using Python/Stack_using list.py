class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peak (self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
s1=Stack()
# s1.push(10)
# s1.push(13)
# s1.push(15)
# s1.push(11)
print("top element is " ,s1.peak())
# print("removed element : ",s1.pop())
# print("top element is " ,s1.peak())



                  
        