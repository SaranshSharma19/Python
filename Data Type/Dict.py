mydict={"Brand":"Ford","Model":"Mustang","Year":"2021"}
print(mydict)
print(mydict["Brand"]) # It will print brand value

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:
mydict={"Brand":"Ford","Model":"Mustang","Year":1900,"Year":2022}
print(mydict["Year"])
print(len(mydict))

# Dictionaries item can be of int boolean string and of list Data Type
mydict={"Brand":"Ford","Electric":True,"Year":2022,"Colours":["Red","Black","white"]}
print(mydict)
print(type(mydict))

# Accessing dictionaries Item
mydict={"Brand":"Ford","Model":"Mustang","Year":"2021"}
print(mydict["Brand"])

# We can also use get() method to access the value related to a particular key
x=mydict.get("Brand")
print(x)

# To know the all keys of a particular dictionary we use key() method which will return a list of all keys
mydict={"Brand":"Ford","Model":"Mustang","Year":"2021"}
x=mydict.keys()
print(x)

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car={"brand":"ford","year":2022,"model":"mustang"}
x=car.keys()
print(x)
car["colour"]="white"
print(x)

# To know all the values of the keys we use value() method which will return a list of all values:
car={"brand":"ford","year":2022,"model":"mustang"}
x=car.values()
print(x)

# Make a change in the original dictionary, and see that the values list gets updated as well:
# Add a new item to the original dictionary, and see that the values list gets updated as well:

car={"brand":"ford","year":2022,"model":"mustang"}
x=car.values()
print(x)

car["year"]=2000
print(x)

car["colour"]="Red"
print(x)

# items() method will return item in a dictionary as tuple in a list
car={"brand":"ford","year":2022,"model":"mustang"}
x=car.items()
print(x)

car={"brand":"ford","year":2022,"model":"mustang"}
x=car.items()
print(x)
car["Colour"]="red" # Adding Item in dictionary data type
print(x)

car={"brand":"ford","year":2022,"model":"mustang"}
if "colourl" in car:
    print("Yes! colour in car")
else:
    print("No! colour in car")

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

car={"brand":"ford","year":2022,"model":"mustang"}
car.update({"year":1900}) # Adding Item in Dictionary Data Type
print(car)

# Removing Item from Dictinary Data Type 
# We can use pop():
 
car={"brand":"ford","year":2022,"model":"mustang"}
car.pop("brand")
print(car)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car={"brand":"ford","year":2022,"model":"mustang"}
car.popitem()
print(car)

# we can completely delet the dictionary using del method:
car={"brand":"ford","year":2022,"model":"mustang"}
del car
# print(car) # it will show error ( no longer exists)

# To empy the dictionary we can use clewar method:
car={"brand":"ford","year":2022,"model":"mustang"}
car.clear()
print(car)
