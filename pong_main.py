from turtle import Screen
from pong_paddle_class import Paddle
from pong_ball_class import Ball
import time
from pong_scoreboard_class import Scoreboard

game_is_on = True
sleep_time = 0.1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    ball.move()

    #detect ceiling and floor collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()

    #detect if ball has moved passed right paddle
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.increase_left_score()
        scoreboard.update_scoreboard()

    # detect if ball has moved passed left paddle
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.increase_right_score()
        scoreboard.update_scoreboard()




screen.exitonclick()