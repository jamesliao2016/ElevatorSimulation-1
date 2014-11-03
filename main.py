from Tkinter import *
import time
import math
from lift import *
from liftPanel import *
from requestArrow import *

screenWidth = 0
screenHeight = 0
shiftParameter = 250
floorHeight = 108
liftParameter = 972


class ElevatorApp():
    def __init__(self,root):
        global screenWidth,screenHeight
        self.root = root
        self.root.title("Elevator Simulation System")
        self.canvas = Canvas(self.root, width = screenWidth, height = screenHeight, bg = "white")
        self.canvas.pack()
        
        #Vertical Lines
        for i in range(5):
            self.canvas.create_line(i*shiftParameter, 0, i*shiftParameter, screenHeight, fill = "black",tags = "line")

        #Horizontal Lines
        for i in range(9):
            self.canvas.create_line(0, (i+1)*floorHeight, 4*shiftParameter, (i+1)*floorHeight, fill = "black",tags = "line")

        self.draw_lifts(self.canvas)

        #Floor Labelling
        for i in range(10):
            self.canvas.create_text(20, 30+i*floorHeight, anchor=W, font="Purisa",text="Floor No. "+str(10-i))
        
        #liftPanelOuterBoxes
        self.draw_panels(self.canvas)

        #alertBoxes
        self.canvas.create_rectangle(1200, 610, 1400, 750, outline="#000", fill="white")
        self.canvas.create_text(1250, 630, anchor=W, fill="red", font="Purisa",text="Alert Lift 1")
        self.canvas.create_rectangle(1500, 610, 1700, 750, outline="#000", fill="white")
        self.canvas.create_text(1550, 630, anchor=W, fill="red", font="Purisa",text="Alert Lift 2")
        self.canvas.create_rectangle(1200, 770, 1400, 910, outline="#000", fill="white")
        self.canvas.create_text(1250, 790, anchor=W, fill="red", font="Purisa",text="Alert Lift 3")
        self.canvas.create_rectangle(1500, 770, 1700, 910, outline="#000", fill="white")
        self.canvas.create_text(1550, 790, anchor=W, fill="red", font="Purisa",text="Alert Lift 4")
        
        #draw Request Arrow
        self.draw_requestArrow(self.canvas)
        
    def draw_lifts(self,canvas):
        self.liftList = []
        for i in range(4):
            self.liftList.append(Lift(i*shiftParameter, liftParameter, (i+1)*shiftParameter, liftParameter+floorHeight,canvas))
    
    def draw_panels(self,canvas):
        for i in range (4):
            LiftPanel(i,self.canvas) 

    def draw_requestArrow(self,canvas):
        for i in range(10):
            Arrow(1030, i*floorHeight+40, 1070, i*floorHeight+40, 1050,i*floorHeight+10,canvas)
            Arrow(1030, i*floorHeight+50, 1070, i*floorHeight+50, 1050,i*floorHeight+80,canvas)


def main():

    root = Tk()
    posx = 0
    posy = 0
    global screenWidth
    global screenHeight
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.wm_geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, posx, posy))
    app = ElevatorApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
