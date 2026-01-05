import turtle as t
import random

rgb_colors = [(240, 246, 243), (133, 164, 202), (225, 150, 101),
       (30, 43, 64), (201, 136, 148), (163, 59, 49), (236, 212, 88), (44, 101, 147), (136, 181, 161), (148, 64, 72),
       (51, 41, 45), (161, 32, 29), (60, 115, 99), (59, 48, 45), (170, 29, 32), (215, 83, 73), (236, 167, 157),
       (230, 163, 168), (36, 61, 55), (15, 96, 71), (33, 60, 106), (172, 188, 219), (194, 99, 108), (106, 126, 158),
       (18, 83, 105), (175, 200, 188), (35, 150, 209)]

# screen actions
screen=t.Screen()
screen.setup(width=500, height=500)

# turtle actions
t.colormode(255)
timmy=t.Turtle()
timmy.shape("turtle")
timmy.hideturtle()
timmy.penup()
timmy.speed("slow")
timmy.setx(-200)
timmy.sety(-200)
starting_y = -200

for _ in range(1 , 101):

    timmy.dot(10, random.choice(rgb_colors))
    timmy.forward(40)
    if _ % 10 == 0:
        starting_y = starting_y + 40

        timmy.sety(starting_y)
        timmy.setx(-200)