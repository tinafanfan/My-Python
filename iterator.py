# source: https://www.w3schools.com/python/python_iterators.asp

# show usage of iter() and next()
# An iterator is an object that contains a countable number of values.
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator.
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))

# create an iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter)) # 1
print(next(myiter)) # 3

# create an iterator with StopIteration that avoid unlimit iteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
    else:
        raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x) # 1,2,...,20
