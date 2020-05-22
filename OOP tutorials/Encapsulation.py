class Student:
    def __init__(self): # initialize the variables firstly
        self.name = "No name"

    def setName(self,name):  # setters or modifiers
        self.name = name

    def getName(self):       # getters or accessors
        return self.name

# main program
obj = Student()
print(obj.getName())
obj.setName("Nazhim Kalam")
print(obj.getName())