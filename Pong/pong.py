# Pong Game

import turtle
import winsound

wn = turtle.Screen() 
    #wn is window
wn.title("Pong by TheTraveler")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
    #tracer delays the screen from updating

# Score
score_a = 0
score_b = 0


# Paddle A 
paddle_a = turtle.Turtle()
    #'Turtle' is the turtle object and class name
paddle_a.speed(0)
    #speed() is the animation speed
paddle_a.shape("square")
paddle_a.color("gold")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    #shapesize to stretch from square to rectangle
    #the paddle square shape is by default 20px x 20px so streching it makes it 100px by 20px
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("gold")
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
ball.dx = 0.15
    #dx to move the ball to the right by 2 pixels
ball.dy = -0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function (To move paddle and ball)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
        #sety will set paddle_a to what y equals

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
wn.listen()
    # Listen tells us to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")
    # when the user presses "w" (note it has to be lowercase so make sure caps are off), call the function paddle_a_up
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
    # 'Up' and 'Down' are for the arrow keys

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
        # Allow the ball to move from corrdinate 0,0 to dx which is 2 px to the right
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            # the *= -1 reverses the direction
            # Remeber that coordinate 0,0 is at the center of the screen, and screen height is 600
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions for bouncing 
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)