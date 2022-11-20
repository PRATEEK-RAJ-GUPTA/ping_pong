#pong_game

import turtle
import winsound

wn=turtle.Screen()
wn.title('Ping Pong Game')
wn.bgcolor('black')
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color('yellow')
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('yellow')
paddle_b.penup()
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dy = 0.0625  # type: ignore
ball.dx = 0.0625  # type: ignore

#pen

pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0",align="center",font=('Courier',24,'normal'))

#Score
score_a=0
score_b=0
#FUNCTION

#function to move y up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
#function to move y down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)
#function to move x up
def paddle_b_up():
    x=paddle_b.ycor()
    x+=20
    paddle_b.sety(x)
#function to move x down
def paddle_b_down():
    x=paddle_b.ycor()
    x-=20
    paddle_b.sety(x)
#keyboard listen
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

#Main Game Loop

while True:
    wn.update()
#moveing the ball
    ball.setx(ball.xcor()+ ball.dx)  # type: ignore
    ball.sety(ball.ycor()+ ball.dy) # type: ignore
#Border checking
    #TOP-BOTTOM
    if ball.ycor()>290:
      ball.sety(290)
      ball.dy*=-1     # type: ignore
      winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor()<-290:
      ball.sety(-290)
      ball.dy*=-1  # type: ignore
      winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     

    #LEFT-RIGHT
    if  ball.xcor()>390:
      ball.goto(0,0)
      ball.dx*=-1 # type: ignore
      score_a+=1
      pen.clear()
      pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=('Courier',24,'normal'))
      winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     


    if  ball.xcor()<-390:
      ball.goto(0,0)
      ball.dx*=-1  # type: ignore
      score_b+=1
      pen.clear()
      pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font=('Courier',24,'normal'))
      winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     


#Bouncing off ball
 #right
    if(ball.xcor()>340) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-50):
      ball.setx(340)
      ball.dx*=-1    # type: ignore 
      winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
     

#left 
    if(ball.xcor()<-340) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
      ball.setx(-340)
      ball.dx*=-1    # type: ignore 
      winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if score_a>=10:
      pen.clear()
      pen.write("Player B won",align="center",font=('Courier',24,'normal'))
      flag=False
    elif score_b>=10:
      pen.clear()
      pen.write("Player A won",align="center",font=('Courier',24,'normal'))
    # if(flag==False):
    #   pen.clear()
    #   pen.write("Want To play Again press 1 else 0:",align="center",font=('Courier',24,'normal'))
    #   x=int(input())
    #   flag=x
      # if(x==1):
      #   flag=True
      # else:
      #   flag=False
