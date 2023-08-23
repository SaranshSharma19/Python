mytuple=("apple","banana","kiwi")
print(mytuple)

# To create a tuple containing only one element we need to add comma at last
mytuple=("Apple",)
print(mytuple)

mytuple=("apple","banana","kiwi")
print(len(mytuple)) # to find the length of the tuple

#Tuple can be of int float and string type
type1=(1,2,3)
type2=('a','b','c')
type3=(True,False,True)
print(type1)
print(type2)
print(type3)
print(type(type1))
print(type(type2))
print(type(type3))

#Tuple can be created using tuple construct
mytuple=tuple(("apple","kiwi","Watermelon"))
print(mytuple)

#Accessing Element in Tuple
mytuple=("apple","banana","kiwi")
print(mytuple[1])

if "apple" in mytuple:
    print("yes")

#To Change the element of a tuple we need to convert tuple into a list first
x=("apple","banana","kiwi")
y=list(x)
y[1]="hello"
x=tuple(y)
print(x)

thistuple=("apple","banana","watermelon")
y=list(thistuple)
# y[1]="Hello"
y.append("orange")
thistuple=tuple(y)
print(thistuple)

thistuple=("apple","banana","watermelon")
y=("kiwi",)
thistuple+=y
print(thistuple)

#To remove the element from tuple we need to convert it into a list
#To delet the tuple we can use del method
#To remove all element from tuple we can use clear method

thistuple=("apple","banana","watermelon")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)

thistuple=("apple","banana","watermelon")
del thistuple
#print(thistuple) #it will show an error



