from turtle import Turtle as t, Screen


# create a new turtle object
tim = t()
tim.shape('turtle')
tim.color('green')

# draw a dashed line
for _ in range(5):
    tim.forward(10)
    tim.up()
    tim.forward(10)
    tim.down()


my_screen = Screen()
my_screen.exitonclick()
