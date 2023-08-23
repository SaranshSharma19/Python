from collections import defaultdict
# arr = [15,5,3,7,0,1,7,18,2,21,19]
# odd = []
# even = []
# m = sorted(arr)
# for i in m:
#     if arr.index(i)%2!=0:
#         odd.append(i) 
#     else:
#         even.append(i)
# odd.sort()
# even.sort()
# print(odd[1]+even[-2])

# m = defaultdict(list)
# arr = ["a","b","c","d","a","a"]
# for i in arr:
#     if i in m:
#         n = m[i]
#         s = n[-1]
#         m[i].append(s+1)
#     else:
#         m[i].append(1)
# print(m)

# arr = [i for i in range(10)]
# for i in range(10,36):
#     arr.append(chr(i+55))
# n = int(input())
# divisor = int(input())
# li = []
# while n!=0:
#     rem = n%divisor
#     li.append(rem)
#     n = n//divisor
# li.reverse()
# a = ""
# for i in li:
#     a+=str(arr[i])
# print(a)

str1=input()
str2=input()
if len(str1)!=len(str2):
    print("No")
else:
    str1+=str2
    d={}
    c=0
    for i in str1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for i in d:
        if d[i]%2!=0:
            c=1
            break
    if c==1:
        print("no")
    else:
        print("Yes")