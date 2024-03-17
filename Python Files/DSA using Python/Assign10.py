from Assign3 import *
class Stack:
    def __init__(self) :
        self.myList=SLL()
        self.item_count=0
    def is_empty(self):
        return self.myList.is_empty()
    def push(self,data):
        self.myList.insert_at_start(data)
        self.item_count+=1
    def pop(self):
        if not self.is_empty():
         self.myList.delete_first()
         self.item_count-=1
    def peek(self):
        if not self.is_empty():
            return self.myList.start.item
    def size(self):
        return self.item_count


s=Stack()
s.push(2)
s.push(3)
s.push(6)
s.push(9)
s.push(4)
s.peek()
print('top element is : ',s.peek())
s.pop()
print('top element is : ',s.peek())


    
        
