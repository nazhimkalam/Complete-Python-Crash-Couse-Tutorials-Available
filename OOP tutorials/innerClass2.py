# Inner classes and Outer classes
# Let's say we need to get details of student and details of his/her laptop

class Student:
    def __init__(self, name, idNum):
        self.name  = name
        self.idNum = idNum

    def show(self):
        print(self.name,self.idNum)

    class Laptop:
        def __init__(self, brand, ram, processor):
            self.brand = brand
            self.ram = ram
            self.processor = processor

        def show(self):
            print(self.brand, self.ram, self.processor)
# MAIN PROGRAM
# l1 = Student.Laptop('Dell','8gb','i5 core')  # now this will display the result but it has no link with student
# l1.show()

s1 = Student('Nazhim',2019281)
s1.show()                     # displays student details

l1 = s1.Laptop('Dell','4gb','i3 core',)
l1.show()                     # displays the s1 laptop details
# this is related to student because without s1 you aren't able to add the laptop details