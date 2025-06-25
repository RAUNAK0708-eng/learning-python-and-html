
import turtle
import random

# from snake import Snake

POSITION = (range(-300 , 300))
POS_X = random.choice(POSITION)
POS_Y = random.choice(POSITION)
# snake = Snake()
FOOD_POSITI0N= (POS_X ,POS_Y)
print(FOOD_POSITI0N)



class Food:
    def __init__(self):


        self.food = turtle.Turtle()
        self.food.shape("circle")
        self.food.color("yellow")
        self.food.penup()
        self.food.shapesize(stretch_len=0.5 , stretch_wid=0.5)
        self.food.goto(FOOD_POSITI0N)


    def new_food(self):
        position = (range(-300, 300))
        pos_x = random.choice(position)
        pos_y = random.choice(position)


        self.food.goto(pos_x , pos_y)





