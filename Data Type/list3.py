#Sorting
mylist = ["orange", "mango", "kiwi", "pineapple", "banana"]
mylist.sort()
print(mylist)

#Reverse Sorting 
mylist.sort(reverse=True)
print(mylist)

#Customize Sort Function
def fun(n):
    return abs(n)
    #return(n-50)

thislist=[100,50,60,80,88]
thislist.sort(key = fun)
print(thislist)

#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
mylist = ["Orange", "mango", "Kiwi", "pineapple", "banana"]
mylist.sort()
print(mylist)

'''
Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:

'''
mylist.sort(key=str.lower)
print(mylist)
mylist.reverse() #IIt Will Reverse The String
print(mylist)

mylist = ["Orange", "mango", "Kiwi", "pineapple", "banana"]
mylist.reverse()
print(mylist)

#Copy
mylist = ["Orange", "mango", "Kiwi", "pineapple", "banana"]
thislist=mylist.copy()
print(thislist)
slist=list(mylist)
print(slist)

#Joining Two List
list1=['a','b','c']
list2=[1,2,3]
list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

list1=['a','b','c']
list2=[1,2,3]
list1.extend(list2)
print(list1)