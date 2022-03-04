FONT = ("Courier", 24, "normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-250, 260)
        self.write(f"Level: {self.level}", False, align="left", font=FONT)
        self.hideturtle()

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)