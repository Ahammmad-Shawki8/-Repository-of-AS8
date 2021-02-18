# turtle library

# turtle graphics is basically nice and easy tool that allows us to make fun little animation with coding.
# first we need to import turtle. and we always need to end our turtle by done() method.
import turtle

# making a Turtle object.
a=turtle.Turtle()

# Task 1
# making a line

# to move the pen forward
a.forward(100) # this take how many unit we want to forward as an argument.
a.backward(200)
# rotate the pen
a.right(45) # this takes how many degrees we want to rotate right as an argument.
a.left(360)
# we can see more optioons in official tutle documentation.
"""https://docs.python.org/3.8/library/turtle.html?highlight=turtle#turtle.right"""


# Task 2
# making shape

# changing pen color
a.color("cyan")
# turtle have some difinite amount of color.
# but if we want to use some shade of any color, then
# we can go to google and search online color wheel. their we need to choose our specific color shade.
# they will give us a hex color value. and we can use that in our color() method too.
a.color("#3C9118")
# it also accepts rgb values.


# now we need to fill the shape inside with a color.
# we have two function called begin_fill() and end_fill()

# if we want outline color and fill color different. then we can pass another color in the color() function.
a.color("black","cyan")

a.begin_fill()
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.end_fill()

# lets say we want to make another square in different location.
# we can see that the pen is continuous.
# in order to get spaces between our shapes we can use penup() and pendown() function.
a.penup()
a.forward(50)
a.pendown()

a.color("black","magenta")
a.begin_fill()
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.left(90)
a.forward(100)
a.end_fill()

# we can also use setheading() method to change the pen direction.
# it has no relation with pens current position and rotation.
# it is mostly like a quardent system.

# Task 3
# making a Flower

# we can change the speed using speed() function.
a.speed(15)

a.color("red","orange")
a.begin_fill()
for i in range(36):
    a.forward(300)
    a.left(170)
a.end_fill()

# Task 4
# from this color code, we can make some complex design using some math functions.

# first we need to import math libary.
import math

a.speed(3000)

a.color("black")
for i in range(2000):
    a.forward(math.sqrt(i))
    a.left(i%180)

for i in range(4000):
    a.forward(10)
    a.left(math.sin(i/10)*25)
    a.left(20)

# we can also use the random library
import random
# and play around with it.

# Task 5
# Star design

# we can channge the background color with bgcolor() function.
# first we have to get the screen using getscreen() method and then use the bgcolor() method.
a.getscreen().bgcolor("#994444")

a.penup()
# we can also use goto() function.
# it takes a tuple of cartessian coordinates as an argument.
a.goto((-200,100))
a.pendown()

a.speed(50)

def star(a,s):
    for i in range(5):
        if s<=10:
            break
        else:
            a.forward(s)
            star(a,s/3)
            a.left(216)
        i=i

star(a,365)

# note that, whenever we have a recursive function we need to put an if-else case.
# unless it will give us a recursion error.



# this will hold the title graphics box even after the pen has done this work. 
turtle.done()