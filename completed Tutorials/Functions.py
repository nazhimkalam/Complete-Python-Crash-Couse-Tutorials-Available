#Functions have to be declared at first then later only the main program comes

def firstFunc():
    print ('This is my first function')

def secondFunc(number,string):
    print('This function takes in parameters of two types\n')
    print('This is a number ' + str(number))
    print('This is a string ' + string)


#main program
firstFunc()
secondFunc(7,'Nazhim')
