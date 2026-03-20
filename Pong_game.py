import turtle 

wn = turtle.Screen() #creates a window for the game
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) 

paddle_a = turtle.Turtle() #creates the left paddle for player 1
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle() #creates the right paddle for player 2
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle() #creates the ball
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

def paddle_a_up(): #function to move the left paddle up
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): #function to move the left paddle down
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up(): #function to move the right paddle up
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down(): #function to move the right paddle down
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen() #tells the window to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #binds the "w" key
wn.onkeypress(paddle_a_down, "s") #binds the "s" key
wn.onkeypress(paddle_b_up, "Up") #binds the "Up" arrow key
wn.onkeypress(paddle_b_down, "Down") #binds the "Down" arrow key

while True: #main game loop
    wn.update()