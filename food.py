from turtle import Turtle
import random as rand
MIN= -280
MAX=280
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')


    def refresh(self):
        rand_x = rand.randint(MIN, MAX)
        rand_y=rand.randint(MIN, MAX)
        self.goto(rand_x, rand_y)

