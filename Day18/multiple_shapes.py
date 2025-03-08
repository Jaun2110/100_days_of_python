from turtle import Turtle as t , Screen
import random

my_screen = Screen()
my_screen.colormode(255)
tim = t()
# draw from triangle to decagon
# for each shape
side_length = 100


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(side_length)
        tim.right(angle)


for i in range(3, 11):
    #  get random integer to represent the rgb numbers
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tim.color(r, g, b)
    draw_shape(i)


my_screen.exitonclick()
