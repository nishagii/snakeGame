from turtle import Screen, Turtle

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.bgcolor("black")
screen.title("Feed me unless I will eat you!!!")


for i in range(3):

    bodyPart1 = Turtle(shape="square")
    bodyPart1.color("white")
    bodyPart1.goto(0+(i*-20), 0)

print(screen)

screen.exitonclick()
