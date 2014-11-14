from Tkinter import *
import time

class Testing():

    def __init__(self,main):
        self.main = main
        self.counter = 1
        self.completeTest1 = False
        self.completeTest2 = False
    
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
        elif self.counter==2 and self.completeTest1:
            print "----Test 2 Completed Successfully----"
            self.completeTest2 = True
            time.sleep(5)
        if not self.completeTest2:
            self.main.root.after(5100,self.test2)
        

    # Bug was reported during this test case not always lift number 1 was selected
    # and lift did not open in descending order so I fixed that changes made in two files lift.py and main.py
