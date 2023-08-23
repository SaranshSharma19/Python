# For Loop
fruits=["apple","mango","kiwi"]
for x in fruits:
    print(x)
for x in "mango":
    print(x)
for x in fruits:
    print(x)
    if x=="mango":
        break
for x in fruits:
    if x=="mango":
        break
    print(x)
for x in fruits:
    if x=="mango":
        continue
    print(x)
"""
The range() Function
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 
(by default), and ends at a specified number.

The range() function defaults to increment the sequence by 1,
however it is possible to specify the increment value by adding a third parameter: 
range(2, 30, 3):

"""

for x in range(6):
    print(x)
for x in  range(2,6):
    print(x)
for x in range(2,22,2): # third value is the number by which we need to increment the previous number
    print(x)
for x in range(6):
    print(x)
else:
    print("number is greater than 5")

#If the loop breaks, the else block is not executed.
for x in range(6):
    if x==3:
        break
    print(x)
else:
    print("loop break")
    #it will not execute else statement bcoz if the loop of if break than els eloop will never execute

# Nested FOr Loop
a=["ae","be","ce","de"]
d=["ee","fe","ge","he"]
for x in a:
    for y in d:
        print(x,y)

"""
The pass Statement
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

"""
for x in [0,1,2]:
    pass
