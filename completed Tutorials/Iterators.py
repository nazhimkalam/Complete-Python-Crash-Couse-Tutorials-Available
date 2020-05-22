# Iterator is an object where you are able to traverse through all the values.
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator.

myTuple = ("apple", "banana", "cherry")
myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))

# normally we don't use iterator its like the old type nowadays we use for i in tupleName and get the output
# Strings are also iterable objects, containing a sequence of characters
myStr = "cake"
myStrIt = iter(myStr)

print(next(myStrIt))
print(next(myStrIt))
print(next(myStrIt))
print(next(myStrIt))


# Looping through an iterator
# We can also use a for loop to iterate through an iterable object
fruits = ("apple", "banana", "cherry")

for x in fruits:
  print(x)

myName = 'Nazhim Kalam'
for x in myName:
    print(x)

