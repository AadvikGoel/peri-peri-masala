from  turtle import *
# A function is defined for each part, with following steps

# 1. pen up

# 2. move to correct position

# 3. pen down

# 4. draw

# 5. return home
class Face:
    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = 'small'
    def setSize(self, radius):
            self.size = radius
    def draw(self) :
        self .goHome()
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)
        # --------------------------------------------------

# Functions that are called from with the class

# --------------------------------------------------

# After drawing each part, turtle position

# returns to centre. Parts can be drawn in any order
    def goHome(self):
     penup()
     goto(self.coord)

     setheading(0) 
    def drawOutline(self):
        penup()
# move turtle pen in forward direction
forward(self.size)
left(90)
        # draw a circle of given radiuspendown()
circle(self.size)
        # return back to centre
self.goHome()

def drawEye(self, turn):
        penup()
        # turn turtle pen to given angle
        left(turn)
        # move turtle pen i