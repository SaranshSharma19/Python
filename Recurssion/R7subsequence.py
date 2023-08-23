def sub(ind,a,arr,n):
    if ind>=n:
        print(a,end=" ")
        return
    a.append(arr[ind])
    sub(ind+1,a,arr,n)
    a.pop()
    sub(ind+1,a,arr,n)
arr=[3,1,2]
n=3
a=[]
sub(0,a,arr,n)