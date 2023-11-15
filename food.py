import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(r_x, r_y)

    def refresh(self):
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(r_x, r_y)
