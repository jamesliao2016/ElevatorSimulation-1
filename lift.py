from Tkinter import *


floorHeight = 108
shiftParameter = 250
liftParameter = 972

class Lift():

    def __init__(self,x0,y0,x1,y1,canvas):
        self.canvas = canvas
        self.coords = (x0,y0,x1,y1)
        self.body = self.canvas.create_rectangle(self.coords, outline="black", fill="#f0b")


