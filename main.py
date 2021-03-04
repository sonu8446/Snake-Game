from snake import Snake
from food import Food
from turtle import Screen
import time
screen = Screen()
screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
score = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        score += 1
        food.refresh()
        snake.add_tail()



screen.exitonclick()
