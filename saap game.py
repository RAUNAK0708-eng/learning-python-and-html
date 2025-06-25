from turtle import   Screen
import time

from snake import Snake
from food import Food
screen=Screen()
screen.setup(height=680 , width=680)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
segment=[]
starting_position =[(0,0) , (-20,0) , (-40,0)]


snake=Snake()
food = Food()

screen.listen()

screen.onkey(snake.up,"w")
screen.onkey(snake.down,"s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()
    # detect collision with food
    if snake.head.distance(food) < 10:
        food.new_food()























screen.exitonclick()