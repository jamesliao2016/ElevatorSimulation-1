from Tkinter import *
import time
import math

floor_height = 108

class Lift():

    def __init__(self,x0,y0,x1,y1,canvas,lift_number):
        self.canvas = canvas
        self.lift_number = lift_number
        self.coords = (x0,y0,x1,y1)
        self.body = self.canvas.create_rectangle(self.coords, outline="black", fill="#1e90ff")
        self.door = self.canvas.create_rectangle(self.coords, outline="black", fill="#7cbb00")
        self.state = "idle"
        self.request_queue = []
        
        for i in range(11):
            self.request_queue.append(0)

        self.curr_floor = 1
        self.direction = "up"
        self.destination = None
        self.lift_speed = 2
        self.person_count = 0
        self.door_status = 0
        self.open_status = 0
        self.y = self.canvas.coords(self.body)[1]
        self.x = self.canvas.coords(self.body)[0]

    def update(self):

        if self.state == "idle":
            self.checkRequestQueue()

        elif self.state == "opening":
            self.openDoor()

        elif self.state == "open":
            self.keepDoorOpen()

        elif self.state == "closing":
            self.closeDoor()

        elif self.state == "moving":
            self.checkRequestQueue()
            self.checkDestination()
            self.moveLift()

        self.canvas.update()

    def addFloorRequest(self,floor,direction):
        self.request_queue[floor] = 1

    def checkRequestQueue(self):
        if self.state == "idle":
            for i in range(11):
                if self.request_queue[i] == 1 and self.curr_floor<=i:
                    self.destination = i
                    self.vel = -self.lift_speed
                    self.direction = "up"
                    self.state = "moving"
                    break
                elif self.request_queue == 1 and self.curr_floor>i:
                    self.destination = i
                    self.vel = self.lift_speed
                    self.direction = "down"
                    self.state = "moving"
                    break
            

        elif self.state == "moving":
            for i in range(11):
                if self.request_queue[i] == 1 and self.direction == "up" and self.curr_floor<=i:
                    self.destination = i
                    break
                elif self.request_queue[i] == 1 and self.direction == "down" and self.curr_floor>=i:
                    self.destination = i
                    break

    def checkDestination(self):
        self.curr_floor = int(10-math.floor((self.y+108)/108))
        #print self.curr_floor

        if self.curr_floor == self.destination:
            self.request_queue[self.curr_floor] = 0
            self.state = "opening"
            self.vel = 0


    def moveLift(self):
        self.canvas.move(self.body,0,self.vel)
        self.canvas.move(self.door,0,self.vel)
        self.x = self.canvas.coords(self.body)[0]
        self.y = self.canvas.coords(self.body)[1]

    def openDoor(self):
        if self.door_status == 250:
            self.status = "open"
        else:
            self.door_status += 2
            self.canvas.coords(self.door,self.x,self.y,self.x+self.door_status,self.y+floor_height)


    def keepOpenDoor(self):
        if self.open_status == 100:
            self.status = "closing"
            self.open_status = 0
        else:
            self.open_status += 5

    def closeDoor(self):
        if self.door_status == 0:
            self.status = "idle"
        else:
            self.door_status -= 2
            self.canvas.coords(self.door,self.x,self.y,self.x+self.door_status,self.y+floor_height)

            



