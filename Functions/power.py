def power(x,y):
    ans=1
    while y!=0:
        ans*=x
        y-=1
    return ans


a=int(input("Enter the value of a- "))
b=int(input("Enter the value of b- "))
m=power(a,b)
print(m)