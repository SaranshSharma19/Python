# Print from 1-N without using +1 operator.
# Using BackTracking
def number(i,n):
    if i<1:
        return 
    number(i-1,n)
    print(i)
n=int(input("Enter the value of n: "))
number(n,n)

# Print from N-1 without using +1 operator.
# Using BackTracking
def number(i,n):
    if i>n:
        return 
    number(i+1,n)
    print(i)
n=int(input("Enter the value of n: "))
number(1,n)