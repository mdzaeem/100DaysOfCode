from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

#zaeem

def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def right_angel():
    tim.right(10)


def left_angel():
    tim.left(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "Up",)
screen.onkey(move_backward, "Down",)
screen.onkey(left_angel, "Left")
screen.onkey(right_angel, "Right")
screen.onkey(clear, "c")
screen.exitonclick()