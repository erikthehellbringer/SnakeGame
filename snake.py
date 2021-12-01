import turtle as t
import time
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP= 90
DOWN= 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]



    def create_snakes(self):
        for position in STARTING_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = t.Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.snakes.append(new_snake)
        # moves snake

    def add_one(self):
        self.add_snake(self.snakes[-1].position())

    def move(self):
        for snk_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snk_num - 1].xcor()
            new_y = self.snakes[snk_num - 1].ycor()
            self.snakes[snk_num].goto(new_x, new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)