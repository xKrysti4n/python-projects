from turtle import Turtle, Screen
t = Turtle()

for _ in range(4):
    t.forward(10)
    t.pu()
    t.forward(10)
    t.pd()
    t.right(90)


    
Screen().exitonclick()