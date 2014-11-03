from Tkinter import *

floorHeight = 108
shiftParameter = 250

class Arrow():

    def __init__(self,x0,y0,x1,y1,x2,y2,canvas):
        self.coords = (x0,y0,x1,y1,x2,y2)
        self.canvas = canvas
        self.body = self.canvas.create_polygon(self.coords,fill="red")


