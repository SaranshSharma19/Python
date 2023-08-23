from re import X
from stat import FILE_ATTRIBUTE_OFFLINE


print("Hello world")
if 5>2:
 print("Five is Greater Than Two")
x=5
# print(x) 
# #is used for single line comment
# """ Multi Line Comment """

x="sally"
#print(x)

#Casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#for Knowing the type of Variable
print(type(y))

#Case Sensitive
a=4      # a is different from A 
A="Hi"
print(a)
print(A)
x=str("s1")
print(x)

"""
Variable Names-:

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""
"""
Camel Case -: 
Each word, except the first, starts with a capital letter:
myVariableName = "John"

Pascal Case -:
Each word starts with a capital letter:
MyVariableName = "John"

Snake Case -:
Each word is separated by an underscore character:
my_variable_name = "John"

"""

x,y,z=3,4,5
print(x,y,z)

r=s=t=5
print(r,s,t)

"""
Unpack a Collection
If you have a collection of values in a list, tuple etc. 
Python allows you to extract the values into variables. 
This is called unpacking.

"""
fruits=["orange",5,"hi"]  # Unpacking
x,y,z=fruits
print(x,y,z)

"""You can also use the + operator to output multiple variables:"""
x = "Hi, "
y = "I am "
z = "Saransh"
print(x + y + z)

# Function
x="good"   # Gloabal Variable
def myfun():
    print("python is "+x)
myfun()

x="good"   # Gloabal Variable
def myfun():
    x="fantastic"  # Local Variable for function
    print("python is "+x)
myfun()

print("python is "+x)

"""To create a global variable inside a function, you can use the global keywor"""
def fun():
    global x 
    x="Awesome"
    print("Pyhton is "+x)
fun()
print("Pyhton is "+x)
"""
To change the value of a global variable inside a function, refer to the variable 
by using the global keyword:

"""
x="good"
def f():
    global x 
    x="awsm"
f()
print("Python is "+ x)    

#Multi Line String
g="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(g)

a="Hello World"
print(a[1])

#bool
class myclass():
    def __len__(self):
        return 1 # It will return True
        # return 0 # It will return False
myobject=myclass()
print(bool(myobject)) 

#Function Bool
def myfun():
    return True
print(bool(myfun))

def my():
    return False # It will return NO (Else Loop is Executed in this)
    # return True # It will Return Yes (If Loop is Executed in this)
if my():
    print("YES!")
else:
    print("NO!")  

def m():
    # return False # It will return NO (Else Loop is Executed in this)
    return True # It will Return Yes (If Loop is Executed in this)
if m():
    print("YES!")
else:
    print("NO!")     

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function,
which can be used to determine if an object is of a certain data type:

"""    

l=200
print(isinstance(l,int))

s=200.0
print(isinstance(s,int))

a="""Python also has many built-in functions that return a boolean value, like the isinstance() function,
which can be used to determine if an object is of a certain data type:"""
print(a)

#Keyword argument ke baad kabhi bhi postional argument nhi aata

