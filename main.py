from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

spid_snake = 0.1
game_is_on = True
while game_is_on:
  screen.update()
  time.sleep(spid_snake)
  snake.move()

  #Detect collision with food
  if snake.getHead().distance(food)<20:
    food.foodLocation()
    snake.extend()
    scoreboard.setScore()

  #Detect collision with wall
  if snake.getHead().xcor() > 290 or snake.getHead().xcor() < -290 or snake.getHead().ycor() > 290 or snake.getHead().ycor() < -290:
    game_is_on = False
    scoreboard.gameOver()
  
  #Detect collision with tail
  for segment in snake.getSegments()[1:]:
    if snake.getHead().distance(segment) < 10:
      game_is_on = False
      scoreboard.gameOver()











screen.exitonclick()