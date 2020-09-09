import society
import turtle

for i in range(0,20):
    society.Person()
wn = turtle.Screen()
wn.bgcolor("black")
turtle_exist=[]

for i in society.Person.whole_society:
    turtle_exist.append(turtle.Turtle())

for i in turtle_exist:
    i.color("white")
    i.shape("circle")
    i.shapesize(0.3)
    i.penup()
    i.speed("fastest")

for j in range(0,100):

    for i in range(0,len(turtle_exist)):
        turtle_exist[i].setx(society.Person.whole_society[i].x_locate-650)
        turtle_exist[i].sety(society.Person.whole_society[i].y_locate-350)
       


    society.Person.move_one_step()

#delay = raw_input("sdsads")

