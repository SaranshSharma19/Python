from re import M


myset={"apple","mango","kiwi","apple"}
print(myset)
print(len(myset))

# Set item can be of int bool string type
set1={"a","b","c"}
set2={1,2,3}
set3={True,False,True}
print(set1)
print(set2)
print(set3)
print(type(set1))
print(type(set2))
print(type(set3))

# Set Construct
myset=set(("apple","banana","mango"))
print(myset)
print(type(myset))

# Accessing Set Elements
myset={"apple","mango","kiwi","apple"}
for x in myset:
    print(x)
if "mango" in myset:
    print("Yes!")

myset={"apple","mango","kiwi","apple"}
myset.add("banana")
myset.add("Watermelon")
print(myset)

myset={"apple","mango","kiwi","apple"}
thisset={"watermelon","banana"}
myset.update(thisset)
print(myset)

# we can use update to add list tuple andv dictionaries etc. using update function
myset={"apple","mango","kiwi","apple"}
myset.remove("mango")
print(myset)
# we can use discard method to remove any element from set
myset={"apple","mango","kiwi","apple"}
myset.discard("mango")
print(myset)

# pop method remove the last element from set
myset={"apple","mango","kiwi","apple"}
x=myset.pop()
print(x)
print(myset)

# clear is used to empties the set:
myset={"apple","mango","kiwi","apple"}
myset.clear()
print(myset)

# del is used to delet the set completely:
myset={"apple","mango","kiwi","apple"}
del myset
# print(myset) # it will show error 

# Joining Two Sets
set1={"a","b","c"}
set2={1,2,3}
set3=set1.union(set2)
set1.update(set2)
print(set3)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets.
set1={"a","b","c"}
set2={1,2,"a"}
set1.intersection_update(set2)
print(set1)
set1={"a","b","c"}
set2={1,2,"a"}
z=set1.intersection(set2)
print(z)

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
set1={"a","b","c"}
set2={1,2,"a"}
set1.symmetric_difference_update(set2)
print(set1)

set1={"a","b","c"}
set2={1,2,"a"}
z=set1.symmetric_difference(set2)
print(z)

# Difference will give output of set 1 element whic are not in set 2
set1={"a","b","c"}
set2={1,2,"a"}
z=set1.difference(set2)
print(z)

set1={"a","b","c"}
set2={1,2,"a"}
set1.difference_update(set2)
print(set1)

# Return True if no items in set x is present in set y: (isdisjoint)
set1={"a","b","c"}
set2={1,2,"a"}
z=set1.isdisjoint(set2)
print(z)

# Return True if all items in set x are present in set y: (issubset)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)

# Return True if all items set y are present in set x:(isuperset)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y)
print(z)