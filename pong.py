import turtle
import random

game_speed = 2

wn = turtle.Screen()
wn.title("Pong by @t_hud_subi")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation (max speed = 0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # does not draw a line
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation (max speed = 0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # does not draw a line
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation (max speed = 0)
ball.shape("square")
ball.color("white")
ball.penup() # does not draw a line
ball.goto(0, 0)
ball.dx = .25 * game_speed
ball.dy = .25 * game_speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}     PlayerB: {}".format(score_a, score_b), align="center", font=("Serrif", 12, "normal"))


# Player Game Functions

# global paddle_a_go_up

# global paddle_a_go_down

"""def paddle_a_up():
    paddle_a_go_up = True
    print('go up')"""


"""def paddle_a_stop_up():
    paddle_a_go_up = False
    print('stop up')"""


"""def paddle_a_down():
    paddle_a_go_down = True
    print('go down')"""


"""def paddle_a_stop_down():
    paddle_a_go_down = False
    print('stop down')"""


def a_up():
    y = paddle_a.ycor()
    y += 7 * game_speed
    paddle_a.sety(y)

def a_down():
    y = paddle_a.ycor()
    y -= 7 * game_speed
    paddle_a.sety(y)


# Keyboard binding
wn.listen() # tells turtle to listen for keyboard input
wn.onkeypress(a_up, "w") # when the user presses w run paddle_a_up
# wn.onkeyrelease(paddle_a_stop_up, "w")
wn.onkeypress(a_down, "s")
# wn.onkeyrelease(paddle_a_stop_down, "s")


# Main game loop
while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}     PlayerB: {}".format(score_a, score_b), align="center", font=("Serrif", 12, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}     PlayerB: {}".format(score_a, score_b), align="center", font=("Serrif", 12, "normal"))


    # Paddle and ball colisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1

    # Paddle tracking

    if (ball.ycor() < paddle_b.ycor()) and ball.xcor() > 0:
        y = paddle_b.ycor()
        y -= random.randint(0, 10)/35 * game_speed
        paddle_b.sety(y)

    if (ball.ycor() > paddle_b.ycor()) and ball.xcor() > 0:
        y = paddle_b.ycor()
        y += random.randint(0, 10)/35 * game_speed
        paddle_b.sety(y)


    """if paddle_a_go_up:
        y = paddle_a.ycor()
        y += 5
        paddle_a.sety(y)

    if paddle_a_go_down:
        y = paddle_a.ycor()
        y -= 5
        paddle_a.sety(y)"""

