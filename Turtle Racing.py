from turtle import *
from random import *
import turtle
import time


#setting up the screen
setup(800,500)
title("Turtle Racing!")
bgcolor("blue")
speed(0)

#heading
penup()
goto(-100,205)
color("white")
write("Turtle Race",font=("Arial", 20, "bold"))

#Dirt
goto(-350,200)
pendown()
color("chocolate")
begin_fill()
for x in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

#finish line
gap_size = 20
shape("square")
penup()

#white squares row
color("white")
for x in range(10):
    goto(250,(170-(x*gap_size*2)))
    stamp()

for x in range(10):
    goto(250 + gap_size,((210-gap_size)-(x*gap_size*2)))
    stamp()

#black squares
color("black")
for x in range(10):
    goto(250,(190-(x*gap_size*2)))
    stamp()

for x in range(10):
    goto(251+gap_size,((190-gap_size)-(x*gap_size*2)))
    stamp()

# TURTLE 1 - blue
blue_turtle = Turtle()
blue_turtle.color("cyan")
blue_turtle.shape("turtle")
blue_turtle.shapesize(1.5)
blue_turtle.penup()
blue_turtle.goto(-300,150)
blue_turtle.pendown()

# TURTLE 2 - pink
pink_turtle = Turtle()
pink_turtle.color("magenta")
pink_turtle.shape("turtle")
pink_turtle.shapesize(1.5)
pink_turtle.penup()
pink_turtle.goto(-300,50)
pink_turtle.pendown()


# TURTLE 3 - yellow
yellow_turtle = Turtle()
yellow_turtle.color("yellow")
yellow_turtle.shape("turtle")
yellow_turtle.shapesize(1.5)
yellow_turtle.penup()
yellow_turtle.goto(-300,-50)
yellow_turtle.pendown()



# TURTLE 4 - green
green_turtle = Turtle()
green_turtle.color("green")
green_turtle.shape("turtle")
green_turtle.shapesize(1.5)
green_turtle.penup()
green_turtle.goto(-300,-150)
green_turtle.pendown()


#pause 1 sec before starting
time.sleep(1)

#move turtles
while blue_turtle.xcor()<=230 and pink_turtle.xcor()<=230 and yellow_turtle.xcor()<=230 and green_turtle.xcor()<=230:
    blue_turtle.forward(randint(1,10))
    pink_turtle.forward(randint(1,10))
    yellow_turtle.forward(randint(1,10))
    green_turtle.forward(randint(1,10))

#who is the winner

if blue_turtle.xcor() > pink_turtle.xcor()and blue_turtle.xcor() > yellow_turtle.xcor()and blue_turtle.xcor() > green_turtle.xcor():
    print("Blue turtle wins")
    for x in range(72):
        blue_turtle.right(5)
        blue_turtle.shapesize(2.5)
    
elif pink_turtle.xcor() > blue_turtle.xcor()and pink_turtle.xcor() > yellow_turtle.xcor()and pink_turtle.xcor() > green_turtle.xcor():
    print("pink turtle wins")
    for x in range(72):
        pink_turtle.right(5)
        pink_turtle.shapesize(2.5)

elif yellow_turtle.xcor() > blue_turtle.xcor()and yellow_turtle.xcor() > pink_turtle.xcor()and yellow_turtle.xcor() > green_turtle.xcor():
    print("Blue turtle wins")
    for x in range(72):
        yellow_turtle.right(5)
        yellow_turtle.shapesize(2.5)
else:
    print("green turtle wins")
    for x in range(72):
        green_turtle.right(5)
        green_turtle.shapesize(2.5)
