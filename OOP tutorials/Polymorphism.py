# ====> POLYMORPHISM means many behaviours
# There are four ways of implementing polymorphism
#    1.) Duck Typing
class PyCharm:
    def execute(self):
        print('Executing ide....')
class JetBrain:
    def execute(self):
        print('Executing ide....')
# obj = PyCharm()  # this also has execute method
# obj = JetBrain() # this also has execute method
# obj.execute()
print("____________________________________________________________________________________________________________")

#    2.) Operator Overloading
class Student:
    def __init__(self,mark1,mark2):
        self.mark1 = mark1
        self.mark2 = mark2

    def __add__(self, other): # adding overloading operator
        mark01Total = self.mark1 + other.mark1
        mark02Total = self.mark2 + other.mark2
        return str(mark01Total) + " " + str(mark02Total)

# main program
s1 = Student(70,84)
s2 = Student(96,55)
result = s1 + s2   # this is equal to Student.__add__(s1,s2)
# s1 becomes self and s2 becomes other in the __add__() method
print(result)
print("____________________________________________________________________________________________________________")

#    3.) Method Overloading
class CAL:
    def sum(self,a = None,b = None,c = None):
        total = 0
        if a is not None and b is not None and c is not None:   # is not is equal to !=
            total = a + b + c
        elif a is not None and b is not None:
            total = a + b
        else:
            total = a
        print(total)

# main program
obj = CAL()
obj.sum(1)
obj.sum(1,2)
obj.sum(1,2,3)

print("____________________________________________________________________________________________________________")

#    4.) Method Overriding
class A:
    def show(self):
        print('show at A')
class B(A):
    def show(self):
        print('show at B')

# main program
newObj = B()
newObj.show()

