'''
Create a class Employee with attributes empid,name,salary and also define methods to access
properties  of employee 

'''


class Empolyee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
    def setEmpid(self,empid):
        self.empid=empid
    def setName(self,name):
        self.name=name
    def setSalary(self,salary):
        self.salary=salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
e1=Empolyee()
e2=Empolyee(1,"Rahul",40000)
e1.setEmpid(4)
e1.setSalary(20000)
e1.setName("Akash")
print(e1.getEmpid(),e1.getName(),e1.getSalary())
print(e2.getEmpid(),e2.getName(),e2.getSalary())
