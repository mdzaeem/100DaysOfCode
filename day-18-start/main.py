import turtle
from turtle import Turtle, Screen

tim = Turtle()
# Square
# tim.shape("turtle")
# tim.forward(200)
# tim.color("red")
# tim.left(90)
# tim.color("blue")
# tim.forward(200)
# tim.left(90)
# tim.color("yellow")
# tim.forward(200)
# tim.left(90)
# tim.color("green")
# tim.forward(200)

#dashed lines
# for i in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

#shapes

import random
colors = ['Coral', 'Teal', 'Indigo', 'Lime', 'Orchid', 'Turquoise', 'Crimson', 'Gold', 'SlateBlue', 'Salmon']
#
# tim.forward(100)
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     for j in range(i):
#         x=360/i
#         tim.right(x)
#         tim.forward(100)
#     # tim.forward(100)

#Snake Line
# turtle.colormode(255)
# lis=[180, 90, 270, 0]
# x = 4
#
# tim.speed(speed="fast")
# for i in range(100):
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tim.forward(30)
#     tim.setheading(random.choice(lis))
#     tim.pencolor((r, g, b))
#     # tim.color(random.choice(colors))
#     tim.pensize(width=x)
#     x += 0.1

#Circles
tim.speed(speed="fastest")
for i in range(600):
    tim.circle(70)
    tim.right(5)

screen = Screen()
screen.exitonclick()