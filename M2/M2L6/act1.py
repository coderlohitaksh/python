#SPIRAL PATTERN

import turtle
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Turtle")
pen = turtle.Turtle()
size = 0

while True :
    for i in range (4):
        pen.fd ( size + 1 )
        pen.left ( 90 )
        size = size - 5
        size = size + 1