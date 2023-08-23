# Using % 
name="ABC"
course="Python Course"
age=19
s="Welcome %s to the %s at the age of %s"%(name,course,age)
print(s)

# Using Format Function
name="XYZ"
course="C"
age=19
s="Welcome {0} to the {1} course at the age of {2}".format(name,course,age)
print(s)

# Using f string(Latest Method)
name="New"
course="C Python"
age=19
s=f"Welcome {name} to the {course} course at the age of {age}"
print(s)

# Some more example using F String
a=20
b=20
print(f"the sum {a} and {b} is {a+b}")
print(f"Product of {a} and {b} is {a*b}")