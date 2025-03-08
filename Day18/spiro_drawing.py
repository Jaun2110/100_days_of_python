from turtle import Turtle, Screen
import random
my_screen = Screen()
my_screen.colormode(255)

tim = Turtle()
tim.speed(0)

def random_color():
       # generate a color
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


def draw_spiro(gap_size):

    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(150)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)


draw_spiro(2)

my_screen.exitonclick()
