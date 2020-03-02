import turtle
wn = turtle.Screen()
wn.title("Pong by @ToykyoEdTech")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a = turtle.Turtle()  # name
paddle_a.speed(0)  # speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)  # where paddle starts


# Paddle B
paddle_b = turtle.Turtle()  # name
paddle_b.speed(0)  # speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)  # where paddle starts

# Ball
ball = turtle.Turtle()  # name
ball.speed(0)  # speed of animation
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)  # where ball starts


# funtion


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()  # linsten for keyboard inpput
wn.onkeypress(paddle_a_up, "w")  # when "w" is pressed call funtion y
wn.onkeypress(paddle_a_down, "s")  # when "s" is pressed call funtion y
wn.onkeypress(paddle_b_up, "Up")  # when "up" is pressed call funtion y
wn.onkeypress(paddle_b_down, "Down")  # when "down" is pressed call funtion y

# Main game loop
while True:
    wn.update()
