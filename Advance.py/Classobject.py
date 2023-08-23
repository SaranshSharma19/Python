"""
Python is a object oriented programming language
Almost everthing in python is an object , with its properties and method.
A class is like an object constructor , or a "blueprint" for creating objects

TO create a class we use the keyword class:

"""
# Creating a Class named myclass , with property named x:
class myclass:
    x=5
print(myclass)

# Creating an Object p1 , and print the value of x:
class myclass:
    x=5  #x is the property of MyClass
p1=myclass() #p1 is the obuject of MyClass
print(p1.x)

# The __init__() Function
# To understand the meaning of classes we need to understand the built in __init__ function.
# All classes have function called __init__() Which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties, or other operations that are necessary
# to do when the object is being created:

class person:
    def __init__(self,name,age): #name , age , self is the property
        self.name=name
        self.age=age
p1=person("saransh",20)  #p1 is the object for person class

print(p1.name)
print(p1.age)

# Object Methods
# Objects can also contains method. Methods in objects are functions that belongs to the object.

# Inserting a function that prints a greeting , and execute it on the p1 object:

class People:
    def __init__(self,name,age): # we need to use def word to use __init__() Function.
        self.name=name
        self.age=age
    def myfun(self):
        print("Hello My name is " + self.name)

p1 = People("saransh",20)
p1.myfun()

class pe:
    def __init__(abc,name,age):
        abc.name=name
        abc.age=age
    def my(abc):
        order="my name is "+ abc.name + ", I am {} years old"
        print(order.format(p1.age))
p1=pe("Sharmila",45)
p1.my()

# Mobifying object properties
class we:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(sss):
        print("my name is "+ sss.name)
p2=we("sansh",20)
p2.myfunc()
# p2.age=40
# print(p2.age)
# p2.name="Ayush"
# print(p2.name)

# To delet name age or any parameter we use del method

class wee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myy(self):
        print("My name is "+ self.name)
p3=wee("saransh",20)
del p3.age
# print(p3.age)
# It will show error

# we can delet object using del method
# del p3
# print(p3.name)
# It will also show error

# If we don't have any content to write in a class we use pass so we don't get any error
class person:
    pass