import random
from turtle import Turtle as t , Screen

timmy = t()
my_screen = Screen()
my_screen.colormode(255)

walking_directions = [0, 90, 180, 270]
walk_distance = 20
timmy.width(10)
timmy.speed(0)


def random_color():
       # generate a color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


def walk(distance):
    timmy.color(random_color())
    timmy.setheading(random.choice(walking_directions))
    timmy.forward(distance)


for i in range(1, 300):
    walk(walk_distance)

my_screen.exitonclick()
