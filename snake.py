from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

  def __init__(self) -> None:
    self.segments = []
    self.createSnake()
    self.head = self.segments[0]
  
  def getHead(self):
    return self.head

  def getSegments(self):
    return self.segments
  
  def createSnake(self):
    for position in STARTING_POSITIONS:
      self.addSegment(position)
  
  def addSegment(self, position):
    new_segment=Turtle("square")
    if len(self.segments) == 0:
      new_segment.color("green")
    else:
      new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

  def extend(self):
    self.addSegment(self.segments[-1].position())

  def move(self):
    for segment_num in range(len(self.segments) - 1, 0 , -1):
      new_x = self.segments[segment_num - 1].xcor()
      new_y = self.segments[segment_num - 1].ycor()
      self.segments[segment_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
  
  def left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)

  def down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)

  def right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
  