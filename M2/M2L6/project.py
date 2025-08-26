print("Hello ! \nWe are making a square . \nThe yellow square is all we need .\nRest are added for a bit beautifulness\nPresenting it .. ( May take some time ... COMLETED )")

import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")
pen = turtle.Turtle()
pen.speed(10)

pen.penup()
pen.color("white")
for _ in range(50):
    x = random.randint(-380, 380)
    y = random.randint(100, 280)
    pen.goto(x, y)
    pen.dot(random.randint(2, 6))

pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.color("darkgreen")
pen.begin_fill()
for _ in range(2):
    pen.forward(800)
    pen.right(90)
    pen.forward(200)
    pen.right(90)
pen.end_fill()

pen.penup()
pen.goto(200, 150)
pen.pendown()
pen.color("white")
pen.begin_fill()
pen.circle(50)
pen.end_fill()

pen.penup()
pen.goto(-400, -100)
pen.pendown()
pen.color("dimgray")
pen.begin_fill()
pen.goto(-250, 150)
pen.goto(-100, -100)
pen.goto(-400, -100)
pen.end_fill()

pen.penup()
pen.goto(-150, -100)
pen.pendown()
pen.color("gray")
pen.begin_fill()
pen.goto(50, 200)
pen.goto(250, -100)
pen.goto(-150, -100)
pen.end_fill()

pen.penup()
pen.goto(100, -100)
pen.pendown()
pen.color("dimgray")
pen.begin_fill()
pen.goto(300, 120)
pen.goto(500, -100)
pen.goto(100, -100)
pen.end_fill()

pen.penup()
pen.goto(-50, -100)
pen.pendown()
pen.color("Yellow")
pen.begin_fill()
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()

turtle.done()
