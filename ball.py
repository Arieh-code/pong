from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        directions = ["up_right", "down_right", "up_left", "down_left"]
        self.direction = random.choice(directions)

    def move(self):
        if self.direction is "up_right":
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
        elif self.direction is "down_right":
            new_x = self.xcor() + 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)
        elif self.direction is "up_left":
            new_x = self.xcor() - 10
            new_y = self.ycor() + 10
            self.goto(new_x, new_y)
        elif self.direction is "down_left":
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(new_x, new_y)

    def bounce(self):
        if self.direction is "up_right":
            self.direction = "down_right"
            self.move()
        elif self.direction is "down_right":
            self.direction = "up_right"
            self.move()
        elif self.direction is "up_left":
            self.direction = "down_left"
            self.move()
        elif self.direction is "down_left":
            self.direction = "up_left"
            self.move()
