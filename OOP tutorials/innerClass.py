# Inner classes and Outer classes
# Let's say we need to get details of student and details of his/her laptop
class Student:
    def __init__(self, name, idNum):
        self.name  = name
        self.idNum = idNum
        self.Lap = self.Laptop()

    def show(self):
        print(self.name,self.idNum)
        self.Lap.show()

    class Laptop:
        def __init__(self):
            self.brand = 'Hp'
            self.ram = '8gb'
            self.processor = 'i5 core'

        def show(self):
            print(self.brand, self.ram, self.processor)
# MAIN PROGRAM
s1 = Student('Nazhim',2019281)


L1 = Student.Laptop()  # You can create an object of laptop like this
L1.show()

# we can use the outer class object to access the inner class object by calling the inner class methods from the outer class method
s1.show()
