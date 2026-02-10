# import turtle
import turtle as trtl
painter = trtl.Turtle() # painter is the name of the turtle used to draw the grass

# create grass
painter.penup()
painter.goto(-400,-100)
painter.pendown()
painter.fillcolor("green")
painter.begin_fill()
for count in range(2): # use for loop to draw the rectangle for the grass
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
for count in range(2): # use for loop to draw the rectangle for the sky
    painter.forward(400)    
    painter.right(90)
    painter.forward(800)
    painter.right(90)
painter.end_fill()

# create clouds
cloud = trtl.Turtle()
# list of (x, y) coordinates for where each cloud starts
cloud_locations = [(-300, 200), (-20, 160), (180, 140)]

for loc in cloud_locations:
    cloud.penup()
    cloud.goto(loc) # move to the next location in the list
    cloud.setheading(90)
    
    # if statement to change the pen color and size for the second cloud
    if loc[0] == -20:
        cloud.pencolor("silver")
        cloud.pensize(4)
    else:
        cloud.pencolor("white")
        cloud.pensize(1)
        
    # draw the cloud (the three overlapping rectangles)
    for i in range(3):
        cloud.pendown()
        cloud.fillcolor("white")
        cloud.begin_fill()
        for count in range(2):
            cloud.forward(20)
            cloud.right(90)
            cloud.forward(40)
            cloud.right(90)
        cloud.end_fill()
        
        # move slightly to draw the next part of the same cloud
        cloud.penup()
        if i == 0: # after first box, go up and right
            cloud.goto(cloud.xcor() + 20, cloud.ycor() + 20)
        else: # after second box, go down and right
            cloud.goto(cloud.xcor() + 20, cloud.ycor() - 20)

# create the lemonade stand base
turtle = duck = lemonade_stand = trtl.Turtle()
lemonade_stand.penup()
lemonade_stand.goto(-200,-100)
lemonade_stand.setheading(90)
lemonade_stand.pendown()
lemonade_stand.fillcolor("brown")
lemonade_stand.begin_fill()
for count in range(2): # draw the rectangle for the lemonade stand
    lemonade_stand.forward(60) 
    lemonade_stand.right(90)    
    lemonade_stand.forward(150)
    lemonade_stand.right(90)
lemonade_stand.end_fill()

# write lemonade on the stand base
lemonade_stand.penup()
lemonade_stand.goto(-125, -70) 
lemonade_stand.pencolor("white")
lemonade_stand.write("LEMONADE", align="center", font=("Arial", 12, "bold")) # write "LEMONADE" on the base of the stand

# create supports of the lemonade stand
lemonade_stand.penup()
lemonade_stand.goto(-200, -100)
for count in range(2):
    lemonade_stand.setheading(90)
    lemonade_stand.pendown()
    lemonade_stand.pencolor("brown")
    lemonade_stand.pensize(5)
    lemonade_stand.forward(150)
    lemonade_stand.penup()
    lemonade_stand.goto(lemonade_stand.xcor() + 150, lemonade_stand.ycor() - 150) # shift over to the right for the second support
    lemonade_stand.pendown()

# create the roof of the lemonade stand
lemonade_stand.penup()
lemonade_stand.goto(-200, 50)
lemonade_stand.setheading(90)
lemonade_stand.pendown()
lemonade_stand.fillcolor("brown")
lemonade_stand.begin_fill()
for count in range(2): # use for loop to draw the rectangle for the roof
    lemonade_stand.forward(60) 
    lemonade_stand.right(90)    
    lemonade_stand.forward(150)
    lemonade_stand.right(90)
lemonade_stand.end_fill()

# write "ice fresh" on the stand
lemonade_stand.penup()
lemonade_stand.goto(-125, 80)
lemonade_stand.pencolor("white")
lemonade_stand.write("ICE FRESH", align="center", font=("Arial", 12, "bold"))

# draw man behind the stand
man = trtl.Turtle()
man.penup()
man.speed(0)

# 1. draw the head
man.fillcolor("peachpuff")
man.goto(-125, -20) # centered behind the stand
man.setheading(0)
man.pendown()
man.begin_fill()
man.circle(15) 
man.end_fill()

# 2. draw the body (torso)
man.penup()
man.goto(-125, -20)
man.setheading(270)
man.pendown()
man.forward(20) # this part goes behind the brown base

# 3. draw the arms (waving)
man.penup()
man.goto(-125, -30) # mid-body
man.pendown()
# left arm
man.setheading(160)
man.forward(20)
# right arm
man.penup()
man.goto(-125, -30)
man.pendown()
man.setheading(20)
man.forward(20)
# draw face details (eyes and expression)
# 1. eyes
man.penup()
# left eye
man.goto(-132, -5) 
man.dot(4, "black")
# right eye
man.goto(-118, -5)
man.dot(4, "black")

man.penup()

# Draw a smile
man.goto(-133, -10)
man.setheading(310)
man.pendown()
man.circle(8, 100) # Draws a small arc for a smile
man.hideturtle()


# create filled lemonade pitcher on the stand
pitcher = trtl.Turtle()
pitcher.penup()
pitcher.goto(-100, -40) # position on the stand
pitcher.setheading(90)
pitcher.pendown()
pitcher.fillcolor("yellow")
pitcher.begin_fill()
for count in range(2): # draw the rectangle for the pitcher
    pitcher.forward(30) 
    pitcher.right(90)    
    pitcher.forward(20)
    pitcher.right(90)
pitcher.end_fill()
# create empty part of the pitcher
pitcher.penup()
pitcher.goto(-100, -10) # position for the empty part (slightly higher than the full part)
pitcher.setheading(90)
pitcher.pendown()
pitcher.pensize(1)
pitcher.pencolor("black")
for count in range(2): # draw the rectangle for the empty part of the pitcher
    pitcher.forward(10) 
    pitcher.right(90)    
    pitcher.forward(20)
    pitcher.right(90)
pitcher.hideturtle()

# import duck image and create duck customer
wn = trtl.Screen()
duck_image = "duck_use.gif" # make sure to have a duck.gif file in the same directory as this code
wn.addshape(duck_image) # add the duck image as a shape to the turtle screen
duck = trtl.Turtle()
duck.shape(duck_image) # set the duck turtle to use the duck image
duck.penup()
duck.goto(200, -50) # position the duck image where the drawn duck is
duck.pendown()

duck.penup()
duck.setheading(180)
duck.forward(200) # move the duck to the left to be next to the lemonade stand
duck.speed(1)

# create text bubble for the duck
text_bubble = trtl.Turtle()
text_bubble.penup()
text_bubble.goto(87, 85) # position above the duck
text_bubble.pendown()
text_bubble.fillcolor("white")
text_bubble.begin_fill()
# draw the oval for the text bubble
text_bubble.setheading(140)# angle the turtle to draw the oval shape
for count in range(2):
    text_bubble.circle(90,90) # draw the curved part of the oval
    text_bubble.circle(40,90) # draw the straight part of the oval
text_bubble.end_fill()
# write text in the bubble
text_bubble.penup()
text_bubble.goto(30, 40) # position for the text inside the bubble
text_bubble.pencolor("black")
text_bubble.write("Hey! Bum-bum-bum, \n got any grapes?", align="center", font=("Arial", 9, "bold"))

wn = trtl.Screen()
wn.mainloop()