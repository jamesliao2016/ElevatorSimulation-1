from Tkinter import *


class Lift():

    def __init__(self,x0,y0,x1,y1,canvas):
        self.canvas = canvas
        self.coords = (x0,y0,x1,y1)
        self.body = self.canvas.create_rectangle(self.coords, outline="black", fill="#f0b")
        self.state = "idle"
        self.request_queue = []
        for i in range(11):
            self.request_queue[i] = 0
        self.curr_floor = 1
        self.direction = "up"
        self.destination = None
        self.lift_speed = 2
        self.person_count = 0
        self.y = self.canvas.coords(self.body)[1]

    def update(self):
        if self.state == "moving":
            pass

    def checkRequestQueue(self):
        if self.state == "idle":
            for i in range(11):
                if self.request_queue[i] == 1 and self.curr_floor<=i:
                    self.destination = i
                    self.vel = -self.lift_speed
                    self.direction = "up"
                    break
                elif self.request_queue == 1 and self.curr_floor>i:
                    self.destination = i
                    self.vel = self.lift_speed
                    self.direction = "down"
                    break
            self.state = "moving"

        elif self.state == "moving":
            for i in range(11):
                if self.request_queue[i] == 1 and self.direction == "up" and self.curr_floor<=i:
                    self.destination = i
                    break
                elif self.request_queue[i] == 1 and self.direction == "down" and self.curr_floor>=i:
                    self.destination = i
                    break

    def checkDestination(self):
        self.curr_floor = 10-int(self.y/108)

        if self.curr_floor == self.destination:
            self.request_queue[self.curr_floor] = 0



