import turtle, math

class Snowflake(turtle.Turtle):
    #extends the Turtle class
    def __init__(self,*args,**kwargs):
        super(Snowflake,self).__init__(*args,**kwargs)
        self.penup()

    #draw arms at 45 degree angle from main branch
    def drawarm(self,s):
        self.left(45)
        for i in range(3):
            self.forward(s)
            self.backward(s)
            self.right(45)
        self.left(90)
    
    #draws a single branch at a specified angle with optional parameters
    def drawbranch(self,angle,length=100,arms=1,armsize=30,width=4,armchange=0,offset=0):
        self.pendown()
        self.showturtle()
        self.pensize(width)
        self.right(45)
        moved = 0
        dist = armsize * 0.7071067
        if offset == 0:
            offset = length - (((arms-1) * dist) + armsize)
        even = False
        self.forward(offset)
        moved+=offset
        if offset > 0 and arms > 1:
            dist = (length - (offset+armsize)) / (arms-1)
            even = True
            
        armlen = armsize
        for i in range(arms):
            self.drawarm(armlen)
            if not(i == arms-1 and even):
                self.forward(dist)
                moved+=dist
            armlen -= armchange
        self.backward(moved)
        self.right(angle)
        self.left(45)
        self.hideturtle()
        self.penup()
