import turtle

window = turtle.Screen()
window.bgcolor("black")

painter = turtle.Turtle()
painter.fillcolor('skyblue')
painter.pencolor('skyblue')
painter.pensize(3)

def drawsq(t, s):
    for i in range(4):
        t.forward(s)
        t.left(90)

for i in range(1,180):
    painter.left(18)
    drawsq(painter, 200)
