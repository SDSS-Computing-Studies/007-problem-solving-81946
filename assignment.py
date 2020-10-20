#python3

import pyautogui as p 
import time as t

p.mouseInfo()

#1-Set up auto clicker in one spot to click.
#2-Set up timer.
#3- After ever so often, determine blue boxes.
#4- Click all avaliable boxes.
#5- return to clicking.
#Game- https://particle-clicker.web.cern.ch/




def blue(x):
    finger=True
    times=[]
    events= []
    x=1
    if x==1:
        p.click(1590,170)
        while finger:
            JTN= p.locateCenterOnScreen('Person icon.png')
            p.click(JTN)
            print(".", end="")


            curTime = t.time()



            times.append(curTime + 120)
            events.append('120 seconds')



            numEvents = len(events)
            index = 0

            curTime = t.time()

            for i in times:
        
                if curTime > i:
                    print(events[index])
            
                    times.pop(index)
                    events.pop(index)
                    finger= False



                    click()

    
    
    
    


def click():
    point= True
    times=[]
    events = []
    x=0
    while point:
        p.click(1200,387)
        print(".", end="")


        curTime = t.time()



        times.append(curTime + 15)
        events.append('15 seconds')



        numEvents = len(events)
        index = 0

        curTime = t.time()

        for i in times:
        
            if curTime > i:
                print(events[index])
            
                times.pop(index)
                events.pop(index)
                point= False
            
                blue(x)






click()





    






      
