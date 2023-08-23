"""
Python Iterators -:

An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().

"""
mytuple=("Apple","Mango","Banana")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects
mystr="Banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Using For Loop For Iteration
mytuple=("Apple","Mango","Banana")
for x in mytuple:
    print(x)

"""
To create an object/class as an iterator you have to implement 
the methods __iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(),
which allows you to do some initializing when the object is being created.

"""

"""
                                iter
The __iter__() method acts similar, you can do operations (initializing etc.),
but must always return the iterator object itself.
                                next
The __next__() method also allows you to do operations, and must return the next item in the sequence.

"""

# Create an iterator that return number  from 1 to 5
class mynumber:
    def __iter__(self):
        self.a=1       # .a is used to increment the variable value.
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=mynumber()
myit=iter(myclass)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

class mynumber():
    def __iter__(self):
        self.a=2
        return self
    def __next__(self):
        if self.a<=20: 
            x=self.a
            self.a+=2
            return x
        else:
            raise StopIteration
myclass=mynumber()
myit=iter(myclass)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

