"""
This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python
you will have to import a library, like the NumPy library.

"""
fruits=["apple","banana","kiwi","mango"]

# Accessing the elements of Array
x = fruits[0]
print(x) 

# Modifying the value at a particular index
fruits[0]="grapes"
print(fruits)

# To find the length of array we use
print(len(fruits))

# Looping Array Elemets 
for x in fruits:
    print(x)

# Adding elemets in array 
fruits.append("cherry")
print(fruits)

# Removing elemets from array
fruits.pop(1)
print(fruits)

# We can also use remove() Method to remove the elements from array
fruits.remove("cherry")
print(fruits)
