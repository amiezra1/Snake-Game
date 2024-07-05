from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

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

  if snake.getHead().distance(food)<15:
    food.foodLocation()












screen.exitonclick()