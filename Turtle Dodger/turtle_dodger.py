import turtle

wn = turtle.Screen() 
    #wn is window
wn.title("Test Game by TheTraveler")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Character "A" Apperance
char_a = turtle.Turtle()
char_a.speed(0)
char_a.shape("turtle")
char_a.color("white")
char_a.shapesize(stretch_wid=2, stretch_len=2)
char_a.penup()
char_a.goto(0,-280)
char_a.left(90)

#Arrow Apperance
arrow_1 = turtle.Turtle()
arrow_1.speed(0)
arrow_1.shape("triangle")
arrow_1.color("red")
arrow_1.penup()
arrow_1.goto(0,240)
arrow_1.right(90)
arrow_1.dy = -0.20

arrow_2 = turtle.Turtle()
arrow_2.speed(0)
arrow_2.shape("triangle")
arrow_2.color("red")
arrow_2.penup()
arrow_2.goto(50,240)
arrow_2.right(90)
arrow_2.dy = -0.22

arrow_3 = turtle.Turtle()
arrow_3.speed(0)
arrow_3.shape("triangle")
arrow_3.color("red")
arrow_3.penup()
arrow_3.goto(-50,240)
arrow_3.right(90)
arrow_3.dy = -0.24

arrow_4 = turtle.Turtle()
arrow_4.speed(0)
arrow_4.shape("triangle")
arrow_4.color("red")
arrow_4.penup()
arrow_4.goto(100,240)
arrow_4.right(90)
arrow_4.dy = -0.26

arrow_5 = turtle.Turtle()
arrow_5.speed(0)
arrow_5.shape("triangle")
arrow_5.color("red")
arrow_5.penup()
arrow_5.goto(-100,240)
arrow_5.right(90)
arrow_5.dy = -0.28

arrow_6 = turtle.Turtle()
arrow_6.speed(0)
arrow_6.shape("triangle")
arrow_6.color("red")
arrow_6.penup()
arrow_6.goto(150,240)
arrow_6.right(90)
arrow_6.dy = -0.30

arrow_7 = turtle.Turtle()
arrow_7.speed(0)
arrow_7.shape("triangle")
arrow_7.color("red")
arrow_7.penup()
arrow_7.goto(-150,240)
arrow_7.right(90)
arrow_7.dy = -0.30

arrow_8 = turtle.Turtle()
arrow_8.speed(0)
arrow_8.shape("triangle")
arrow_8.color("red")
arrow_8.penup()
arrow_8.goto(200,240)
arrow_8.right(90)
arrow_8.dy = -0.30

arrow_9 = turtle.Turtle()
arrow_9.speed(0)
arrow_9.shape("triangle")
arrow_9.color("red")
arrow_9.penup()
arrow_9.goto(-200,240)
arrow_9.right(90)
arrow_9.dy = -0.30

arrow_10 = turtle.Turtle()
arrow_10.speed(0)
arrow_10.shape("triangle")
arrow_10.color("red")
arrow_10.penup()
arrow_10.goto(250,240)
arrow_10.right(90)
arrow_10.dy = -0.30

arrow_11 = turtle.Turtle()
arrow_11.speed(0)
arrow_11.shape("triangle")
arrow_11.color("red")
arrow_11.penup()
arrow_11.goto(-250,240)
arrow_11.right(90)
arrow_11.dy = -0.30

arrow_12 = turtle.Turtle()
arrow_12.speed(0)
arrow_12.shape("triangle")
arrow_12.color("red")
arrow_12.penup()
arrow_12.goto(300,240)
arrow_12.right(90)
arrow_12.dy = -0.30

arrow_13 = turtle.Turtle()
arrow_13.speed(0)
arrow_13.shape("triangle")
arrow_13.color("red")
arrow_13.penup()
arrow_13.goto(-300,240)
arrow_13.right(90)
arrow_13.dy = -0.30

arrow_14 = turtle.Turtle()
arrow_14.speed(0)
arrow_14.shape("triangle")
arrow_14.color("red")
arrow_14.penup()
arrow_14.goto(350,240)
arrow_14.right(90)
arrow_14.dy = -0.30

arrow_15 = turtle.Turtle()
arrow_15.speed(0)
arrow_15.shape("triangle")
arrow_15.color("red")
arrow_15.penup()
arrow_15.goto(-350,240)
arrow_15.right(90)
arrow_15.dy = -0.30

arrow_16 = turtle.Turtle()
arrow_16.speed(0)
arrow_16.shape("triangle")
arrow_16.color("red")
arrow_16.penup()
arrow_16.goto(400,240)
arrow_16.right(90)
arrow_16.dy = -0.30

arrow_17 = turtle.Turtle()
arrow_17.speed(0)
arrow_17.shape("triangle")
arrow_17.color("red")
arrow_17.penup()
arrow_17.goto(-400,240)
arrow_17.right(90)
arrow_17.dy = -0.30

#Pen
pen = turtle.Turtle()
pen.speed(1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  Lives: 3", align="center", font=("Courier", 24, "normal"))

#Quit
exit = turtle.Turtle()
exit.speed(0)
exit.color("white")
exit.penup()
exit.hideturtle()
exit.goto(0,-240)

#Score
score = 0
lives = 3



#Move Function

def char_a_left():
    x = char_a.xcor()
    x -= 10
    char_a.setx(x)

def char_a_right():
    x = char_a.xcor()
    x += 10
    char_a.setx(x)

#Keyboard binding
wn.listen()
wn.onkeypress(char_a_left, "Left")
wn.onkeypress(char_a_right, "Right")

#Dead turtle

def dead_turtle():
    for i in range(4):
        char_a.right(i)
        



#Main Game Loop
while True:
    wn.update()

    #Border Check
    if char_a.xcor() > 380:
        char_a.setx(380)
    
    if char_a.xcor() < -380:
        char_a.setx(-380)
    
    #Move Arrow_1
    arrow_1.sety(arrow_1.ycor() + arrow_1.dy)

    #Arrow_1 Reset
    
    if arrow_1.ycor() < -300:
        arrow_1.goto(0,240)
        score += 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_2 Activate and Reset
    arrow_2.hideturtle()
    if score >= 1:
        arrow_2.showturtle()
        arrow_2.sety(arrow_2.ycor() + arrow_2.dy)
        if arrow_2.ycor() < -300:
            arrow_2.goto(50,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_3 Activate and Reset
    arrow_3.hideturtle()
    if score >= 2:
        arrow_3.showturtle()
        arrow_3.sety(arrow_3.ycor() + arrow_3.dy)
        if arrow_3.ycor() < -300:
            arrow_3.goto(-50,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    
    #Arrow_4 Activate and Reset
    arrow_4.hideturtle()
    if score >= 3:
        arrow_4.showturtle()
        arrow_4.sety(arrow_4.ycor() + arrow_4.dy)
        if arrow_4.ycor() < -300:
            arrow_4.goto(100,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    #Arrow_5 Activate and Reset
    arrow_5.hideturtle()
    if score >= 4:
        arrow_5.showturtle()
        arrow_5.sety(arrow_5.ycor() + arrow_5.dy)
        if arrow_5.ycor() < -300:
            arrow_5.goto(-100,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    #Arrow_6 Activate and Reset
    arrow_6.hideturtle()
    if score >= 5:
        arrow_6.showturtle()
        arrow_6.sety(arrow_6.ycor() + arrow_6.dy)
        if arrow_6.ycor() < -300:
            arrow_6.goto(150,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_7 Activate and Reset
    arrow_7.hideturtle()
    if score >= 6:
        arrow_7.showturtle()
        arrow_7.sety(arrow_7.ycor() + arrow_7.dy)
        if arrow_7.ycor() < -300:
            arrow_7.goto(-150,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    #Arrow_8 Activate and Reset
    arrow_8.hideturtle()
    if score >= 7:
        arrow_8.showturtle()
        arrow_8.sety(arrow_8.ycor() + arrow_8.dy)
        if arrow_8.ycor() < -300:
            arrow_8.goto(200,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))    
    
    #Arrow_9 Activate and Reset
    arrow_9.hideturtle()
    if score >= 8:
        arrow_9.showturtle()
        arrow_9.sety(arrow_9.ycor() + arrow_9.dy)
        if arrow_9.ycor() < -300:
            arrow_9.goto(-200,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))     

    #Arrow_10 Activate and Reset
    arrow_10.hideturtle()
    if score >= 9:
        arrow_10.showturtle()
        arrow_10.sety(arrow_10.ycor() + arrow_10.dy)
        if arrow_10.ycor() < -300:
            arrow_10.goto(250,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_11 Activate and Reset
    arrow_11.hideturtle()
    if score >= 10:
        arrow_11.showturtle()
        arrow_11.sety(arrow_11.ycor() + arrow_11.dy)
        if arrow_11.ycor() < -300:
            arrow_11.goto(-250,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))   

    #Arrow_12 Activate and Reset
    arrow_12.hideturtle()
    if score >= 11:
        arrow_12.showturtle()
        arrow_12.sety(arrow_12.ycor() + arrow_12.dy)
        if arrow_12.ycor() < -300:
            arrow_12.goto(300,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_13 Activate and Reset
    arrow_13.hideturtle()
    if score >= 12:
        arrow_13.showturtle()
        arrow_13.sety(arrow_13.ycor() + arrow_13.dy)
        if arrow_13.ycor() < -300:
            arrow_12.goto(-300,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_14 Activate and Reset
    arrow_14.hideturtle()
    if score >= 13:
        arrow_14.showturtle()
        arrow_14.sety(arrow_14.ycor() + arrow_14.dy)
        if arrow_14.ycor() < -300:
            arrow_14.goto(350,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_15 Activate and Reset
    arrow_15.hideturtle()
    if score >= 14:
        arrow_15.showturtle()
        arrow_15.sety(arrow_15.ycor() + arrow_15.dy)
        if arrow_15.ycor() < -300:
            arrow_15.goto(-350,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_16 Activate and Reset
    arrow_16.hideturtle()
    if score >= 15:
        arrow_16.showturtle()
        arrow_16.sety(arrow_16.ycor() + arrow_16.dy)
        if arrow_16.ycor() < -300:
            arrow_16.goto(400,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_17 Activate and Reset
    arrow_17.hideturtle()
    if score >= 16:
        arrow_17.showturtle()
        arrow_17.sety(arrow_17.ycor() + arrow_17.dy)
        if arrow_17.ycor() < -300:
            arrow_17.goto(-400,240)
            score += 1
            pen.clear()
            pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_1 Collision

    if (arrow_1.ycor() < char_a.ycor() + 40) and (arrow_1.xcor() > char_a.xcor() - 30) and (arrow_1.xcor() < char_a.xcor() + 30):
        arrow_1.goto(0, 240) #240 for y axis so arrow is not covering the score board
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    #Arrow_2 Collision

    if (arrow_2.ycor() < char_a.ycor() + 40) and (arrow_2.xcor() > char_a.xcor() - 30) and (arrow_2.xcor() < char_a.xcor() + 30):
        arrow_2.goto(50, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_3 Collision

    if (arrow_3.ycor() < char_a.ycor() + 40) and (arrow_3.xcor() > char_a.xcor() - 30) and (arrow_3.xcor() < char_a.xcor() + 30):
        arrow_3.goto(-50, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_4 Collision

    if (arrow_4.ycor() < char_a.ycor() + 40) and (arrow_4.xcor() > char_a.xcor() - 30) and (arrow_4.xcor() < char_a.xcor() + 30):
        arrow_4.goto(100, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_5 Collision

    if (arrow_5.ycor() < char_a.ycor() + 40) and (arrow_5.xcor() > char_a.xcor() - 30) and (arrow_5.xcor() < char_a.xcor() + 30):
        arrow_5.goto(-100, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_6 Collision

    if (arrow_6.ycor() < char_a.ycor() + 40) and (arrow_6.xcor() > char_a.xcor() - 30) and (arrow_6.xcor() < char_a.xcor() + 30):
        arrow_6.goto(150, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))
    
    #Arrow_7 Collision

    if (arrow_7.ycor() < char_a.ycor() + 40) and (arrow_7.xcor() > char_a.xcor() - 30) and (arrow_7.xcor() < char_a.xcor() + 30):
        arrow_7.goto(-150, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_8 Collision

    if (arrow_8.ycor() < char_a.ycor() + 40) and (arrow_8.xcor() > char_a.xcor() - 30) and (arrow_8.xcor() < char_a.xcor() + 30):
        arrow_8.goto(200, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_9 Collision

    if (arrow_9.ycor() < char_a.ycor() + 40) and (arrow_9.xcor() > char_a.xcor() - 30) and (arrow_9.xcor() < char_a.xcor() + 30):
        arrow_9.goto(-200, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_10 Collision

    if (arrow_10.ycor() < char_a.ycor() + 40) and (arrow_10.xcor() > char_a.xcor() - 30) and (arrow_10.xcor() < char_a.xcor() + 30):
        arrow_10.goto(250, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_11 Collision

    if (arrow_11.ycor() < char_a.ycor() + 40) and (arrow_11.xcor() > char_a.xcor() - 30) and (arrow_11.xcor() < char_a.xcor() + 30):
        arrow_11.goto(-250, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_12 Collision

    if (arrow_12.ycor() < char_a.ycor() + 40) and (arrow_12.xcor() > char_a.xcor() - 30) and (arrow_12.xcor() < char_a.xcor() + 30):
        arrow_12.goto(300, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_13 Collision

    if (arrow_13.ycor() < char_a.ycor() + 40) and (arrow_13.xcor() > char_a.xcor() - 30) and (arrow_13.xcor() < char_a.xcor() + 30):
        arrow_13.goto(-300, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_14 Collision

    if (arrow_14.ycor() < char_a.ycor() + 40) and (arrow_14.xcor() > char_a.xcor() - 30) and (arrow_14.xcor() < char_a.xcor() + 30):
        arrow_14.goto(350, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_15 Collision

    if (arrow_15.ycor() < char_a.ycor() + 40) and (arrow_15.xcor() > char_a.xcor() - 30) and (arrow_15.xcor() < char_a.xcor() + 30):
        arrow_15.goto(-350, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_16 Collision

    if (arrow_16.ycor() < char_a.ycor() + 40) and (arrow_16.xcor() > char_a.xcor() - 30) and (arrow_16.xcor() < char_a.xcor() + 30):
        arrow_16.goto(400, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Arrow_17 Collision

    if (arrow_17.ycor() < char_a.ycor() + 40) and (arrow_17.xcor() > char_a.xcor() - 30) and (arrow_17.xcor() < char_a.xcor() + 30):
        arrow_17.goto(-400, 240)
        lives -= 1
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))

    #Game Over

    if lives == 0:
        exit.clear()
        exit.color("red")
        exit.goto(0,0)
        exit.write("GAME OVER", align="center", font=("Courier", 80, "bold"))        
        
        pen.clear()
        pen.write("Score: {}  Lives: {}".format(score, lives), align="center", font=("Courier", 24, "normal"))        
        
        arrow_1.dy = 0
        arrow_2.dy = 0
        arrow_3.dy = 0
        arrow_4.dy = 0
        arrow_5.dy = 0
        arrow_6.dy = 0
        arrow_7.dy = 0
        arrow_8.dy = 0
        arrow_9.dy = 0
        arrow_10.dy = 0
        arrow_11.dy = 0
        arrow_12.dy = 0
        arrow_13.dy = 0
        arrow_14.dy = 0
        arrow_15.dy = 0
        arrow_16.dy = 0
        arrow_17.dy = 0

        dead_turtle()
        # arrow_1.hideturtle()
        # arrow_2.hideturtle()
        # arrow_3.hideturtle()
        # arrow_4.hideturtle()
        # arrow_5.hideturtle()
        # arrow_6.hideturtle()
        # arrow_7.hideturtle()
        # arrow_8.hideturtle()
        # arrow_9.hideturtle()
        # arrow_10.hideturtle()
        # arrow_11.hideturtle()
        # arrow_12.hideturtle()
        # arrow_13.hideturtle()
        # arrow_14.hideturtle()
        # arrow_15.hideturtle()
        # arrow_16.hideturtle()
        # arrow_17.hideturtle()              


        
 

