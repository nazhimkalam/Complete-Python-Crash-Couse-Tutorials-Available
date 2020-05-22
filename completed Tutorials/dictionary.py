#The dictionaries are enclosed with { }
#Inside the { } we have a key value pair in this formatc{ key : value, key : value }

#Keys are unique within a dictionary while values may not be.
#The values of a dictionary can be of any type, but the keys must be of an immutable data type such as strings, numbers, or tuples.

dictionary_01 = {} #this is an empty dictionary
print(str(dictionary_01)+ ' this is an empty dictionary')

dictionary_02 = {'Name':'Nazhim','Age':'18', 'Gender':'Male'}

print(dictionary_02)           #I display the entire dictionary

print(dictionary_02['Name'])   #I display Nazhim

print(dictionary_02.get('Age'))#Using dictionary.get() is similar to using dictionary[] but get() is much better cuz it doesn't throw errors if the key is not present, instead a alternative message will be displayed

#print(dictionary_02['school']) Throws up an error due to key not present

print(dictionary_02.get('school','The school key is not present, therefore no value to be displayed')) #displays the alternative message

#UPDATING A DICTIONARY --------------------------------------

#updating an existing key value
dictionary_02['Age'] = 19
print(str(dictionary_02) + ' this is the updated dictionary')

#adding a new key value pair into the dictionary
dictionary_02['school'] = 'Royal Institute'
print(str(dictionary_02) + ' this is the updated dictionary')

#DELETION IN A DICTIONARY -----------------------------------

#removing an entry with a key name
del(dictionary_02['Name'])
print(str(dictionary_02) + ' Name has been deleted')

#remove all the entries in a dictionary and make it EMPTY
tempDic = {'stdID':'2019281', 'UoWID':'w1761265','Name':'Nazhim'}
print(str(tempDic) + ' this is the temp dictionary')
tempDic.clear()                  #I delete all the records in the tempDic
print(tempDic)

#delete the entire dictionary there by the dictionary is of no more
tempDic2 = {'stdID':'215364', 'UoWID':'w17651236','Name':'Harry Potter'}
del(tempDic2)
#print(tempDic2)  #this will throw you an error because the dictionary has been deleted and doesn't exist now

#LENGTH OF THE DICTIONARY
print('There are ' + str(len(dictionary_02)) + ' records in the dictionary')

#COPYING A DICTIONARY
copyOfdictionary_02 = dictionary_02.copy()
print(str(dictionary_02) + ' original one')
print(str(copyOfdictionary_02) + ' a copied version')

print(copyOfdictionary_02.fromkeys('nazhim',7))     #breaks 'Nazhim' into 6 individual characters as keys and gives of the characters with the value 7
print('Age' in copyOfdictionary_02.keys())          #this returns True if the 'Age' key is present in the dictionary

#Returns a list of dict's (key, value) tuple pairs
for i in copyOfdictionary_02.items():
    print(i)

#Returns list of dictionary dict's keys
for i in copyOfdictionary_02.keys():
    print(i)

#Adds dictionary dict2's key-values pairs to dict
tempDic3 = {'stdID':'215364', 'UoWID':'w17651236','Name':'Harry Potter'}
copyOfdictionary_02.update(tempDic3)
print(str(copyOfdictionary_02) + ' this is the updated dictionary')


#Returns list of dictionary dict's values
for i in copyOfdictionary_02.values():
    print(i)

#if i need to get the key and value and display both with in a message
for (k,v) in copyOfdictionary_02.items():
    print('This is the key ' + str(k) + ' and this is the corrosponding value ' + str(v))

#we can use the dict() function in order to create a dictionary
record = dict(name = "John", age = 36, country = "Norway")
#now record will act as a dictionary
print(record)           #displays the dictionary
print(record['name'])   #displays the value of name 
print(record['age'])
print(record['country'])
















