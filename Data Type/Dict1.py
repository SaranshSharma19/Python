# Loops

car={"brand":"ford","year":2022,"model":"mustang"}
for x in car: # Print all key names in the dictionary, one by one:
    print(x)
for x in car: # Print all values in the dictionary, one by one:
    print(car[x])
for x in car.values(): # Print all values in the dictionary, one by one:
    print(x)
for x in car.keys(): # Print all keys in the dictionary, one by one:
    print(x)
for x,y in car.items(): # Print all keys and Values in the dictionary, one by one:
    print(x , y)

# Copy the Dictionary 
car={"brand":"ford","year":2022,"model":"mustang"}
mydict=car.copy()
print(mydict)

# Another function to copy is by using dict() method:
car={"brand":"ford","year":2022,"model":"mustang"}
mydict=dict(car)
print(mydict)

# Nested Dictinary
myfamily={
    "child1" : {
        "name": "Shruti",
        "age" : 29
    },
        "child2" : {
        "name": "riya",
        "age" : 23
    },
        "child3" : {
        "name": "saransh",
        "age" : 20
    }
}
print(myfamily)
child1 = {
        "name": "Shruti",
        "age" : 29
    }
child2 = {
        "name": "riya",
        "age" : 23
    }
child3 = {
        "name": "saransh",
        "age" : 20
    }
myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily)

x=("model","year","age")
y=0
mydict=dict.fromkeys(x,y)
print(mydict)