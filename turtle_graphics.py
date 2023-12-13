import turtle
from prettytable import PrettyTable
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.color('brown3')
# timmy.shape("turtle")
# timmy.forward(500)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


table = PrettyTable()
table.field_names = ["Pokemon", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
    ]
)

table.align = 'c'

print(table)