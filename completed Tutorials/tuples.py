#A tuple is an immutable sequence of Python objects.
#Tuples are just like a list
#Differnce between list and tuple is, tuples cannot be changed like lists
#tuples use paranthesis ()
#If you need to create a fixed list like struture (which cannot be altered), then we can use tuples

emptyTuple = ()
print(emptyTuple)

#if you are creating a tuple with only one value u have to include a commma at the end
singleTuple = (50,)
print(singleTuple)

tup1 = ('Chemistry','Computing',2000,1997)
tup2 = (1,2,3,4,5)
print(tup1)
print(tup2)

#Accessing values of tuple
print(tup1[0]) #first value
print(tup1[len(tup1)-1]) #last value

#slicing a the value of the tuple [ start : end : step ]
print(tup2[2:])
print(tup2[:2])
print(tup2[1:3])
print(tup2[::2])

#You can't update a current existing tuple instead we can create a new tuple and extract values from the current tuple and put it into it
#We also cannot delete INDIVIDUAL elements from a tuple instead we can delete the entire tuple

#del(tup2[0]) #this will throw an error

#del(tup2)   #this will work
#print(tup2)

#GETTING THE LENGTH OF A TUPLE
print(len(tup2))

#CONCATINATION OF TUPLES
print(tup1 + tup2)

#REPETITION
print(tup2 * 5)

#We can check if a value is in a tuple and return a boolean value as a result
print(3 in tup2)

#We can print the values from the tuple
for i in tup2:
    print(i)


#we can also assign variables like this
x , y , z  = 1 , 2 , 3
print(str(x) + ' ' + str(y) + ' ' + str(z))

#maximum value from a tuple with numbers
print(max(tup2))

#minimum value from a tuple with numbers
print(min(tup2))

#tuple() converts a list into a tuple
randomList = [51,24,62,53,65,12,56]
print(str(randomList) + ' this is a list')
print(str(tuple(randomList)) + ' this is now a tuple')
print(str(randomList) + ' but the main list is not permenantly changed')
