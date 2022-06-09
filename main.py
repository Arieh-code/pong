from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle("right")
paddle_l = Paddle("left")

ball = Ball()

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
speed = 0.4
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce()

    if paddle_l.distance(ball) <= 10:
        ball.hit("left")
        speed -= 0.05

    if paddle_r.distance(ball) <= 10:
        ball.hit("right")
        speed -= 0.05

screen.exitonclick()
