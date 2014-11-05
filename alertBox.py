from Tkinter import *
import math


class Alert():

    def __init__(self,x0,y0,x1,y1,canvas,main,lift_number):
        self.canvas = canvas
        self.main = main
        self.lift_number = lift_number
        coords = (x0,y0,x1,y1)
        self.canvas.create_rectangle(coords, outline="#000", fill="white")
        self.canvas.create_text(coords[0]+50, coords[1]+20, anchor=W, fill="red", font="Purisa",text="Alert Lift 1")
        self.alert_message = self.canvas.create_text(coords[0]+45, coords[1]+90, anchor=W, fill="red", font="Purisa",text="")
        self.person_count = self.canvas.create_text(coords[0]+20, coords[1]+50, anchor=W, fill="red", font="Purisa",text="No. of Persons: "+ str(0))

    def update(self):
        self.canvas.itemconfigure(self.person_count, text="No. of Persons: "+ str(self.main.lift_list[self.lift_number-1].person_count))
        if self.main.lift_list[self.lift_number-1].person_count > 10:
            self.canvas.itemconfigure(self.alert_message, text="Overloaded")
        else:
            self.canvas.itemconfigure(self.alert_message, text="")


        