from Tkinter import *
from button import *


class LiftPanel():

    def __init__(self,i,canvas,main):
        self.canvas = canvas
        self.main = main
        self.button_list = []

        if i%2==0:
            if(int(i/2)==0):#Lift Number 1
                self.lift_number = i
                self.canvas.create_rectangle(1200, 30, 1400, 290, outline="#000", fill="#fb0")
                self.canvas.create_text(1250, 50, anchor=W, font="Purisa",text="Lift No. 1")
                self.coords = (1410, 220, 1450, 260)
                self.coords1 = (1410,220-50,1450,260-50)
                self.addButton = canvas.create_oval(self.coords, outline="black", fill="white", width=2)
                self.canvas.tag_bind(self.addButton,'<Button-1>', lambda x: self.addPerson(1))
                self.removeButton = canvas.create_oval(self.coords1, outline="black", fill="white", width=2)
                self.canvas.tag_bind(self.removeButton,'<Button-1>', lambda x: self.removePerson(1))
                self.buttonPlus = canvas.create_text(self.coords[0]+15, self.coords[1]+20, anchor=W, font="Purisa",text="+")
                self.canvas.tag_bind(self.buttonPlus,'<Button-1>', lambda x: self.addPerson(1))
                self.buttonMinus = canvas.create_text(self.coords1[0]+15, self.coords1[1]+20, anchor=W, font="Purisa",text="-")
                self.canvas.tag_bind(self.buttonMinus,'<Button-1>', lambda x: self.removePerson(1))
                for i in range(3):
                    for j in range(3):
                        coords = (1220+j*50, 70+i*50, 1260+j*50, 110+i*50)
                        self.button_list.append(Button(coords,self.lift_number,3*i+1*(j+1),self.main,self.canvas))

                coords = (1220, 220, 1260, 260)
                self.button_list.append(Button(coords,self.lift_number,10,self.main,self.canvas))
                coords = (1270, 220, 1310, 260)
                Button(coords,self.lift_number,"<>",self.main,self.canvas)
                coords = (1320, 220, 1360, 260)
                Button(coords,self.lift_number,"><",self.main,self.canvas)


            else:#Lift Number 3
                self.lift_number = i
                self.canvas.create_rectangle(1200, 30+300, 1400, 290+300, outline="#000", fill="#fb0")
                self.canvas.create_text(1250, 350, anchor=W, font="Purisa",text="Lift No. 3")
                self.coords = (1410, 520, 1450, 560)
                self.coords1 = (1410, 520-50, 1450, 560-50)
                self.addButton = canvas.create_oval(self.coords, outline="black", fill="white", width=2)
                self.removeButton = canvas.create_oval(self.coords1, outline="black", fill="white", width=2)
                self.buttonPlus = canvas.create_text(self.coords[0]+15, self.coords[1]+20, anchor=W, font="Purisa",text="+")
                self.buttonMinus = canvas.create_text(self.coords1[0]+15, self.coords1[1]+20, anchor=W, font="Purisa",text="-")
                self.canvas.tag_bind(self.addButton,'<Button-1>', lambda x: self.addPerson(1))
                self.canvas.tag_bind(self.removeButton,'<Button-1>', lambda x: self.removePerson(1))
                self.canvas.tag_bind(self.buttonPlus,'<Button-1>', lambda x: self.addPerson(1))
                self.canvas.tag_bind(self.buttonMinus,'<Button-1>', lambda x: self.removePerson(1))
                for i in range(3):
                    for j in range(3):
                        coords = (1220+j*50, 370+i*50, 1260+j*50, 410+i*50)
                        self.button_list.append(Button(coords,self.lift_number,3*i+1*(j+1),self.main,self.canvas))

                coords = (1220, 520, 1260, 560)
                self.button_list.append(Button(coords,self.lift_number,10,self.main,self.canvas))
                coords = (1270, 520, 1310, 560)
                Button(coords,self.lift_number,"<>",self.main,self.canvas)
                coords = (1320, 520, 1360, 560)
                Button(coords,self.lift_number,"><",self.main,self.canvas)
        
        else:
            if(int(i/2)==0):#Lift Number 2
                self.lift_number = i
                self.canvas.create_rectangle(1500, 30, 1700, 290, outline="#000", fill="#fb0")
                self.canvas.create_text(1550, 50, anchor=W, font="Purisa",text="Lift No. 2")
                self.coords = (1710, 220, 1750, 260)
                self.coords1 = (1710, 220-50, 1750, 260-50)
                self.addButton = canvas.create_oval(self.coords, outline="black", fill="white", width=2)
                self.removeButton = canvas.create_oval(self.coords1, outline="black", fill="white", width=2)
                self.buttonPlus = canvas.create_text(self.coords[0]+15, self.coords[1]+20, anchor=W, font="Purisa",text="+")
                self.buttonMinus = canvas.create_text(self.coords1[0]+15, self.coords1[1]+20, anchor=W, font="Purisa",text="-")
                self.canvas.tag_bind(self.addButton,'<Button-1>', lambda x: self.addPerson(1))
                self.canvas.tag_bind(self.removeButton,'<Button-1>', lambda x: self.removePerson(1))
                self.canvas.tag_bind(self.buttonPlus,'<Button-1>', lambda x: self.addPerson(1))
                self.canvas.tag_bind(self.buttonMinus,'<Button-1>', lambda x: self.removePerson(1))
                for i in range(3):
                    for j in range(3):
                        coords = (1520+j*50, 70+i*50, 1560+j*50, 110+i*50)
                        self.button_list.append(Button(coords,self.lift_number,3*i+1*(j+1),self.main,self.canvas))

                coords = (1520, 220, 1560, 260)
                self.button_list.append(Button(coords,self.lift_number,10,self.main,self.canvas))
                coords = (1570, 220, 1610, 260)
                Button(coords,self.lift_number,"<>",self.main,self.canvas)
                coords = (1620, 220, 1660, 260)
                Button(coords,self.lift_number,"><",self.main,self.canvas)

            
            else:#Lift Number 4
                self.lift_number = i
                self.canvas.create_rectangle(1500, 330, 1700, 590, outline="#000", fill="#fb0")
                self.canvas.create_text(1550, 350, anchor=W, font="Purisa",text="Lift No. 4") 
                self.coords = (1710, 520, 1750, 560)
                self.coords1 = (1710, 520-50, 1750, 560-50)
                self.addButton = canvas.create_oval(self.coords, outline="black", fill="white", width=2)
                self.removeButton = canvas.create_oval(self.coords1, outline="black", fill="white", width=2)
                self.buttonPlus = canvas.create_text(self.coords[0]+15, self.coords[1]+20, anchor=W, font="Purisa",text="+")
                self.buttonMinus = canvas.create_text(self.coords1[0]+15, self.coords1[1]+20, anchor=W, font="Purisa",text="-")
                self.canvas.tag_bind(self.addButton,'<Button-1>', lambda x: self.addPerson(1))
                self.canvas.tag_bind(self.removeButton,'<Button-1>', lambda x: self.removePerson(1))
                self.canvas.tag_bind(self.buttonPlus,'<Button-1>', lambda x: self.addPerson(1))
                self.canvas.tag_bind(self.buttonMinus,'<Button-1>', lambda x: self.removePerson(1))
                for i in range(3):
                    for j in range(3):
                        coords = (1520+j*50, 370+i*50, 1560+j*50, 410+i*50)
                        self.button_list.append(Button(coords,self.lift_number,3*i+1*(j+1),self.main,self.canvas))

                coords = (1520, 520, 1560, 560)
                self.button_list.append(Button(coords,self.lift_number,10,self.main,self.canvas))
                coords = (1570, 520, 1610, 560)
                Button(coords,self.lift_number,"<>",self.main,self.canvas)
                coords = (1620, 520, 1660, 560)
                Button(coords,self.lift_number,"><",self.main,self.canvas)

    def addPerson(self,event):
        if not(self.main.lift_list[self.lift_number].state == "moving"):
            if self.main.lift_list[self.lift_number].state == "closing" or self.main.lift_list[self.lift_number].state == "idle":
                self.main.lift_list[self.lift_number].state = "opening"
                self.main.lift_list[self.lift_number].person_count = self.main.lift_list[self.lift_number].person_count+1

    def removePerson(self,event): 
        if not(self.main.lift_list[self.lift_number].state == "moving"):
            if self.main.lift_list[self.lift_number].state == "closing" or self.main.lift_list[self.lift_number].state == "idle":
                self.main.lift_list[self.lift_number].state = "opening"
                if self.main.lift_list[self.lift_number].person_count > 0:
                    self.main.lift_list[self.lift_number].person_count = self.main.lift_list[self.lift_number].person_count-1

