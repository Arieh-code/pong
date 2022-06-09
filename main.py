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

    if ball.xcor() == 280 or ball.xcor() == -280:
        ball.bounce()


screen.exitonclick()
