import turtle

wn = turtle.Screen()
wn.title("my Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# paddle functions
def pa_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def pa_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def pb_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def pb_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(pa_up, "w")
wn.onkeypress(pa_down, "s")
wn.onkeypress(pb_up, "i")
wn.onkeypress(pb_down, "k")


while True:
    wn.update()
