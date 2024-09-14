from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(100)
t.penup()
t.left(90)

colors = ['red','blue','pink','yellow','brown','purple','black','green','orange','gray',]
for e in range(10):
    for i in range(5):
        for x in range(5):
            t.color(colors[e])
            t.pendown()
            t.forward(20)
            t.right(72)
        t.penup()
        t.forward(40)
        t.right(72)
    t.forward(80)
    t.right(36)

t.forward(400)
