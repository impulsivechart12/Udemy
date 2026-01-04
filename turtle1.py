
import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
screen = Screen()
timmy.speed("fastest")
timmy.shape("turtle")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


list_directions = [0, 90, 180, 270 ]
timmy.speed(5)
timmy.pensize(1)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()