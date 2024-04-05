from turtle import Turtle

# Constant variables
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    # Initializer
    def __init__(self):
        self.snake_body = []
        self.create_body()
        self.head = self.snake_body[0]

    # Method to create the initial body of the snake (3 parts)
    def create_body(self):
        for i in INITIAL_POSITIONS:
            self.create_part(i)

    # Method to create a single part of body and putting it at the position of the previous last part
    def create_part(self, position):
        square = Turtle(shape="square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.snake_body.append(square)

    # Method to give the previous last position to create a new part
    def increase_body(self):
        self.create_part(self.snake_body[-1].position())

    # Method to delete the previous snake and initialize it again
    def reset_snake(self):
        for i in self.snake_body:
            i.goto(1000, 1000)

        self.snake_body.clear()
        self.create_body()
        self.head = self.snake_body[0]

    # Method to move all the body parts to their next position
    def move(self):
        # range(start=, finish=, step=)
        for j in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[j].goto(self.snake_body[j - 1].position())
        self.head.forward(MOVE_DISTANCE)

    # Methods to change directions
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
