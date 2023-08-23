"""
A Function is a block of code which only run when it is called
You can pass data, known as parameters into a function.
A function can return data as a result

"""
def my_function():
    print("Hello from my_funtion side")
my_function()

"""
Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

"""
# Arguments are often shortened to args in python documentations.
def myfunc(fname):
    print(fname + " Sharma")
myfunc("Amardeep")
myfunc("Sharmila")
myfunc("Shruti")
myfunc("Riya")
myfunc("Saransh")

def myfunction(fname,lname):
    print(fname +" "+ lname)
myfunction("Saransh","Sharma")

# If function expects 2 arguments , you have to call the function with 2 arguments , not more and not less .
# def myfunction(fname,lname):
#     print(fname +" "+ lname)
# myfunction("Saransh")        # It will lead to an error

# IF you do not know how many arguments that will be passed into your function add a * before the parameter name in the function definition.
# This way the function will recieve a tuple of arguments and can access the item accordingly

# Arbitrary Arguments (Denoted By -: *args)
def myfunc(*kids):
    print("the youngest kid is " + kids[2])
myfunc("Shruti","Riya","Saransh")

# Keyword Arguments(Key=Value)
def myy(child3,child2,child1):
    print("The Youngest Chile is: "+child3)
myy(child1="Shruti",child2="Riya",child3="Saransh")

# If you do not know how many keyword arguments that will be passed to a function add two **
# (Asterisk) before the parameter name in the function definition.
def myyy(**child):
    print("Hey what is your name, Hi i am "+child["fname"] +" "+ child["lname"])
myyy(fname="Saransh",lname="Sharma")

# Arbitrary Keyword Argument are often shortened to *kwarg in Python Dictionaries.
def mykid(**kids):
    print(kids["fname"]+" "+kids["lname"])
mykid(fname="Sharmila",lname="Sharma")

# Default Parameter Value
def mycountry(country = "India"):
    print("I am from "+country)
mycountry("USA")
mycountry() # Default value
mycountry("Brazil")
mycountry("UAE")

# Passsing a list as an arguments:
def myfood(food):
    for x in food:
        print("I love to eat "+x)
food=["Noodles","Pizza","Burger"]
myfood(food)

def mytable(x):
    return 6*x
for x in range(1,11):
    print(mytable(x))

# If we do not have anything to write in the function than we use pass statement to avoid geeting an error
def myfunction():
    pass
