import turtle
s=turtle.getscreen()
s.title("Moving Turtle Like a Fan ")
t1=turtle.Turtle()
t1.pencolor("yellow")
t1.shape("turtle")
t1.shapesize(10,10,10)
for angle in range(0,901,90):
    t1.left(angle)
