"""
Python does not have a random() function to make a random number,
but Python has a built-in module called random that can be used to make random numbers:

"""

import random
print(random.randrange(0,10))

for x in "Hello":
    print(x)

"""To check if a certain phrase or character is present in a string, we can use the keyword in."""

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
 print("Yes , 'free' in txt")

"""
Slicing-:

You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

"""
"""Get the characters from position 2 to position 5 (not included):"""
b = "Hello, World!"
print(b[2:5]) # peeche wallha nhi leta

b = "Hello, World!"
print(b[-4:-2]) # Aage wallha nhi leta

x=" Hello I am Saransh "
print(x.upper())
print(x.lower())
print(x.strip()) #method removes any whitespace from the beginning or the end:
print(x.replace("I","aaii"))
print(x.split())#The split() method splits the string into substrings if it finds instances of the separator:

#String Cocatination
a="Hello"
b="I am saransh"
c=a+b
d=a + " " + b #to Add Space
print(c)
print(d)

"""
String Format
As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
But we can combine strings and numbers by using the format() method!

The format() method takes the passed arguments, formats them,
and places them in the string where the placeholders {} are:
The format() method takes unlimited number of arguments, 
and are placed into the respective placeholders:

"""
a=70
b="Hello i am saransh {}"
print(b)
print(b.format(a))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} prices of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder="I want to pay {2} dollars for {0} pieces of item {1}"
print (myorder.format(quantity,itemno,price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
"""
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

The escape character allows you to use double quotes when you normally would not be allowed:
sign=\"\"

"""

txt="I am Saransh and I \"am\" 20 \'years\' old"
B= "Hello \rWorld!" #\r carriage return
print(txt)
print(B)

A="hey\fhow are you"
print(A)