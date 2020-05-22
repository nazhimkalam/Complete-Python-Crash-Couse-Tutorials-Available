class Student:
    schoolName = 'Royal Institute Havelock Town' # class variable or static variables
    count = 0
    @classmethod
    def schoolDetails(cls):         # class method
        cls.count += 1
        print('School name is ' + cls.schoolName + ' and so far we have calculated results for ' + str(cls.count) + ' students')

    @staticmethod
    def numberOdStudentsDisplay(groupNumber):   # static method
        # we assume the same student results are not displayed more than once
        return 'These results are calculated by the group number ' + str(groupNumber)

    def __init__(self,name,age,idNum):   # we have to initialize the variables here as well that why it's called _init_ ( constructor )
        self.name = name         # instance variables
        self.age = age
        self.idNum = idNum
        self.mark = 0
        self.schoolDetails()

    def set_mark(self, enteredMark): # instance method and called modifier or setters
        self.mark = enteredMark
    def getMark(self):   # instance method and called Accessor or getters
        return self.mark

    def displayResult(self): #instance method
        message = 'For the 2020 Math Examination \n' + self.name + ' age of ' + str(self.age) + ' with the ID ' + str(self.idNum) + ' has scored ' + str(self.getMark())
        return message
# MAIN PROGRAM
student01 = Student('Nazhim',18,2019281)        # creating student object and pass the data for the variables
student02 = Student('Hashim',14,2015364)
student03 = Student('Shaahid',18,2019251)
student04 = Student('Ranul',14,2019542)
student05 = Student('Hammad',14,2015623)
student01.set_mark(70)
student02.set_mark(54)
student03.set_mark(88)
student04.set_mark(77)
student05.set_mark(40)
print(student05.displayResult())
print(Student.numberOdStudentsDisplay("B120")) # displaying a static method content