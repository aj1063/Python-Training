l = 2.3
list = [12,13,45,65]
dis = {'S':'Sunday','M':'Monday','T':'Tuesday'}

class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.1415*self.radius*self.radius
    def perimeter(self):
        return 2*self.radius*3.1415
    def daimeter(self):
        return 2*self.radius

class Rectangle:
    def __init__(self,l,b):
        self.length=l
        self.breath=b
    def area(self):
        return self.length*self.breath
    def perimeter(self):
        return 2*(self.length+self.breath)
    def is_square(self):
        return self.length==self.breath
class Person:
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email
    def __str__(self):
        return 'Person({0},{1},{2})'.format(self.fname,self.lname,self.email)
    def fullname(self):
        return self.fname + " " + self.lname
    def getmail(self):
        return self.email

class Employee(Person):
    def __init__(self,fname,lname,email,Eid,salary):
        Person.__init__(self,fname,lname,email)
        self.Eid=Eid
        self.salary=salary
    def __str__(self):
        return 'Employee({0},{1},{2},{3},{4})'.format(self.fname,self.lname,self.email,self.Eid,self.salary)
    def getsalary(self):
        return self.salary


