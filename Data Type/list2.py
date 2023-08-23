#Loop-: print item of list one by one using loop

#For Loop
mylist=["Apple","Orange","Kiwi","Banana","WaterMelon"]
for x in mylist:
    print(x)

print(len(mylist)) # To find the length of the List
for i in range(len(mylist)):
    print(mylist[i])

#While Loop
mylist=["Apple","Orange","Kiwi","Banana","WaterMelon"]
i=0
while i<  len(mylist):
    print(mylist[i])
    i=i+1

# Looping Using List Comprehension
# List Comprehension offers the shortest syntax for looping through lists:
mylist=["apple","Orange","Kiwi","Banana","WaterMelon"]
[print(x) for x in mylist]
newlist=[]
for x in mylist:
    if "a" in x:
        newlist.append(x)
print(newlist)

fruits=["apple","Orange","Kiwi","Banana","WaterMelon"]
nlist=[x for x in fruits if "a" in x] #Return Those Elemets Which Include 'a' alphabet
mlist=[x for x in fruits if x!="apple"] # Return List Which does Not Include apple
slist=[x.upper() for x in fruits] # All Elements in Uppercase
qlist=['Hello' for x in fruits] # Replace all Elemnets by Hello
rlist=[x if x!="Banana" else "Hello" for x in fruits] # Banana is replaced by Hello
print(nlist)
print(mlist)
print(slist)
print(qlist)
print(rlist)

mylist=[x for x in range(10)]
print(mylist)