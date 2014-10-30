from Tkinter import *
import time
import math
from random import randint

screenWidth = 0
screenHeight = 0
shiftParameter = 250
floorHeight = 108
floorRequest = []
lift = []
lift1Request = []
lift2Request = []
lift3Request = []
lift4Request = []
noPersonLift1 = 0
noPersonLift2 = 0
noPersonLift3 = 0
noPersonLift4 = 0

class Button():

    def __init__(self,x0,y0,x1,y1,name=None,floorNumber=None):
        self.coords = (x0,y0,x1,y1)
        self.name = name
        self.floorNumber = floorNumber


    def draw(self, canvas):
        self.body = canvas.create_oval(self.coords, outline="black", fill="white", width=2)
        self.buttonText = canvas.create_text(self.coords[0]+15, self.coords[1]+20, anchor=W, font="Purisa",text=self.floorNumber)
        canvas.tag_bind(self.body, "<1>", self.mouse_click)
        canvas.tag_bind(self.buttonText, "<1>", self.mouse_click)

    def mouse_click(self, event):
        if(self.name == 1):
            lift1Request[int(self.floorNumber)] = 1
        elif(self.name == 2):
            lift2Request[int(self.floorNumber)] = 1
        elif(self.name == 3):
            lift3Request[int(self.floorNumber)] = 1
        elif(self.name == 4):
            lift4Request[int(self.floorNumber)] = 1    
        print "I got a mouse click (%s)" % self.floorNumber

class AddRemoveButton():
    def __init__(self,x0,y0,x1,y1,liftNumber):
        self.coords = (x0,y0,x1,y1)
        self.coords1 = (x0,y0-50,x1,y1-50)
        self.liftNumber = liftNumber

    def draw(self,canvas):
        self.canvas = canvas
        self.addButton = canvas.create_oval(self.coords, outline="black", fill="white", width=2)
        self.removeButton = canvas.create_oval(self.coords1, outline="black", fill="white", width=2)
        self.buttonPlus = canvas.create_text(self.coords[0]+15, self.coords[1]+20, anchor=W, font="Purisa",text="+")
        self.buttonMinus = canvas.create_text(self.coords1[0]+15, self.coords1[1]+20, anchor=W, font="Purisa",text="-")
        canvas.tag_bind(self.addButton, "<1>", self.mouse_click)
        canvas.tag_bind(self.buttonPlus, "<1>", self.mouse_click)
        canvas.tag_bind(self.removeButton, "<1>", self.mouse_click1)
        canvas.tag_bind(self.buttonMinus, "<1>", self.mouse_click1)

    def mouse_click(self, event):
        global noPersonLift4,noPersonLift1,noPersonLift2,noPersonLift3
        if(self.liftNumber==1):
            noPersonLift1 = noPersonLift1 + 1
        elif(self.liftNumber==2):
            noPersonLift2 = noPersonLift2 + 1
        elif(self.liftNumber==3):
            noPersonLift3 = noPersonLift3 + 1
        else:
            noPersonLift4 = noPersonLift4 + 1
        self.canvas.update()

        print "I got a mouse click (%s)" % self.liftNumber

    def mouse_click1(self, event):
        global noPersonLift4,noPersonLift1,noPersonLift2,noPersonLift3
        if(self.liftNumber==1):
            noPersonLift1 = noPersonLift1 - 1
        elif(self.liftNumber==2):
            noPersonLift2 = noPersonLift2 - 1
        elif(self.liftNumber==3):
            noPersonLift3 = noPersonLift3 - 1
        else:
            noPersonLift4 = noPersonLift4 - 1
        self.canvas.update() 
        print "I got a mouse click (%s)" % self.liftNumber


class Arrow():

    def __init__(self,x0,y0,x1,y1,x2,y2,name=None):
        self.coords = (x0,y0,x1,y1,x2,y2)
        self.name = name

    def draw(self, canvas):
        self.body = canvas.create_polygon(self.coords,fill="red")
        canvas.tag_bind(self.body, "<1>", self.mouse_click)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
        

    def update(self,canvas,liftVel):
        canvas.move(self.body,0,liftVel)
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]

    def mouse_click(self, event):
        global floorRequest
        floorRequest[int(self.name)] = 1
        print "I got a mouse click (%s)" % self.name

class Lift():

    def __init__(self,x0,y0,x1,y1,direction,currFloor,isMoving, liftNumber):
        self.coords = (x0,y0,x1,y1)
        self.direction = direction
        self.currFloor = currFloor
        self.isMoving = isMoving
        self.liftNumber = liftNumber


    def draw(self, canvas):
        self.body = canvas.create_rectangle(self.coords, outline="black", fill="#f0b")
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
        if(self.liftNumber==1):
            self.label = canvas.create_text(self.x+150, self.y+67,font="Purisa", text="No. of Persons: "+str(noPersonLift1))
        elif(self.liftNumber==2):
            self.label = canvas.create_text(self.x+150, self.y+67,font="Purisa", text="No. of Persons: "+str(noPersonLift2))
        elif(self.liftNumber==3):
            self.label = canvas.create_text(self.x+150, self.y+67,font="Purisa", text="No. of Persons: "+str(noPersonLift3))
        elif(self.liftNumber==4):
            self.label = canvas.create_text(self.x+150, self.y+67,font="Purisa", text="No. of Persons: "+str(noPersonLift4))
         
    def update(self,canvas,liftVel,moveParameter):
        global floorRequest,lift1Request,lift2Request,lift3Request,lift4Request,noPersonLift1,noPersonLift2,noPersonLift3,noPersonLift4
        self.x = canvas.coords(self.body)[0]
        self.y = canvas.coords(self.body)[1]
        while(self.y>moveParameter):
            time.sleep(.25)
            if(self.y%108==0 and (floorRequest[10-int(self.y/108)]==1 or (self.liftNumber==1 and lift1Request[10-int(self.y/108)]==1) or (self.liftNumber==2 and lift2Request[10-int(self.y/108)]==1) or (self.liftNumber==3 and lift3Request[10-int(self.y/108)]==1) or (self.liftNumber==4 and lift4Request[10-int(self.y/108)]==1))):
                floorRequest[10-int(self.y/108)] = 0
                canvas.itemconfig(self.body, fill="green")
                canvas.update()
                time.sleep(2)
                canvas.itemconfig(self.body, fill="#f0b")
                canvas.update()
                if(self.liftNumber==1):
                    canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift1))
                elif(self.liftNumber==2):
                    canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift2))
                elif(self.liftNumber==3):
                    canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift3))
                elif(self.liftNumber==4):
                    canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift4))

                canvas.itemconfig(self.label, text="No. of Persons: ")
            canvas.move(self.body,0,liftVel)
            canvas.move(self.label,0,liftVel)
            canvas.update()
            self.currFloor = 10-math.floor(self.y/108)
            self.y = canvas.coords(self.body)[1]
        canvas.itemconfig(self.body, fill="green")
        canvas.update()
        time.sleep(2)
        canvas.itemconfig(self.body, fill="#f0b")
        canvas.update()
        if(self.liftNumber==1):
            canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift1))
        elif(self.liftNumber==2):
            canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift2))
        elif(self.liftNumber==3):
            canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift3))
        elif(self.liftNumber==4):
            canvas.itemconfig(self.label, text="No. of Persons: "+str(noPersonLift4))
        self.isMoving = False
                        

    def liftMotion(self):
        return self.isMoving

    def getCurrentFloor(self):
        return self.currFloor


class MainGUI(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")

        self.parent = parent
        self.canvas = Canvas(parent, width = screenWidth, height = screenHeight, bg = "white")
        self.canvas.pack()
        self.displayVertical()

        global floorRequest
        for i in range(11):
            floorRequest.append(0)
        for i in range(11):
            lift1Request.append(0)
        for i in range(11):
            lift2Request.append(0)
        for i in range(11):
            lift3Request.append(0)
        for i in range(11):
            lift4Request.append(0)

        self.simulate()
        self.initUI()

    def initUI(self):

        self.parent.title("Elevator Simulation System")
        self.pack(fill=BOTH, expand=1)

    def displayVertical(self):
        global screenHeight
        global screenWidth
        global shiftParameter
        global arrowParameter

        #fiveVerticalLines
        self.canvas.create_line(0, 0, 0, screenHeight, fill = "black",tags = "line")
        self.canvas.create_line(shiftParameter, 0, shiftParameter, screenHeight, fill = "black",tags = "line")
        self.canvas.create_line(2*shiftParameter, 0, 2*shiftParameter, screenHeight, fill = "black",tags = "line")
        self.canvas.create_line(3*shiftParameter, 0, 3*shiftParameter, screenHeight, fill = "black",tags = "line")
        self.canvas.create_line(4*shiftParameter, 0, 4*shiftParameter, screenHeight, fill = "black",tags = "line")

        #Ten Horizontal Lines
        self.canvas.create_line(0, floorHeight, 4*shiftParameter, floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 2*floorHeight, 4*shiftParameter, 2*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 3*floorHeight, 4*shiftParameter, 3*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 4*floorHeight, 4*shiftParameter, 4*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 5*floorHeight, 4*shiftParameter, 5*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 6*floorHeight, 4*shiftParameter, 6*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 7*floorHeight, 4*shiftParameter, 7*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 8*floorHeight, 4*shiftParameter, 8*floorHeight, fill = "black",tags = "line")
        self.canvas.create_line(0, 9*floorHeight, 4*shiftParameter, 9*floorHeight, fill = "black",tags = "line")

        #liftParameters
        lift.append(Lift(0, 972, shiftParameter, 972+floorHeight,0,1,False,1))
        lift[0].draw(self.canvas)
        lift.append(Lift(1*shiftParameter, 972, 2*shiftParameter, 972+floorHeight,0,1,False,2))
        lift[1].draw(self.canvas)
        lift.append(Lift(2*shiftParameter, 972, 3*shiftParameter, 972+floorHeight,0,1,False,3))
        lift[2].draw(self.canvas)
        lift.append(Lift(3*shiftParameter, 972, 4*shiftParameter, 972+floorHeight,0,1,False,4))
        lift[3].draw(self.canvas)


        #upArrows
        self.upf10 = Arrow(1030, 40, 1070, 40, 1050,10,name="10")
        self.upf10.draw(self.canvas)
        self.upf9 = Arrow(1030, floorHeight+40, 1070, floorHeight+40, 1050,floorHeight+10,name="9")
        self.upf9.draw(self.canvas)
        self.upf8 = Arrow(1030, floorHeight+40+108, 1070, floorHeight+40+108, 1050,floorHeight+10+108,name="8")
        self.upf8.draw(self.canvas)
        self.upf7 = Arrow(1030, 2*floorHeight+40+108, 1070, 2*floorHeight+40+108, 1050,2*floorHeight+10+108,name="7")
        self.upf7.draw(self.canvas)
        self.upf6 = Arrow(1030, 3*floorHeight+40+108, 1070, 3*floorHeight+40+108, 1050,3*floorHeight+10+108,name="6")
        self.upf6.draw(self.canvas)
        self.upf5 = Arrow(1030, 4*floorHeight+40+108, 1070, 4*floorHeight+40+108, 1050,4*floorHeight+10+108,name="5")
        self.upf5.draw(self.canvas)
        self.upf4 = Arrow(1030, 5*floorHeight+40+108, 1070, 5*floorHeight+40+108, 1050,5*floorHeight+10+108,name="4")
        self.upf4.draw(self.canvas)
        self.upf3 = Arrow(1030, 6*floorHeight+40+108, 1070, 6*floorHeight+40+108, 1050,6*floorHeight+10+108,name="3")
        self.upf3.draw(self.canvas)
        self.upf2 = Arrow(1030, 7*floorHeight+40+108, 1070, 7*floorHeight+40+108, 1050,7*floorHeight+10+108,name="2")
        self.upf2.draw(self.canvas)
        self.upf1 = Arrow(1030, 8*floorHeight+40+108, 1070, 8*floorHeight+40+108, 1050,8*floorHeight+10+108,name="1")
        self.upf1.draw(self.canvas)

        #downArrows
        self.downf10 = Arrow(1030, 50, 1070, 50, 1050,80,name="10")
        self.downf9 = Arrow(1030, floorHeight+50, 1070, floorHeight+50, 1050,floorHeight+80,name="9")
        self.downf8 = Arrow(1030, 2*floorHeight+50, 1070, 2*floorHeight+50, 1050,2*floorHeight+80,name="8")
        self.downf7 = Arrow(1030, 3*floorHeight+50, 1070, 3*floorHeight+50, 1050,3*floorHeight+80,name="7")
        self.downf6 = Arrow(1030, 4*floorHeight+50, 1070, 4*floorHeight+50, 1050,4*floorHeight+80,name="6")
        self.downf5 = Arrow(1030, 5*floorHeight+50, 1070, 5*floorHeight+50, 1050,5*floorHeight+80,name="5")
        self.downf4 = Arrow(1030, 6*floorHeight+50, 1070, 6*floorHeight+50, 1050,6*floorHeight+80,name="4")
        self.downf3 = Arrow(1030, 7*floorHeight+50, 1070, 7*floorHeight+50, 1050,7*floorHeight+80,name="3")
        self.downf2 = Arrow(1030, 8*floorHeight+50, 1070, 8*floorHeight+50, 1050,8*floorHeight+80,name="2")
        self.downf1 = Arrow(1030, 9*floorHeight+50, 1070, 9*floorHeight+50, 1050,9*floorHeight+80,name="2")
        self.downf10.draw(self.canvas)
        self.downf9.draw(self.canvas)
        self.downf8.draw(self.canvas)
        self.downf7.draw(self.canvas)
        self.downf6.draw(self.canvas)
        self.downf5.draw(self.canvas)
        self.downf4.draw(self.canvas)
        self.downf3.draw(self.canvas)
        self.downf2.draw(self.canvas)
        self.downf1.draw(self.canvas)

        self.canvas.create_text(20, 30, anchor=W, font="Purisa",text="Floor No. 10")
        self.canvas.create_text(20, 30+floorHeight, anchor=W, font="Purisa",text="Floor No. 9")
        self.canvas.create_text(20, 30+2*floorHeight, anchor=W, font="Purisa",text="Floor No. 8")
        self.canvas.create_text(20, 30+3*floorHeight, anchor=W, font="Purisa",text="Floor No. 7")
        self.canvas.create_text(20, 30+4*floorHeight, anchor=W, font="Purisa",text="Floor No. 6")
        self.canvas.create_text(20, 30+5*floorHeight, anchor=W, font="Purisa",text="Floor No. 5")
        self.canvas.create_text(20, 30+6*floorHeight, anchor=W, font="Purisa",text="Floor No. 4")
        self.canvas.create_text(20, 30+7*floorHeight, anchor=W, font="Purisa",text="Floor No. 3")
        self.canvas.create_text(20, 30+8*floorHeight, anchor=W, font="Purisa",text="Floor No. 2")
        self.canvas.create_text(20, 30+9*floorHeight, anchor=W, font="Purisa",text="Floor No. 1")

        #liftPanelOuterBoxes
        self.canvas.create_rectangle(1200, 30, 1400, 290, outline="#000", fill="#fb0")
        self.canvas.create_rectangle(1500, 30, 1700, 290, outline="#000", fill="#fb0")
        self.canvas.create_rectangle(1200, 330, 1400, 590, outline="#000", fill="#fb0")
        self.canvas.create_rectangle(1500, 330, 1700, 590, outline="#000", fill="#fb0")
        self.canvas.create_text(1250, 50, anchor=W, font="Purisa",text="Lift No. 1")
        self.canvas.create_text(1550, 50, anchor=W, font="Purisa",text="Lift No. 2")
        self.canvas.create_text(1250, 350, anchor=W, font="Purisa",text="Lift No. 3")
        self.canvas.create_text(1550, 350, anchor=W, font="Purisa",text="Lift No. 4")

        #InternalsForLiftNumber1
        Button(1220, 70, 1260, 110, 1, 1).draw(self.canvas)
        Button(1270, 70, 1310, 110, 1, 2).draw(self.canvas)
        Button(1320, 70, 1360, 110, 1, 3).draw(self.canvas)
        Button(1220, 120, 1260, 160, 1, 4).draw(self.canvas)
        Button(1270, 120, 1310, 160, 1, 5).draw(self.canvas)
        Button(1320, 120, 1360, 160, 1, 6).draw(self.canvas)
        Button(1220, 170, 1260, 210, 1, 7).draw(self.canvas)
        Button(1270, 170, 1310, 210, 1, 8).draw(self.canvas)
        Button(1320, 170, 1360, 210, 1, 9).draw(self.canvas)
        Button(1220, 220, 1260, 260, 1, 10).draw(self.canvas)
        Button(1270, 220, 1310, 260, 1, "O").draw(self.canvas)
        Button(1320, 220, 1360, 260, 1, "C").draw(self.canvas)

        #InternalsForLiftNumber3
        Button(1220, 370, 1260, 410, 3, 1).draw(self.canvas)
        Button(1270, 370, 1310, 410, 3, 2).draw(self.canvas)
        Button(1320, 370, 1360, 410, 3, 3).draw(self.canvas)
        Button(1220, 420, 1260, 460, 3, 4).draw(self.canvas)
        Button(1270, 420, 1310, 460, 3, 5).draw(self.canvas)
        Button(1320, 420, 1360, 460, 3, 6).draw(self.canvas)
        Button(1220, 470, 1260, 510, 3, 7).draw(self.canvas)
        Button(1270, 470, 1310, 510, 3, 8).draw(self.canvas)
        Button(1320, 470, 1360, 510, 3, 9).draw(self.canvas)
        Button(1220, 520, 1260, 560, 3, 10).draw(self.canvas)
        Button(1270, 520, 1310, 560, 3, "O").draw(self.canvas)
        Button(1320, 520, 1360, 560, 3, "C").draw(self.canvas)

        #InternalsForLiftNumber2
        Button(1520, 70, 1560, 110, 2, 1).draw(self.canvas)
        Button(1570, 70, 1610, 110, 2, 2).draw(self.canvas)
        Button(1620, 70, 1660, 110, 2, 3).draw(self.canvas)
        Button(1520, 120, 1560, 160, 2, 4).draw(self.canvas)
        Button(1570, 120, 1610, 160, 2, 5).draw(self.canvas)
        Button(1620, 120, 1660, 160, 2, 6).draw(self.canvas)
        Button(1520, 170, 1560, 210, 2, 7).draw(self.canvas)
        Button(1570, 170, 1610, 210, 2, 8).draw(self.canvas)
        Button(1620, 170, 1660, 210, 2, 9).draw(self.canvas)
        Button(1520, 220, 1560, 260, 2, 10).draw(self.canvas)
        Button(1570, 220, 1610, 260, 2, "O").draw(self.canvas)
        Button(1620, 220, 1660, 260, 2, "C").draw(self.canvas)

        #InternalsForLiftNumber4
        Button(1520, 370, 1560, 410,4, 1).draw(self.canvas)
        Button(1570, 370, 1610, 410,4, 2).draw(self.canvas)
        Button(1620, 370, 1660, 410,4, 3).draw(self.canvas)
        Button(1520, 420, 1560, 460,4, 4).draw(self.canvas)
        Button(1570, 420, 1610, 460,4, 5).draw(self.canvas)
        Button(1620, 420, 1660, 460,4, 6).draw(self.canvas)
        Button(1520, 470, 1560, 510,4, 7).draw(self.canvas)
        Button(1570, 470, 1610, 510,4, 8).draw(self.canvas)
        Button(1620, 470, 1660, 510,4, 9).draw(self.canvas)
        Button(1520, 520, 1560, 560,4, 10).draw(self.canvas)
        Button(1570, 520, 1610, 560,4, "O").draw(self.canvas)
        Button(1620, 520, 1660, 560,4, "C").draw(self.canvas)

        #alertBoxes
        self.canvas.create_rectangle(1200, 610, 1400, 750, outline="#000", fill="white")
        self.canvas.create_text(1250, 630, anchor=W, fill="red", font="Purisa",text="Alert Lift 1")
        self.canvas.create_rectangle(1500, 610, 1700, 750, outline="#000", fill="white")
        self.canvas.create_text(1550, 630, anchor=W, fill="red", font="Purisa",text="Alert Lift 2")
        self.canvas.create_rectangle(1200, 770, 1400, 910, outline="#000", fill="white")
        self.canvas.create_text(1250, 790, anchor=W, fill="red", font="Purisa",text="Alert Lift 3")
        self.canvas.create_rectangle(1500, 770, 1700, 910, outline="#000", fill="white")
        self.canvas.create_text(1550, 790, anchor=W, fill="red", font="Purisa",text="Alert Lift 4")

        #increment and decrement buttons
        AddRemoveButton(1710, 520, 1750, 560,4).draw(self.canvas)
        AddRemoveButton(1710, 220, 1750, 260,2).draw(self.canvas)
        AddRemoveButton(1410, 520, 1450, 560,3).draw(self.canvas)
        AddRemoveButton(1410, 220, 1450, 260,1).draw(self.canvas)


    def simulate(self):
        global floorRequest
        for i in range(11):
            if(floorRequest[i]==1):
                requestFetch = False
                for j in range (4):
                    if (lift[j].getCurrentFloor()<=i):
                        lift[j].update(self.canvas,-12,(10-i)*108)
                        floorRequest[i] = 0
                        requestFetch = True
                        break
                if(not requestFetch):
                    for j in range (4):
                        if(lift[j].getCurrentFloor()>i):
                            lift[j].update(self.canvas, -12, (10-i)*108)
                            requestFetch = True
                            floorRequest[i] = 0
                            lift[j].isMoving = True
                            break

        self.parent.after(5,self.simulate)

                        


def main():

    root = Tk()
    posx = 0
    posy = 0
    global screenWidth
    global screenHeight
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.wm_geometry("%dx%d+%d+%d" % (screenWidth, screenHeight, posx, posy))
    app = MainGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
