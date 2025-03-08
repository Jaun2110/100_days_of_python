from turtle import Turtle, Screen

jaun = Turtle()
screen = Screen()


def move_right():
    jaun.forward(10)


# attach event listener to screen

screen.listen()
screen.onkey(key="d", fun=move_right)


screen.exitonclick()
