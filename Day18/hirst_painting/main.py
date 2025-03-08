import colorgram
from turtle import Turtle, Screen
import random

# my_screen.screensize(900,900)

# colors_in_picture = colorgram.extract('hirst_colors.jpeg', 10)
# # store the rgb in a list of tuples
# color_list = []
# for color in colors_in_picture:
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     color_list.append(color_tuple)
#
# print(color_list)

tim = Turtle()
my_screen = Screen()
my_screen.title("Million Dollar Painting")
my_screen.colormode(255)

color_list = [(32, 96, 183), (232, 165, 86), (108, 190, 228), (217, 71, 108), (203, 71, 19)]


def draw_row(y_coordinate):
    for row_distance in range(-300, 200, 50):

        tim.teleport(row_distance, y_coordinate)
        tim.dot(20, random.choice(color_list))
    # painting size = rows: 10 columns: 10

tim.hideturtle()
for columns in range(-300, 250, 50):
    draw_row(columns)



my_screen.exitonclick()
