import turtle
import math

#turtle.tracer(0,0)

t=turtle.Turtle()
t.shape("turtle")
t.speed(5)


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

"""
Drawing a spiral with arc
for i in range(10,0,-1):
    arc(i*10,270)
"""

def jump(length):
    t.penup()
    t.forward(length)
    t.pendown()

#P1 Defined using parallelogram below

def rectangle(wide, tall):
    for i in range(2):
        t.forward(wide)
        t.left(90)
        t.forward(tall)
        t.left(90)


#P2 Defined using parallelogram below

def rhombus(lenght, angle):
    for i in range(2):
        t.forward(lenght)
        t.left(angle)
        t.forward(lenght)
        t.left(180-angle)

#P3

def parallelogram(side_1, side_2, angle):
    for i in range(2):
        t.forward(side_1)
        t.left(angle)
        t.forward(side_2)
        t.left(180-angle)

def rectangle_2(side_1, side_2):
    parallelogram(side_1, side_2, 90)

def rhombus_2(side, angle):
    side_1 = side
    side_2 = side
    parallelogram(side_1, side_2, angle)

#P4

def triangle(side_1, angle):
    side_2= side_1 * (math.sqrt(2*(1-math.cos(math.radians(angle)))))
    #side_2=abs(2*side_1 * math.cos(angle))
    #side_2 = math.sqrt(2*(side_1**2)-(2*(side_1**2) * math.cos(angle)))
    angle_2 = (180-angle)/2
    t.forward(side_1)
    t.left(180-angle_2)
    t.forward(side_2)
    t.left(180-angle_2)
    t.forward(side_1)
    t.left(180)

def draw_pie(n):
    side_1=100
    angle = 360/n
    for i in range(n):
        triangle(side_1, angle)

#P5

def polyline_r(n, length, angle):
    for i in range(n):
        t.forward(length)
        t.right(angle)

def arc_2(radius, angle):
    arc_length = 2 * math.pi * radius * angle /360
    n=30
    length=arc_length/n
    step_angle=angle/n
    polyline_r(n, length, step_angle)

def petal(radius, angle):
    arc(radius, angle)
    t.left(180-angle)
    arc(radius, angle)
    t.left(180)

    # t.penup()
    # t.goto(0,0)
    # t.pendown()
    # arc_2(radius, angle)
    # t.penup()
    # t.goto(0, 0)
    # t.pendown()

# for i in range(4):
#     petal(100,45)
#     t.left(90)

def flower(radius, angle, n):
    for i in range(n):
        petal(radius, angle)


flower(150, 90, 5)

#petal(200,35)

# angle=60
# arc(100, angle)
# t.left(180-angle)
# arc(100, angle)

turtle.update()
turtle.done()