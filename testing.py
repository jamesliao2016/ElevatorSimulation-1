from Tkinter import *
import time
import random

class Testing():

    def __init__(self,main):
        self.main = main
        self.counter = 1
        self.completeTest1 = False
        self.completeTest2 = False
        self.completeTest3 = False
        self.completeTest4 = False
        self.completeTest5 = False
        self.completeTest6 = False
        self.completeTest7 = False

    # Request to all the floors in ascending orders ---> 
    # To check optimality of algorithm that always lift number1 is selected 
    # and send as it is on the way and could fetch other persons    
    def test1(self):
        if self.counter<=10:
            self.main.floorRequest(self.counter,"up")
            self.counter += 1     
            self.main.root.after(5100,self.test1)
        else:
            print "----Test 1 Completed Successfully----"
            time.sleep(5)
            self.completeTest1 = True
            self.test2()
            

    # Request to all the floor in descending order when one lift was on top floor --->
    # To check the optimality of the algorithm that always lift number 1 is selected
    # and send open on every floor in descending order
    def test2(self):
        if self.counter==11:
            print "----Test 2 started----"
        if self.counter>1 and self.completeTest1:
            self.main.floorRequest(self.counter-1,"up")
            self.counter -= 1
        elif self.counter==1 and self.completeTest1:
            print "----Test 2 Completed Successfully----"
            time.sleep(5)
            self.completeTest2 = True
            self.test3()
        if not self.completeTest2:
            self.main.root.after(5100,self.test2)
        
    # Bug was reported during this test case not always lift number 1 was selected
    # and lift did not open in descending order so I fixed that changes made in two files lift.py and main.py

    
    # Request to all the floors for all the lifts are made ---->
    # Simply to check whether lifts are moving in ascending orders of floor request and stop at every floors
    def test3(self):
        if self.counter == 1:
            print "----Test 3 started----"
        if self.counter<=10:
            for lift in self.main.lift_list:
                lift.addFloorRequest(self.counter,"up")
            self.counter = self.counter + 1
        else:
            print "----Test 3 Completed Successfully----"
            time.sleep(5)
            self.completeTest3 = True
            self.test4()
        if not self.completeTest3:
            self.main.root.after(5500,self.test3)

    # Request to all the floor have been made when all the lifts were at top --->
    # This test is to check whether lifts are moving in descending order and stops at every floors
    def test4(self):
        if self.counter == 11:
            print "----Test 4 started----"
        if self.counter>1:
            for lift in self.main.lift_list:
                lift.addFloorRequest(self.counter-1,"down")
            self.counter -= 1
        else:
            print "----Test 4 Completed Successfully----"
            time.sleep(5)
            self.completeTest4 = True
            self.test5()
        if not self.completeTest4:
            self.main.root.after(5500,self.test4)

    # Randomly choose any of the one lift and make it overload ----> 
    # This is test that if one lift is overloaded then other lift should move and not that
    def test5(self):
        if self.counter == 1:
            print "----Test 5 started----"
            self.main.lift_list[0].person_count = 11
            self.main.lift_list[0].overLoaded = True
        if self.counter<=10:
            self.main.floorRequest(self.counter,"up")
            self.counter += 1
        else:
            print "----Test 5 Completed Successfully----"
            time.sleep(5)
            self.completeTest5 = True
            self.main.lift_list[0].person_count = 0
            self.main.lift_list[0].overLoaded = False
            self.test6()
        if not self.completeTest5:
            self.main.root.after(5500, self.test5)

    # Test the Lift Panel ----> If Request made from lift panel then they are fetched properly or not

    def test6(self):
        print "----Test 6 started----"
        for panels in self.main.lift_panel_list:
            for t in panels.button_list:
                t.request(1,t.floor_number)

        #self.test7()


    # Request to all the floors have been made from the requestArrow ---> 
    # This test is to check whether LEDs are glowing properly or not
    #def test7(self):
    #    if int(self.main.lift_list[0].curr_floor) == 10:
    #        self.completeTest6 = True
    #    if self.completeTest6:
    #        print "----Test 7 started----"
    #        for i in range(10):
    #            self.main.up_arrow_list[i].request(1)
    #    if not self.completeTest7
