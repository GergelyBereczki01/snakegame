from turtle import Turtle
import random

SIZE_OF_SCREEN = 600
EDGE_OF_SCREEN = int((SIZE_OF_SCREEN - 40) / 2)


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(EDGE_OF_SCREEN * -1, EDGE_OF_SCREEN)
        y = random.randint(EDGE_OF_SCREEN * -1, EDGE_OF_SCREEN)
        self.goto(x, y)
