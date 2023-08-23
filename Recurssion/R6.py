# multi Recurssion calls

#Fibonacci
def fib(n):
    if n<=1:
        return n
    slast=fib(n-2)
    last=fib(n-1)  
    return last+slast
print(fib(4))