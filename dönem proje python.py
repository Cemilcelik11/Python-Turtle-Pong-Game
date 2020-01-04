import turtle
import winsound
#building up a window
window = turtle.Screen()
window.title("Pong by Cemil Çelik")
window.bgcolor("black")
window.setup(width=800, height=600)
#preventing the window from updating,we will update manually
window.tracer(0)
window.delay(1)
     


#Player 1
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape("circle")
player_1.color("white")
player_1.penup()
player_1.goto(-350, 0)
player_1.shapesize(stretch_wid=2, stretch_len=2)

#Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape("circle")
player_2.color("white")
player_2.penup()
player_2.goto(350, 0)
player_2.shapesize(stretch_wid=2, stretch_len=2)
        
#Score

score_player_1 = 0
score_player_2 = 0

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)
ball.dx = 0.3
ball.dy = -0.3

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0",align="center",font = ("Courier",15,"normal"))
#Functions
        
def player_1_up():
    y = player_1.ycor()
    y += 30
    player_1.sety(y)
    
def player_1_down():
    y = player_1.ycor()
    y -= 30
    player_1.sety(y)
    
def player_2_up():
    y = player_2.ycor()
    y += 30
    player_2.sety(y)
    
def player_2_down():
    y = player_2.ycor()
    y -= 30
    player_2.sety(y)
    

#Getting inputs from user5
window.listen()
window.onkeypress(player_1_up, "w")
window.onkeypress(player_1_down, "s")
window.onkeypress(player_2_up, "Up")
window.onkeypress(player_2_down, "Down")


#Main loop
while True:
    window.update() #everytime it runs updates the screen
    
    #Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

    #When ball hits the border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_player_2 += 1
        winsound.PlaySound("sfx_weapon_singleshot8.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_player_1,score_player_2), align="center",font = ("Courier",10,"normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_player_1 += 1
        winsound.PlaySound("sfx_wpn_cannon1.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score_player_1,score_player_2), align="center",font = ("Courier",10,"normal"))
   
        
        
    
    #Paddle and ball collide
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player_2.ycor() + 50 and ball.ycor() > player_2.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player_1.ycor() + 50 and ball.ycor() > player_1.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
 
        
   