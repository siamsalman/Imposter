import turtle

body_color = 'red'
glass_color = '#9acedc'

screen = turtle.getscreen()
imp = turtle.Turtle()

def body():
    imp.pensize(18)
    imp.fillcolor(body_color)
    imp.begin_fill()
    imp.right(90)
    imp.forward(50)
    imp.right(180)
    imp.circle(40, -180)
    imp.right(180)
    imp.forward(200)

    imp.right(180)
    imp.circle(100, -180)

    imp.backward(20)
    imp.left(15)
    imp.circle(500, -20)
    imp.backward(15)

    imp.circle(40, -180)
    imp.left(7)
    imp.backward(50)

    imp.up()
    imp.left(90)
    imp.forward(10)
    imp.right(90)
    imp.down()

    imp.right(240)
    imp.circle(50, -70)

    imp.end_fill()

def glass():
    imp.up()
    imp.right(230)
    imp.forward(100)
    imp.left(90)
    imp.forward(20)
    imp.right(90)

    imp.down()
    imp.fillcolor(glass_color)
    imp.begin_fill()

    imp.right(150)
    imp.circle(90,-55)

    imp.right(180)
    imp.forward(1)
    imp.right(180)
    imp.circle(10, -65)
    imp.right(180)
    imp.forward(110)
    imp.right(180)

    imp.circle(50, -190)
    imp.right(170)
    imp.forward(80)

    imp.right(180)
    imp.circle(40, -30)

    imp.end_fill()

def backpack():
    imp.up()
    imp.right(60)
    imp.forward(100)
    imp.right(90)
    imp.forward(75)

    imp.fillcolor(body_color)
    imp.begin_fill()

    imp.down()
    imp.forward(30)
    imp.right(255)

    imp.circle(300, -30)
    imp.right(260)
    imp.forward(30)

    imp.end_fill()

body()
glass()
backpack()


imp.screen.exitonclick()
