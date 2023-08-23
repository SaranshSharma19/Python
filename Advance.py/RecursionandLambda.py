"""
Python also accept function recursion, which means a defined function can call itself.

Recursion is a commonly mathematical and programming concept. It means that a function calls itself.

"""
def myrecursion(x):
    if x>0:
        r=x+myrecursion(x-1) # It will decrement the value of x
        print(r)
    else:
        r=0
        print(r)
    return r
myrecursion(6)

# Lambda Functions:

x=lambda a:a+10
print(x(5))

def fun(n):
    return lambda a:a*n
myfunc=fun(2) # n=2
myfun=fun(3) # n=3
print(myfunc(11)) # a=11
print(myfun(11)) # a=11