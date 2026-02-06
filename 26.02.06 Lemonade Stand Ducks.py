# import turtle
import turtle as trtl
painter = trtl.Turtle()

# create grass
painter.penup()
painter.goto(-400,-100)
painter.pendown()
painter.fillcolor("green")
painter.begin_fill()
for count in range(2):
    painter.forward(800)    
    painter.right(90)
    painter.forward(400)
    painter.right(90)
painter.end_fill()

# create sky
painter.penup()
painter.setheading(90)
painter.goto(-400,-100)
painter.pendown()
painter.fillcolor("lightblue")
painter.begin_fill()
for count in range(2):
    painter.forward(400)    
    painter.right(90)
    painter.forward(800)
    painter.right(90)
painter.end_fill()

# create duck body  
painter.penup()
painter.goto(200,-60)
painter.setheading(270)
painter.pendown()
painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(40,180) 
painter.end_fill()
painter.penup()

# create duck head
painter.goto(220,-50)  
painter.setheading(90)
painter.pendown()
painter.fillcolor("yellow")
painter.begin_fill()
painter.circle(20) # create duck head
painter.end_fill()

# create duck beak
painter.penup()
painter.goto(175,-50)
painter.setheading(270)
painter.pendown()
painter.fillcolor("orange")
painter.begin_fill()
painter.circle(5,360,3) # draw duck beak as a triangle
painter.end_fill()

# create duck eye
painter.penup()
painter.goto(200,-50)
painter.setheading(90)
painter.pendown()
painter.fillcolor("black")
painter.begin_fill()    
painter.circle(3) # create duck eye
painter.end_fill()


wn = trtl.Screen()
wn.mainloop()