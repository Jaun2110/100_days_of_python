from turtle import Turtle, Screen
import random

# setup the screen
screen = Screen()
screen.setup(width=500, height=400)
race_on = False
# popup for user guess
user_guess = screen.textinput("Place your bet", "Enter the color of the turtle\nthat you think will win:").lower()


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y coordinates for each turtle
y_coordinates = [120, 70, 20, -30, -80, -130]
all_turtles = []

# loop to create turtles
for index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_coordinates[index])
    all_turtles.append(new_turtle)


if user_guess:
    race_on = True


while race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
#             check if user chose the color that won
            if user_guess.lower() == winning_color:
                print(f"Your turtle won! The {winning_color} turtle is the winner!")

            else:
                print(f"You Lose! The {winning_color} turtle won the race!")

            race_on = False


screen.exitonclick()
