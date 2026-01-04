import turtle
import math

#turtle.tracer(0,0)

t=turtle.Turtle()
t.shape("turtle")
t.speed(0)


# def polygon(sides, length):
#     for i in range(sides):
#         t.forward(length)
#         t.left(360/sides)

def polyline(n, length, angle):
    for i in range(n):
        t.forward(length)
        t.left(angle)

def polygon(n, length):
    angle = 360/n
    polyline(n, length, angle)

def arc(radius, angle):
    arc_length = 2 * math.pi * radius * angle /360
    n=30
    length=arc_length/n
    step_angle=angle/n
    polyline(n, length, step_angle)

def circle(radius):
    arc(radius, 360)

for i in range(10,0,-1):
    arc(i*10,270)


turtle.update()
turtle.done()