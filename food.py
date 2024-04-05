from turtle import Turtle
import random


class Food(Turtle):
    # Initializer
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.go_random()

    # Method to create a random position and placing the food
    def go_random(self):
        random_location = (random.randint(-360, 360), random.randint(-360, 360))
        self.goto(random_location)
