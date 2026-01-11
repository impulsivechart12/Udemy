from turtle import Screen
from snake_class import Snake
from snake_food import Food
from snake_scoreboard import Scoreboard
import time

snake_squares = []
new_snake = Snake()
food = Food()
score = Scoreboard()
game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(new_snake.up,  "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move_snake()

    #Detect collision with food
    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        score.increase_score()

    #Detect collision with wall.
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280 or new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    #Detect collision with tail.
    for segment in new_snake.snake_squares[1:]:
        if new_snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()