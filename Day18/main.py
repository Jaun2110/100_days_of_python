#immport turtle package and create turtle object

from turtle import Turtle, Screen

# new turtle object
tim = Turtle()
tim.shape('turtle')
tim.color('green')

#draw a  square
# timmy_my_turtle.right(90)
# timmy_my_turtle.forward(100)
# timmy_my_turtle.right(90)
# timmy_my_turtle.forward(100)
# timmy_my_turtle.right(90)
# timmy_my_turtle.forward(100)
# timmy_my_turtle.right(90)
# timmy_my_turtle.forward(100)

#istructions above represented with for loop
for _ in range(4):
    tim.right(90)
    tim.forward(100)


my_screen = Screen()

my_screen.exitonclick()