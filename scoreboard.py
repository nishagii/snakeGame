from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updataScore()

    def updataScore(self):
        self.write(f"නයා කෑ​වා : {self.score} ​ක්", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updataScore()
