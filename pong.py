import turtle
import os
wn = turtle.Screen()
wn.title("Pong by @ToykyoEdTech")
wn.bgcolor("purple")
wn.setup(width=800, height=600)
wn.tracer(0)


# score
score_a = 0
score_b = 0


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
ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center",
          font=("courier", 24, "normal"))


# funtion

# left paddle
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Right Paddle


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

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    # Bottom Border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")
    # Right Border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))
    # Left Border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                  font=("courier", 24, "normal"))
    # Paddle and Ball collisions
    # Right Paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
    # Left Paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
