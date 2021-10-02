from turtle import Turtle
from tkinter import *

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_over
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score:{self.high_score}", align="center", font=("Courier", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def score_reset(self):
        window = Tk()

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()