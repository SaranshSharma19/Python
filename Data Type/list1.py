from audioop import add


mylist=["apple","orange","Kiwi"]
print(mylist)
print(mylist[0])
#In list Index start form 0

"""
The list is changeable, meaning that we can change, add,
and remove items in a list after it has been created.

Allow Duplicates-:
Since lists are indexed,
lists can have items with the same value:

List Items - Data Types
List items can be of any data type:

A list can contain different data types:

"""
my=["apple","Cherry","orange","apple"]
print(my)  #Duplication Example
print(len(my)) #To find Length of the list


li1=[1,2,3,4,45]
li2=["apple","Hello","HI"]
li3=[True,False,True]
print(li1)
print(li2)
print(li3)

li4=[1,"apple",True]
print(li4)
print(type(li4)) #Data Type

# wecan use List Construct to construct a list
# list()

li5=list(("apple",5,"Hi"))
print(li5)

""" 
                            IMPORTANT
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

"""

#Access item
myli=["apple","cherry","KIwi","orange","Banana"]
print(myli[1])

'''
Negative indexing means start from the end

-1 refers to the last item,
-2 refers to the second last item etc.

'''
print(myli[-1])

'''
Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

'''
print(myli[2:5])
#The search will start at index 2 (included) and end at index 5 (not included).

#Negative Indexes
#The search will start at index 2 (included) and end at index 5 (not included).
print(myli[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
  print("NO!,apple is not in the list")  

'''
Change Item Value-:
To change the value of a specific item,
refer to the index number

'''
thatlist=["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thatlist[1]="Black"
print(thatlist)
thatlist[1:3]=["Hello","Hi"]
print(thatlist)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist[1:3]=["Watermelon"]
print(thislist)

'''
Insert Items-:
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

'''
thislist=["apple", "banana", "cherry"]
thislist.insert(2,"Watermelon")
print(thislist)

'''
Append Items-:
To add an item to the end of the list, use the append() method:

'''
thislist = ["apple", "banana", "cherry"]
thislist.append("Hello")
print(thislist)

'''
Extend List
To append elements from another list to the current list, use the extend() method.
The elements will be added to the end of the list.

'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

"""
              IMPORTANT
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove
mylist=["apple","Banana","orange"]
mylist.remove("Banana")
print(mylist)

#pop
mylist=["apple","Banana","orange"]
mylist.pop(1)
print(mylist)

# If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
mylist=["apple","Banana","orange"]
del mylist[0]
print(mylist)

# clear is used to remove every element from list 
mylist=["apple","Banana","orange"]
mylist.clear()
print(mylist)


