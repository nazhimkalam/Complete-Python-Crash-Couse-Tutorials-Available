#A set is a collection which is unordered and unindexed.
#In Python sets are written with curly brackets.

#SETS ARE USED TO REMOVE DUPLICATE DATA PRESENT IN IT

#This is a set
thisset = {"apple", "banana", "cherry","apple"}  #IF YOU NOTICE THAT THERE ARE 2 "apple" and it displays only one apple
print(thisset)         #the output of the elements are in random order

#Sets are unordered
#You cannot be sure in which order the items will appear.

#ACCESSING ITEMS IN A SET ----------------------------------------------------------

#You cannot access items in a set by referring to an index
#since sets are unordered the items has no index

#But you can loop through the set items using a for loop
for x in thisset:
    print(x)
#OR ask if a specified value is present in a set, by using the in keyword.
print('pineapple' in thisset)      #returns False
print('apple' in thisset)          #returns True


#CHANGING ITEMS IN A SET ----------------------------------------------------------

#Once a set is created, you cannot change its items
#But you can add new items.

#To add one item to a set use the add() method.
thisset.add('orange')
print(thisset)

#To add more than one item to a set use the update() method.
thisset.update(['banana','strawberry']) #NOTE: to use [] when using the update function
print(thisset)

#we have multiple methods for set such as len(), discard(), remove(), pop() etc..
#JOINING TWO SETS using union() ---------------------------------------------------

#Note: Both union() and update() will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Note: If the item to remove does not exist, remove() will raise an error.
#Note: If the item to remove does not exist, discard() will NOT raise an error.
set1.remove('a')
print(set1)

#set1.remove('z')         #This throws an error because 'z' is not present in the set1
#print(set1)

set1.discard('z')         #no error

#Note: Sets are unordered, so when using the pop() method, you will not know which item that gets removed.

#It is also possible to use the set() constructor to make a set. ----------------------
thissset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thissset)
