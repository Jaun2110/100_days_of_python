# import Turtle and screen classes
from turtle import Turtle, Screen

#create a new turtle object from the Turtle class
timmy = Turtle()
#change timmy's shape
timmy.shape("turtle")
# change timmy's color
timmy.color("green")
timmy.forward(100)
# create a new screen object
screen1 = Screen()
# method is a function tied to an object

# method that closes screen onclick
screen1.exitonclick()

