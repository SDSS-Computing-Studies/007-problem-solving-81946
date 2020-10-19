#python3

import pyautogui as p 
import time as t
#p.mouseInfo()

#1-Set up auto clicker in one spot to click.
#2-Set up timer.
#3- After ever so often, determine blue boxes.
#4- Click all avaliable boxes.
#5- return to clicking.



point= True
times=[]
events = []





while point:
    p.click(1200,387)
    print(".", end="")


    curTime = t.time()



    times.append(curTime + 5)
    events.append('5 seconds')



    numEvents = len(events)
    index = 0

    curTime = t.time()

    for i in times:
        
        if curTime > i:
            print(events[index])
            
            times.pop(index)
            events.pop(index)
            point= False

            





      
