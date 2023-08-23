# Print 1-N using Recursion
def number(i,n):
    if i>n:
        return 
    print(i)
    number(i+1,n)
n=int(input("Enter the value of n: "))
number(1,n)

# Print N-1 using Recursion
def number1(i,n):
    if i<1:
        return
    print(i)
    number1(i-1,n)

n=int(input("Enter the value of n: "))
number1(n,n)