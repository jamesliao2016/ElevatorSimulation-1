from Tkinter import *


class Arrow():

    def __init__(self,x0,y0,x1,y1,x2,y2,canvas,floor_number,direction,main):
        self.coords = (x0,y0,x1,y1,x2,y2)
        self.canvas = canvas
        self.direction = direction
        self.floor_number = floor_number
        self.main = main
        self.body = self.canvas.create_polygon(self.coords,fill="red")
        self.status = "off"

        self.canvas.tag_bind(self.body,'<Button-1>', lambda x: self.request(1))

    def request(self,event):
        self.main.floorRequest(self.floor_number,self.direction)
        self.canvas.itemconfigure(self.body, fill = "blue")
        self.status = "on"

    def turnOff(self):
        self.canvas.itemconfigure(self.body, fill = "red")
        self.status = "off"



