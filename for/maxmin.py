def mini(a):
    return min(a)
def maxi(a):
    return max(a)
a=[]
n=int(input("Enter the value of n- "))
for i in range(0,n):
    ele=int(input("Enter the value of Ele- "))
    a.append(ele)
m=mini(a)
s=maxi(a)
print(s,m)
