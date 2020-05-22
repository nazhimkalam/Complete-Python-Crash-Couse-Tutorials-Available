import turtle

def square(myturtle,length):
    try:
        angle = 0
        while(True):
            myturtle.right(angle)
            for i in range(4):
                myturtle.forward(length)
                myturtle.right(90)
            angle+=0.5
            
    except:
        print('Thanks for using python version 3.8')

def triangle(myturtle,length):
    try:
        angle = 0
        while(True):
            myturtle.right(angle)
            for i in range(4):
                myturtle.right(45)
                myturtle.forward(length)
                myturtle.right(90)
                myturtle.forward(length)
                myturtle.right(135)
                myturtle.forward(length)
                myturtle.right(135)
                myturtle.forward(length)
                myturtle.left(90)
            angle+=0.5
            
    except:
        print('Thanks for using python version 3.8')

#main program
myturtle = turtle.Turtle() #we call the functions of turtle
myturtle.speed(0)
triangle(myturtle,100)
