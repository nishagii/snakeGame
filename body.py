from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Feed me unless I will eat you!!!")
snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.tracer(0)
# used to turn turtle animation on or off and set a delay for update drawings


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    snake.move()


screen.exitonclick()
