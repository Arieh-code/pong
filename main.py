from turtle import Screen, Turtle
from paddle_right import PaddleRight
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(800, 600)
screen.tracer(0)

paddle1 = PaddleRight()

screen.listen()
screen.onkey(paddle1.up(), "Up")
screen.onkey(paddle1.down(), "Down")

game_is_on = True

while game_is_on:
    screen.update()


screen.exitonclick()
