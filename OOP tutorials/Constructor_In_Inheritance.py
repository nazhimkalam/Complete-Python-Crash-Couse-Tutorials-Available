# PARENT constructor and CHILD constructor
# ---> If you don't have child constructor then by default it will run the parent constructor, we have to use child object.
class Parent:
    def __init__(self):
        print('Parent Constructor...')

class Child(Parent):
    pass            # Child class empty and no constructor created by the user but in general has its default constructor

# main program
obj = Child()   # this will run the parent class constructor because, we didn't define constructor for child class

print('_______________________________________________________________________________________________________________________')
#_______________________________________________________________________________________________________________________

# but if we define our constructor in child class, then it will run the child class constructor
class NewParent:
    def __init__(self):
        print('NewParent Constructor...')

class NewChild(NewParent):
    def __init__(self):
        print('NewChild Constructor...')

# main program
obj1 = NewChild() # this will run the child class constructor because, we defined constructor for child class

print('_______________________________________________________________________________________________________________________')
#_______________________________________________________________________________________________________________________

# If you defined constructors for both child and parent class, and you want to call the parent class constructor using child object
# We can use the "super()" to help us solve this problem
# super() refers to the parent class content

class A:
    def __init__(self):
        print('In constructor A....')

    def random(self):
        print('Random method in A')
class B(A):
    def __init__(self):
        super().__init__()  # now this calls and executes the class A constructor
        print('In constructor B')
        super().random()    # we also can run the methods from class A like this

# main program
object1 = B()

print('_______________________________________________________________________________________________________________________')
#_______________________________________________________________________________________________________________________

# M.R.O ( method resolution order )
# This only applies to multiple inheritance, because 1 class inherits 2 classes

class X:
    def __init__(self):
        print('Constructor X...')

class Y:
    def __init__(self):
        print('Constructor Y...')

    def testerMethod(self):
        print('Tester method for class Y')

class Z(X, Y):      # MRO says start from X and then go to Y
    def __init__(self):
        super().__init__()      # for this it runs the class X cuz constructor present in class X
        super().testerMethod()  # for this it runs the class Y cuz class Y only has this method
        print('Constructor Z...')

#  if the method is not present in class X then only it goes to class Y and checks
# main program
newObj = Z()
