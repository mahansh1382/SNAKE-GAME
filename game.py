import random
import turtle
import time


delay=0.1
# FIRST SCORES
score=0
high_score=0

#SET UP SCREEN
wn=turtle.Screen()
wn.title('SNAKE GAME(:')
wn.bgcolor('black')
wn.setup(height=600,width=600)
wn.tracer(0)


# SNAKE HEAD
head=turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction=''


# SNAKE FOOD
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))



# SCORES
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(' SCORE:0  HIGH SCORE:0',align='center',font=('courier',22,'normal'))
#FUNCTIONS
def go_up():
    if head.direction!='down':
        head.direction='up'
def go_down():
    if head.direction!='up':
        head.direction='down'
def go_right():
    if head.direction!='left':
        head.direction='right'
def go_left():
    if head.direction!='right':
        head.direction='left'

def move():
    if head.direction=='up':
       
        head.sety(head.ycor()+20)

    if head.direction=='down':
       
        head.sety(head.ycor()-20)

    if head.direction=='right':
        head.setx(head.xcor()+20)

    if head.direction=='left':
        
        head.setx(head.xcor()-20)    
# KEYBOARD BINDINGS
wn.listen()
wn.onkeypress(go_up,'w')
wn.onkeypress(go_down,'s')
wn.onkeypress(go_right,'d')
wn.onkeypress(go_left,'a')
# MAIN GAME LOOP
segments=[]
while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        score=0
        pen.clear() 
        pen.write(' SCORE:{}  HIGH SCORE:{}'.format(score,high_score),align='center',font=('courier',22,'normal'))

    
    if head.distance(food)< 20:

        food.goto(x=random.randint(-290,290),y=random.randint(-290,290))
    # ADD SEGMENTS
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('gray')
        new_segment.penup()
        segments.append(new_segment)
        # INCREAS THE SCORE
        score+=10
        if score> high_score:
            high_score=score
        pen.clear() 
        pen.write(' SCORE:{}  HIGH SCORE:{}'.format(score,high_score),align='center',font=('courier',22,'normal'))
    # MOVE SEGMENTS
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
   

    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

    time.sleep(delay)

    
wn.mainloop()