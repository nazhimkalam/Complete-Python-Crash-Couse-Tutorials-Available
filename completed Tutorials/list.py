# NOTE: we don't have arrays in python instead we use lists.

#---------------------------------------------------------------------

#creating a list for numbers in a range
listOne = list(range(20))   #this creates a list of values 0 to 19
print(str(listOne) + " this is my list")

#---------------------------------------------------------------------

#append()	Adds an element at the end of the list
listOne.append(99)
print('\n')    #like this I can print a new line
print('I have appended 99')
print(listOne)

#---------------------------------------------------------------------

#getting the length of the list using len()
print('\n') 
lengthOflistOne = len(listOne)
print('This is the length of the list is ' + str(lengthOflistOne))

#---------------------------------------------------------------------

#printing all the items in the list
print('\n')
print('These were the data present in the list')
for data in listOne:
    print(data)

#---------------------------------------------------------------------
    
#clear()	Removes all the elements from the list
print('\n')
fruits = ['apple','orange','pear']
print('This is NOT an empty list:' + str(fruits))

fruits.clear()
print('This is now a permenant EMPTY list' + str(fruits))

#---------------------------------------------------------------------

#copy()	Returns a copy of the list
print('\n')
listTwo = listOne.copy()
print('This is a duplicate copy of listOne ' + str(listTwo))

#---------------------------------------------------------------------

#count()	Returns the number of elements with the specified value
print('\n')
listTwo.append(5)
listTwo.append(5)
listTwo.append(5)
print('I have ' + str(listTwo.count(5)) + ' of number \'5\' element present in the listTwo')

#---------------------------------------------------------------------

#extend()	Add the elements of a list (or any iterable), to the end of the current list 
food = ['cake','biscuit','chicken','eggs']
drinks = ['soda', 'fanta', 'coke', '7up']
print('\n')
food.extend(drinks) #I am adding all the elements from the drinks list into the end of the food list
print(food)

#---------------------------------------------------------------------

#index()	Returns the index of the first element with the specified value
print('\n')
print(str(food.index('chicken')) + ' this is the index of chicken in the food list')
print(str(food.index('coke')) + ' this is the index of coke in the food list')

#---------------------------------------------------------------------

#insert()	Adds an element at the specified position
print('\n')
food.insert(2,'lamb')
print('You will be able to see that I have added a new element called \'lamb\' into position 2 of the food list')
print(food)

#---------------------------------------------------------------------

#pop()   	Removes the element at the specified position and I will also be able to display the popped result
print('\n') 
poppedItem = food.pop(2)
print('This is the popped item ' + str(poppedItem))
print('This is the updated food list')
print(food)
#---------------------------------------------------------------------

#remove()	Removes the first item with the specified value but I won't be able to display the removed result
print('\n')
print('I have removed an element for the food but not able to display the removed food item')
food.remove('coke')
print(food)

#---------------------------------------------------------------------

#reverse()	Reverses the order of the list
#reverse order changes the order of the list completly
print('\n')
print('This is list in the normal order')
print(food)
food.reverse()
print('This is the revese order of the list')
print(food)

#---------------------------------------------------------------------

#sort()	Sorts the list
print('\n')
print('sort() sort the list alphabetically for the list which consists of alphabets')
food.sort()
print(food)
numbers = [8,7,5,6,6,1,3]
numbers.sort()
print('\nFor a list with numbers the sort() will sort the elements from ascending order')
print(numbers)

#using NEGATIVE indexes to access elements
myList = [84,51,25,46,93,54]
print(myList[0])              #this gives me 84 using positive index 
print(myList[-len(myList)])    #this gives me 84 using negative index


#WE CAN USE STEP TO DISPLAY THE LIST IN REVERSE ORDER [START : END : STEP]
# WHEN STEP IS NEGATIVE IT WILL DISPLAY IN REVERSE
myListR = [84,51,25,46,93,54]
print(myListR[::1]) #displays the same order as to we made
print(myListR[::-1]) #displays the reverse order of the list
      
      
#SORT()  VS  SORTED()

a = [2,1,5,3,4,6]

#sorted() is temperally sorting into a new variable (list)
temperallySortedList = sorted(a)
print(str(a) + ' this is the original list')
print(str(temperallySortedList) + ' this is the temporally sorted list')
#sort() is permenant sorting for the same variable (list)
a.sort()
print(str(a) + ' this is the permenant sorted list')


#---------------------------------------------------------------------------------
#use of list() function
#if pass an existing list into the list() as the parameter then you will get a copy of it.
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
copyOfAlphabets = list(alphabets)
print(copyOfAlphabets)

#converts a (string,tuple,dictionary,set) into a list form with characters
something1 = list('nazhim')
print(str(something1) + ' string')

vowel_tuple = ('a', 'e', 'i', 'o', 'u')
print(str(list(vowel_tuple)) + ' tuple')

vowel_set = {'a', 'e', 'i', 'o', 'u'}
print(str(list(vowel_set)) + ' set') #output of this is in random order

vowel_dictionary = {'a': 4, 'e': 2, 'i': 3, 'o':1, 'u':5}
print(str(list(vowel_dictionary)) + ' dictionary')











