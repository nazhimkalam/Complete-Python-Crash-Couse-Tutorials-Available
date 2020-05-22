import turtle
def square(turtle):
    for i in range (4):
        turtle.forward(100)
        turtle.right(90)
        
def rectangle(turtle):
    for i in range (2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)

def triangle(turtle):
    turtle.right(45)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(145)
    turtle.right(135)
    turtle.forward(110)
def maze(turtle):
    distance = 5
    extra = 5
    try: 
        while(True):
            turtle.forward(distance + extra)
            turtle.right(90)
            extra += 5
    except:
        print('Thanks for using turtle')

def rose(turtle):
    distance = 1
    extra = 1
    try: 
        while(True):
            turtle.forward(distance + extra)
            turtle.right(50)
            extra += 1
    except:
        print('Thanks for using turtle')


#---main program

turtle = turtle.Turtle()
triangle(turtle)
