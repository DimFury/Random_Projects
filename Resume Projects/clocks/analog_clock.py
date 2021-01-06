from turtle import *
import turtle
import time
app = turtle.Screen()
app.bgcolor("black")
app.setup(width=600, height=600)
app.title("Analogue Clock")
app.tracer(0)
# Create the drawing pen
go = turtle.Turtle()
go.hideturtle()
go.speed(0)
go.pensize(3)

def draw_clock(hr, mn, sec, go):
    go.up()
    go.goto(0, 210)
    go.setheading(180)
    go.color("green")
    go.pendown()
    go.circle(210)
    go.up()
    go.goto(0, 0)
    go.setheading(90)
    for _ in range(12):
        go.fd(190)
        go.pendown()
        go.fd(20)
        go.penup()
        go.goto(0, 0)
        go.rt(30)
    hands = [("green", 80, 12), ("white", 150, 60), ("white", 110, 60)]
    time_set = (hr, mn, sec)
    for hand in hands:
        time_part = time_set[hands.index(hand)]
        angle = (time_part/hand[2])*360
        go.penup()
        go.goto(0, 0)
        go.color(hand[0])
        go.setheading(90)
        go.rt(angle)
        go.pendown()
        go.fd(hand[1])
while True:
    hr = int(time.strftime("%I"))
    mn = int(time.strftime("%M"))
    sec = int(time.strftime("%S"))
    draw_clock(hr, mn, sec, go)
    app.update()
    time.sleep(1)
    go.clear()
app.mainloop()