from Tkinter import *


class Button():

    def __init__(self,coords,lift_number,floor_number,main,canvas):

        self.lift_number = lift_number
        self.floor_number = floor_number
        self.canvas = canvas
        self.main = main

        self.body = self.canvas.create_oval(coords, outline="black", fill="white", width=2)
        self.button_text = self.canvas.create_text(coords[0]+15, coords[1]+20, anchor=W, font="Purisa",text=str(self.floor_number))
        self.canvas.tag_bind(self.body,'<Button-1>', lambda x: self.request(1,floor_number))
        self.canvas.tag_bind(self.button_text,'<Button-1>', lambda x: self.request(1,floor_number))
        

    def request(self,event,floor_number):
        if floor_number == "<>":
            if self.main.lift_list[self.lift_number].state == "closing" or self.main.lift_list[self.lift_number].state == "idle":
                self.main.lift_list[self.lift_number].state = "opening"

        elif floor_number == "><":
            if self.main.lift_list[self.lift_number].state == "opening" or self.main.lift_list[self.lift_number].state == "open":
               self.main.lift_list[self.lift_number].state = "closing"

        else:    
            self.main.lift_list[self.lift_number].addFloorRequest(floor_number,"up")

