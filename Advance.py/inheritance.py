class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def print(self):
        print(self.firstname , self.lastname)
x=person("saransh","sharma")
x.print()

# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Creating a child class

# Example -:
# Creating a class named student which will inherit the properties and method from person class:
class student(person):
    pass

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def print(self):
        print(self.firstname,self.lastname)
class student(person):
    pass
x=student("SaransH","SharmA")
x.print()

# Adding __init__() Function  
# We can add __init__() Function to a child class
# The __init__() Function is automatically called every time the class is being used to create a new object
# When we add the __init__() function the child class will no longer inherit the properties and method of parent class
# Thus to keep the inheritance of the parent's __init__() function add a call parents __init__() function

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
class student(person):
    def __init__(self,fname,lname):
        person.__init__(self,fname,lname)
    # pass
x=student("Ansh","Arma")
x.printname()

"""
We can use super() function that will make the child class inherit all the
methods and properties from its parent:

"""

class people:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def print(self):
        print(self.firstname , self.lastname)
class student(people):
    def __init__(self,fname,lname):
        # person.__init__(self,fname,lname)
        super().__init__(fname,lname)
        self.graduationyear = 2022 # Adding Graduation Year
x=student("riya","sharma")
x.print()
print(x.graduationyear)

class people:
    def __init__(self,fname,lname,year):
        self.firstname=fname
        self.lastname=lname
        self.thisyear=year
    def print(self):
        print(self.firstname , self.lastname)
class student(people):
    def __init__(self,fname,lname,year):
        # person.__init__(self,fname,lname)
        super().__init__(fname,lname,year)
        self.graduationyear = year # Adding Graduation Year
x=student("riya","sharma",2022)
x.print()
print(x.graduationyear)

class peeps:
    def __init__(self,fname,lname,year):
        self.firstname=fname
        self.lastname=lname
        self.thisyear=year
    def printout(self):
        print(self.firstname,self.lastname,self.thisyear)
class student(peeps):
    def __init__(self,fname,lname,year):
        peeps.__init__(self,fname,lname,year)
        self.graduationyear=year
# Adding a method named welcome:
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
x=student("Saksham","Garg",2020)
# x.printout()
x.welcome()
