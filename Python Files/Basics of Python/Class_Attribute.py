# class Test:
#     x=10
#     def f1():
#         m1=4
#     def __init__(self,a):
#         self.a=a
# t1=Test()
# t2=Test()



#All variable names in above code

"""
x,m1,a,t1.a,t2.a,t1,t2,f1,__init__,Test,self
x----  class object variable
m1 ---- local variable
a -----local variable
t1.a ------Instance Object Variable
t2.a ------Instance Object Variable
t1  ------global variable
t2  ------global variable
self  ------local variable
test------ global variable
f1 -----variable to represent function Object
__init__variable to represent function object
"""


class  Test:
    x1=9   # class object variable (static variable)
    def  f1(self):#instance method
        self.a=10
        Test.x2=7 
    @staticmethod
    def f2():
        print("hello")
    @classmethod
    def f3(cls):
        cls.x=5
        Test.x=12
        
def f4():
    print("non member function ")

t1=Test()
t1.b=11
t1.f1()  #f1(t1)
Test.x4=13
Test.f2()  #f2()
Test.f3()  #f3(Test)


#Class Object Variable (class object .static variable)