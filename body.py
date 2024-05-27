from turtle import Screen, Turtle
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Feed me unless I will eat you!!!")
screen.tracer(0)

segments=[]

for i in range(3):

    bodyPart1 = Turtle(shape="square")
    bodyPart1.penup()
    bodyPart1.color("white")
    bodyPart1.goto(0+(i*-20), 0)
    segments.append(bodyPart1)

is_game_on=True

while is_game_on:
    time.sleep(0.1)
    screen.update()

    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)

    segments[0].forward(20)
    segments[0].left(90)
screen.exitonclick
