from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score

is_game_on = True

screen = Screen()
screen.tracer(0)
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Saap Ka Khel")
segment_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []
snake = Snake()

khanna = Food()
score_board = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food.
    if snake.head.distance(khanna) < 15 :
        khanna.refresh()
        snake.extend()
        score_board.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.score_reset()
        snake.reset_snake()

    # Detect collision with tail.
    for segment in snake.segment :
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.score_reset()
            snake.reset_snake()


screen.exitonclick()