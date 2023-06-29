from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score: {self.score} ", align="center", font=('Arial', 24, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=('Arial', 24, 'normal'))


    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.increase_score()


    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"GAME OVER", align="center", font=('Arial', 24, 'normal'))
