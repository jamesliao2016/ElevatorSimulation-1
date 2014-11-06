from Tkinter import *
import time
import math
from lift import *
from liftPanel import *
from requestArrow import *
from display import *
from alertBox import *

screen_width = 0
screen_height = 0
shift_parameter = 250
floor_height = 108
lift_parameter = 972

class ElevatorApp():
    def __init__(self,root):
        global screen_width,screen_height
        self.root = root
        self.root.title("Elevator Simulation System")
        self.canvas = Canvas(self.root, width = screen_width, height = screen_height, bg = "white")
        self.canvas.pack()
        
        #Vertical Lines
        for i in range(5):
            self.canvas.create_line(i*shift_parameter, 0, i*shift_parameter, screen_height, fill = "black",tags = "line")

        #Horizontal Lines
        for i in range(9):
            self.canvas.create_line(0, (i+1)*floor_height, 4*shift_parameter, (i+1)*floor_height, fill = "black",tags = "line")

        self.draw_lifts(self.canvas)

        #Floor Labelling
        for i in range(10):
            self.canvas.create_text(20, 30+i*floor_height, anchor=W, font="Purisa",text="Floor No. "+str(10-i))
        
        #liftPanelOuterBoxes
        self.draw_panels(self.canvas)

        #alertBoxes

        Alert(1200, 610, 1400, 750, self.canvas,self,1) 
        Alert(1500, 610, 1700, 750, self.canvas,self,2)
        Alert(1200, 770, 1400, 910, self.canvas,self,3)
        Alert(1500, 770, 1700, 910, self.canvas,self,4)
        
        #draw Alert Boxes
        self.draw_alert_box()
        
        #draw Request Arrow
        self.draw_requestArrow(self.canvas)

        #draw Display Panel
        self.draw_display(self.canvas)
        
    def draw_alert_box(self):
        self.alert_box_list = []
        
        self.alert_box_list.append(Alert(1200, 610, 1400, 750, self.canvas,self,1)) 
        self.alert_box_list.append(Alert(1500, 610, 1700, 750, self.canvas,self,2))
        self.alert_box_list.append(Alert(1200, 770, 1400, 910, self.canvas,self,3))
        self.alert_box_list.append(Alert(1500, 770, 1700, 910, self.canvas,self,4))

    def draw_display(self,canvas):
        self.display_box = []
        for i in range (10):
            self.display_box.append(Display(1100, 30+i*108, 1180, 70+i*108, canvas,self))    

    def draw_lifts(self,canvas):
        self.lift_list = []
        for k in range(4):
            self.lift_list.append(Lift(k*shift_parameter, lift_parameter, (k+1)*shift_parameter, lift_parameter+floor_height,canvas,k+1,self))
    
    def draw_panels(self,canvas):
        self.lift_panel_list = []
        for i in range (4):
            self.lift_panel_list.append(LiftPanel(i,self.canvas,self)) 

    def draw_requestArrow(self,canvas):
        self.up_arrow_list = []
        self.down_arrow_list = []
        for i in range(10):
            self.up_arrow_list.append(Arrow(1030, i*floor_height+40, 1070, i*floor_height+40, 1050,i*floor_height+10,canvas,10-i,"up",self))
            self.down_arrow_list.append(Arrow(1030, i*floor_height+50, 1070, i*floor_height+50, 1050,i*floor_height+80,canvas,10-i,"down",self))
            

    def simulate(self):

        for lift in self.lift_list:
            lift.update()

        for t in self.display_box:
            t.update()

        for a in self.alert_box_list:
            a.update()

        self.root.after(10,self.simulate)

    def floorRequest(self,floor_number,direction):
        print "Request for floor number "+str(floor_number)+" has been made"

        assigned_elevator = None

        for lift in self.lift_list:
            if(lift.curr_floor == floor_number and not lift.overLoaded):
                assigned_elevator = lift
                lift.addFloorRequest(floor_number,direction)
                print "Lift on the same floor as requested " + str(lift.lift_number)
                return

        for lift in self.lift_list:
            if (lift.state == "moving" or lift.state == "opening" or lift.state == "closing" or lift.state == "open") and lift.direction == "up" and lift.curr_floor < floor_number and not lift.overLoaded:
                assigned_elevator = lift
                lift.addFloorRequest(floor_number, direction)
                print "This lift is on the way and picked up other passengers too "+ str(lift.lift_number)
                return
            elif (lift.state == "moving" or lift.state == "opening" or lift.state == "closing" or lift.state == "open") and lift.direction == "down" and lift.curr_floor > floor_number and not lift.overLoaded:
                assigned_elevator = lift
                lift.addFloorRequest(floor_number, direction)
                print "This lift is moving and on the way catch up other persons too " + str(lift.lift_number)
                return

        min_distance = 10
        
        for lift in self.lift_list:
            if lift.state == "idle":
                if abs(lift.curr_floor - floor_number)<min_distance and not lift.overLoaded:
                    assigned_elevator = lift
                    min_distance = lift.curr_floor - floor_number

        if not(assigned_elevator == None):
            assigned_elevator.addFloorRequest(floor_number,direction)
            print "All lift were idle so nearest lift is find out and send "+ str(assigned_elevator.lift_number)
            return

        min_person = 10000000000
        if assigned_elevator == None:
            for lift in self.lift_list:
                if lift.person_count<min_person:
                    min_person = lift.person_count
                    assigned_elevator = lift

        if not(assigned_elevator == None):
            assigned_elevator.addFloorRequest(floor_number,direction)
            print "All lift were full so lift with minimum number of person was picked and assigined "+ str(assigned_elevator.lift_number)
            return


def main():

    root = Tk()
    posx = 0
    posy = 0
    global screen_width
    global screen_height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.wm_geometry("%dx%d+%d+%d" % (screen_width, screen_height, posx, posy))
    app = ElevatorApp(root)
    app.simulate()
    root.mainloop()


if __name__ == '__main__':
    main()