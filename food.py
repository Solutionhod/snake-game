from turtle import Turtle
import random
SHAPE = ["circle", "triangle", "square"]
COLOR = ["red", "yellow", "blue", "purple", "indigo", "gold"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(SHAPE))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLOR))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(SHAPE))
        self.color(random.choice(COLOR))
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
