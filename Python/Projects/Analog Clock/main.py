import turtle
import time
import datetime
window = turtle.Screen()
window.bgcolor("white")
window.setup(width=800, height=600)
window.title("Analog Clock by Naveen")
window.tracer(0)


# pen to draw on the screen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)


def clock(h, m, s, pen):
    # draw the clock
    pen.up()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("black")
    pen.pendown()
    pen.circle(210)

    # draw line for hours
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # draw hour hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('black')
    pen.setheading(90)
    angle = 30*h+m/2+s/120
    pen.rt(angle)
    pen.pendown()
    pen.fd(100)

    # draw the minute hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('black')
    pen.setheading(90)
    angle = 6*m+s/10
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)

    # draw the second hand
    pen.penup()
    pen.goto(0, 0)
    pen.color('black')
    pen.setheading(90)
    angle = 6*s
    pen.rt(angle)
    pen.pendown()
    pen.fd(50)


while True:

    # h = int(time.strftime("%I"))
    # m = int(time.strftime("%M"))
    # s = int(time.strftime("%s"))

    h = datetime.datetime.now().hour
    m = datetime.datetime.now().minute
    s = datetime.datetime.now().second

    clock(h, m, s, pen)
    window.update()
    # time.sleep(1)

    pen.clear()
window.mainloop()
