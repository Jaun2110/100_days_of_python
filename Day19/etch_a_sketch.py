from turtle import Turtle, Screen

# create turtle and screen objects
tom = Turtle()
tom.speed(0)
screen1 = Screen()
# attach event listener to the screen
screen1.listen()


def move_forwards():
    """moves tom forwards when w is pressed"""
    tom.forward(10)


def move_backwards():
    """moves tom back when s is pressed"""
    tom.backward(10)


def counter_clockwise():
    """turn tom counterclockwise"""
    current_heading = tom.heading()
    tom.setheading(current_heading + 10)


def clockwise():
    """turn tom counterclockwise"""
    current_heading = tom.heading()
    tom.setheading(current_heading - 10)


def clear_screen():
    tom.up()
    tom.clear()
    tom.home()
    tom.down()


screen1.onkey(key="a", fun=counter_clockwise)
screen1.onkey(key="d", fun=clockwise)
screen1.onkey(key="s", fun=move_backwards)
screen1.onkey(key="w", fun=move_forwards)
screen1.onkey(key="c", fun=clear_screen)
screen1.exitonclick()
