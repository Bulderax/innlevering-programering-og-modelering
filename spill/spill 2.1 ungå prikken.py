""" Meningen med spille er å ikke bli trofett av ballen som spretter rundt.
    Du beveger deg ved å bruke (w,a,d,s)
"""
import turtle

print("Bruk (w, s, a ,d) til å bevege deg")

# Skjerm
wn = turtle.Screen()
wn.title("Ungå prikken")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Score
score = 0


# spiller A
spiller_a = turtle.Turtle()
spiller_a.speed(0)
spiller_a.shape("square")
spiller_a.color("white")
spiller_a.shapesize(stretch_wid=1, stretch_len=1)
spiller_a.penup()
spiller_a.goto(-350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.endringx = 1 # farten til ballen x retning
ball.endringy = 1 # y retning

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup
pen.hideturtle()
pen.gotto(0, 260)
pen.write("Liv brukt: 0", align="center", font=("courier", 24, "normal"))
    
    # Funksjon
def spiller_a_up():
    y = spiller_a.ycor()
    y += 20
    spiller_a.sety(y)
   
def spiller_a_down():
    y = spiller_a.ycor()
    y -= 20
    spiller_a.sety(y)
    
def spiller_a_right():
    x = spiller_a.xcor()
    x += 20
    spiller_a.setx(x)
    
def spiller_a_left():
    x = spiller_a.xcor()
    x -= 20
    spiller_a.setx(x)
    

# Keyboard binding
wn.listen()
wn.onkeypress(spiller_a_up, "w")
wn.onkeypress(spiller_a_down, "s")
wn.onkeypress(spiller_a_right, "d")
wn.onkeypress(spiller_a_left, "a")


# Main game loop
while True:
    wn.update()
    
   # Flyt ballen
    ball.setx(ball.xcor() + ball.endringx)
    ball.sety(ball.ycor() + ball.endringy)

   # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.endringy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.endringy *= -1   
    
    if ball.xcor() > 390:
        ball.setx(390)
        ball.endringx *= -1
        
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.endringx *= -1
    
    if spiller_a.ycor() > 290:
        spiller_a.sety(290)
    
    if spiller_a.ycor() < -290:
        spiller_a.sety(-290)
        
    if spiller_a.xcor() > 390:
        spiller_a.setx(390)
        
    if spiller_a.xcor() < -390:
        spiller_a.setx(-390)
        
    if ball.xcor() == spiller_a and (ball.ycor() == spiller_a):
        score += 1
        pen.clear()
        pen.write("Liv brukt: {}".formate(score), align="center", font=("courier", 24, "normal"))