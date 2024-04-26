import colorgram
import turtle
import  turtle as turtle_module

tim = turtle_module.Turtle()

colors = colorgram.extract('image.jpg', 30)

firstcolour = colors
print(firstcolour)
colorList = []
tup = []
#Angela Yu's method
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color= (r, g, b)
#     colorList.append(new_color)
#what i did and alternate way
# for i in range(len(colors)):
#     tup.append(colors[i].rgb.r)
#     tup.append(colors[i].rgb.g)
#     tup.append(colors[i].rgb.b)
#     tupl = tuple(tup)
#     colorList.append(tupl)
#     tup = []
import random
turtle_module.colormode(255)
colorList = [(249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9), (248, 11, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61), (5, 38, 33), (67, 219, 155)]
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(220)
tim.forward(350)
tim.setheading(0)

def straightdot():
    tim.forward(-50)
    x=0
    while x != 10:
        tim.forward(50)
        tim.dot(20, random.choice(colorList))
        x += 1


flag = 1
for i in range(10):
    straightdot()
    tim.setheading(90)
    tim.forward(50)
    if flag == 1:
        tim.setheading(180)
        flag = 0
    else:
        tim.setheading(0)
        flag = 1






screen = turtle_module.Screen()
screen.exitonclick()





