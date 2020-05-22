# What is a module?
#--> A module is basically a .py file were you are able to call that file and use its functions or variables from it.

# How to "CREATE" a module?
#--> To create a module just save the code you want in a file with the file extension .py
#--> Example I have 2 .py files (student.py and lecturer.py) in order to use them for explanation.

# How to "USE" a module?
#--> we can use the module we just created, by using the import statement
import student

student.studentName('Nazhim')
print("Your college is",student.collegeName)
print()               # new line

# Modules can have functions as well as variables such as (arrays, dictionaries, objects etc)
# Example of how I am accessing a dictionary from student.py
print(student.student01['Name'])
print(student.student01['Age'])
print(student.student01['Course'])

print()
# RE-NAMING A MODULE
# You can create an alias when you import a module, by using the as keyword

import lecturer as lec
lec.lecturerName('saman')

# In java we import classes but in python we import modules

# We can print out all the list of functions, variables available from a module
print(dir(student))
print(dir(lec))

# Using dir() we can list down all the functions, variables of the in built modules and the modules we create

# We also can call only a specific function or variable from a module using the "from" key word'
from extra import gender as gen
from extra import A
print(gen)
A()

