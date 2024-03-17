class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
         return super.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    def insert(self,index,data):
        raise AttributeError("no attribute 'insert, in stack")
s1=Stack()
# s1.insert(0,10)
s1.push(23)
s1.push(76)
s1.push(17)
s1.push(49)
print("top values = ",s1.peek())

        
        