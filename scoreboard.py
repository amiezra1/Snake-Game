from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Couriel", 24, "normal")

class Scoreboard(Turtle):
  
  def __init__(self) -> None:
    super().__init__()
    self.score = 0
    self.color("white")
    self.penup()
    self.goto(0, 260)
    self.hideturtle()
    self.updateScore()
  
  def updateScore(self):
    self.write(f"Scor: {self.score}", align = ALIGNMENT, font = FONT)

  def setScore(self):
    self.score += 1
    self.clear()
    self.updateScore()