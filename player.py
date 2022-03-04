STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def moveforward(self):
        self.forward(MOVE_DISTANCE)

    def check_reached_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            print("reached finish line")
            self.goto(STARTING_POSITION)
            return True