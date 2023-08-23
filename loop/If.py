# if else:
a=5
b=1
if b>a:
    print("b id greater than a")
else:
    print("a is greater than b")

# if elif else:
a=5
b=5
if b>a:
    print("b is greater than a")
elif b==a:
    print("b is equal to a")
else:
    print("both conditions are false")

# short hand if

a=5
b=10
if b>a: print("b is greater than a")

# short hand if else
a=10
b=5
print("A") if a>b else print("B")

# short hand multiple if else:
a=10
b=10
print("A") if a>b else print("=") if a==b else print("B")

# And logical operator
a=10
b=5
c=100
if a>b and c>a:
    print("c is the greatest element")
# For and both the conditions need to be true

# Or Logical operator
a=10
b=5
c=100
if a>b or a>c:
    print("a is greater than b but a is less than c")
# For or only one condition need to be true

# Nested If 
a=11
if a>10:
    print("above 10")
    if a>20:
        print("above 20")
    else:
        print("less than 20")

"""
The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content,
put in the pass statement to avoid getting an error.

"""
a=10
b=100
if b>a:
    pass # Now it will not show any error and still if content is empty
