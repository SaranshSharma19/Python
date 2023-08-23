def arr(a):
    s=0
    end=len(a)
    if end%2==0:
        while s<end:
            temp=a[s+1]
            a[s+1]=a[s]
            a[s]=temp
            s+=2
        return a
    else:
        while s<end-1:
            temp=a[s+1]
            a[s+1]=a[s]
            a[s]=temp
            s+=2
        return a  
n=int(input("Enter The Value of n- "))
a=[]
print("Enter The value of a-")
for i in range(n):
    ele=int(input())
    a.append(ele)
print(arr(a))