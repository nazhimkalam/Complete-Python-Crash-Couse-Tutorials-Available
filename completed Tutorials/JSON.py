#    JSON ( JavaScript "Object" Notation )
#--> JSON is a syntax for "storing" and "exchanging" data.
#--> JSON is "text", written with JavaScript object notation.
#--> Python has a built-in package called 'json', which can be used to work with "JSON data"

import json

#--> Parse JSON -( Convert from JSON to Python)
#--> If you have a JSON string, you can 'parse' it by using the "json.loads()" method.
#--> The result will be a Python dictionary. eg:- {.......}

# Example 01: Converting from JSON to Python
x = '{ "name":"John", "age":30, "city":"New York" }'  # this is some random JSON file

y = json.loads(x)  # parse x using json.loads()

print(y)            # the result is a python dictionary
print(x)            # this will also result a python looking dictionary but it is a JSON file
#print(x['name'])   #Since (x) is a JSON file you can't access it like a python dictionary unless you convert it to.

print(y['name'])    # this will display "John" because we have parse the JSON file into a python form dictionary
print(y['age'])
print(y['city'])

# Example 02: Convert from Python to JSON

#--> If you have a Python 'object', you can convert it into a 'JSON string' by using the 'json.dumps()' method.

# a Python object (dictionary) 'dictionary acts like an object':
studentObj = {                     #---->  details of the student object in dictionary form
  "name": "Nazhim",
  "age": 18,
  "city": "Colombo"
}

print(str(studentObj) + ' <---- this is a python student object')             #----> this is a python object
# we convert an object into a string using the json.dumps() function provided by the json module

jsonStringCreated = json.dumps(studentObj)                                    #----> convert into JSON

print(jsonStringCreated + ' <------ this is a JSON string')                   #-----> the result is a 'JSON string'

#--------------------------------------------------------------------------------------------------------------------
# --> You can convert Python objects of the following types, into JSON strings:

# ------> dict
# ------> list
# ------> tuple
# ------> string
# ------> int
# ------> float
# ------> True
# ------> False
# ------> None

print(json.dumps({"name": "John", "age": 30}))  # dictionary into JSON string
print(json.dumps(["apple", "bananas"]))         # list into JSON string
print(json.dumps(("apple", "bananas")))         # tuple into JSON string
print(json.dumps("hello"))                      # string into JSON string
print(json.dumps(42))          # integer into JSON string
print(json.dumps(31.76))       # float into JSON string
print(json.dumps(True))        # True into JSON string
print(json.dumps(False))       # False into JSON string
print(json.dumps(None))        # None into JSON string

# When you convert from "Python to JSON", "Python objects are converted into the JSON (JavaScript)" equivalent:
# Python-----JSON-----
# dict	     Object
# list    	 Array
# tuple 	 Array
# str	     String
# int	     Number
# float 	 Number
# True	     true
# False	     false
# None	     null

# Example 03: Convert a Python object containing all the legal data types
pythonObject = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print("You are able to see the conversion of python objects into JSON type (javascript)")
print(json.dumps(pythonObject))

# It's hard to read the JSON strings without indentations and line breaks, so we can use the "indent" in dumps()
# to format the JSON result string

# use four indents to make it easier to read the result:
print(json.dumps( pythonObject, indent = 4 ))  # Now it's much easier to read the JSON string

# Use the separators parameter to change the default separator
print(json.dumps(pythonObject, indent=4, separators=(". ", " = ")))


# Order the Result
# sort the result alphabetically by keys:
print(json.dumps(pythonObject, indent=4, sort_keys=True))


