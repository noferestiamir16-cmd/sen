import turtle
t=turtle.Turtle()
def mycircle(red,green,blue):
    t.color(red,green,blue)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
mycircle(1,0,0)
def mymorabae(size):
    for i in range(4):
        t.forward(size)
        t.right(90)

mymorabae(150)
