from Tkinter import *
import math


class Display():

    def __init__(self,x0,y0,x1,y1,canvas,main):
        self.canvas = canvas
        self.main = main
        coords = (x0,y0,x1,y1)
        self.canvas.create_rectangle(coords, outline="#000", fill="white")
        self.display_floor = self.canvas.create_text(coords[0]+15, coords[1]+20, anchor=W, font="Purisa",text="--")
        self.elevator_assigned = None

    def update(self):
        if not(self.elevator_assigned == None):

            if self.elevator_assigned.state == "moving" or self.elevator_assigned.state == "opening" or self.elevator_assigned.state == "open" or self.elevator_assigned.state == "closing":
                self.canvas.itemconfigure(self.display_floor, text=str(int(math.ceil(self.elevator_assigned.curr_floor)))+" "+ self.elevator_assigned.direction)
            else:
                self.canvas.itemconfigure(self.display_floor, text="--")
        else:
            self.canvas.itemconfigure(self.display_floor, text="--")