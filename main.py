import turtle

screen = turtle.Screen()
screen.setup(width=200,height=220)

def drawSun(x,y,rad,color):
  sun = turtle.Turtle()
  sun.hideturtle()
  sun.color(color)
  sun.penup()
  sun.goto(x,y)
  sun.pendown()
  sun.begin_fill()
  sun.circle(rad)
  sun.end_fill()

drawSun(50,55,23,'#ffe101')
drawSun(-10,-80,1,'black')  
screen.bgcolor('#f0ffde')
def drawRec(turtle,x,y,width,height,color):
  turtle.color(color)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.hideturtle()

  turtle.begin_fill()
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90) 
  turtle.forward(height)
  turtle.end_fill()

house = turtle.Turtle() 
drawRec(house,-80,-100,80,95,'#ebe2af') 
drawRec(house,-30,-50,45,20,'#a35341') 
drawSun(-15,-80,1,'black') 

grass = turtle.Turtle()
drawRec(grass,-100,-110,200,10,'#b1ed7d')

window_left = turtle.Turtle()
drawRec(window_left,-70,-35,20,20,'#afe0d6')
window_right = turtle.Turtle()
drawRec(window_right,-30,-35,20,20,'#afe0d6')

window_lowerTop = turtle.Turtle()

drawRec(window_lowerTop,-70,-70,20,20,'#afe0d6')

window_lowerBottom = turtle.Turtle()

drawRec(window_lowerBottom,-70,-90,20,20,'#afe0d6')

def drawTriangle(x1,y1,x2,y2,x3,y3,color):
  roof = turtle.Turtle()
  roof.hideturtle()
  roof.penup()
  roof.color(color)

  roof.goto(x1,y1)
  roof.pendown()
  roof.begin_fill()
  roof.goto(x2,y2)
  roof.goto(x3,y3)
  roof.goto(x1,y1)
  roof.end_fill()

drawTriangle(-90,-5,10,-5,-40,40,'#a35341')  
