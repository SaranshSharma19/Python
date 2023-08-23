from re import X


def myfunc():
    x=50
    print(x)
myfunc()
# print(x) # It will show error that x is not defined becouse x is local to only myfunc function

def myfuncc():
    x=400
    def mysubfuncc():
        print(x)
    mysubfuncc()
myfuncc()

def my():
    global x
    x=50
    print(x)
my()
print(x) # It will print 50 as a value of x becouse x is globally declared in the my function

#  the variable x is not available outside the function, but it is available for any function inside the function:
def future():
    x=500
    def infuture():
        print(x)
    infuture()
future()

# A variable created outside of a function is global and can be used by anyone
x=5000
def myfun():
    print(x)
myfun()
print(x)

"""
Naming Variables
If you operate with the same variable name inside and outside of a function,
Python will treat them as two separate variables, one available in the global scope (outside the function)
and one available in the local scope (inside the function):

"""
x=300
def myfu():
    x=200
    print(x) # It will print 200
myfu()
print(x) # It will print 300

"""
To change the value of a global variable inside a function,
refer to the variable by using the global keyword:

"""
x =300
def mee():
    global x # It will change the value of global variable
    x=2000
mee()
print(x) 