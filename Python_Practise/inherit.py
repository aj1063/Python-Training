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


P = Person('Ajay','kumar','akd@gmail.com')
print(P)        
a = P.getmail()
print(a)
n = P.fullname()
print(n)

E = Employee('Anil','Kumar','asd@gmail.com',123,10000)
print(E)
A = E.getsalary()
print(A)
S = E.fullname()
print(S)