#python3

import pyautogui as p 
import time as t

#p.mouseInfo()

#1-Set up auto clicker in one spot to click  (Main clicking).
#2-Timer of about 15sec will then stop main clicking.
#3- Click Research tab.
#4- Click all avaliable boxes.
#5- Click Upgrades tab.
#6= Click all avliable boxes.
#6.5- Note* Upgrades needs to go first other wise if HR goes first, upgrades will have no JTN to purchase. If upgrades goes first, more likely ther ewill be JTN left over.
#7- Click HR tab.
#8- Click all avaliable boxes.
#9- Return to clicking main point
#Game- https://particle-clicker.web.cern.ch/
#(1906,1001) bottom
#(1911,218) Top

def Research():
    finger=True
    times=[]
    events= []

    print("========================")
    print("Now buying from Research")
    print("========================")

    p.click(1490,181)
    p.click((1911,218)) #UP
    while finger:
        Data= p.locateCenterOnScreen('Gears.png')
        p.click(Data)
        print(".", end="")
        curTime = t.time()
        times.append(curTime + 5)
        events.append('Part1 : Success')
        numEvents = len(events)
        index = 0
        curTime = t.time()
        for i in times:
                if curTime > i:
                    print(events[index])
                    times.pop(index)
                    events.pop(index)
                    Upgrades()



#p.click(1906,1001) #Down



def Upgrades():
    finger3=True
    times=[]
    events= []

    print("========================")
    print("Now buying from Upgrades")
    print("========================")

    p.click(1666,166)
    while finger3:
        Upgrades= p.locateCenterOnScreen('Money.png')
        p.click(Upgrades)
        print(".", end="")


        curTime = t.time()



        times.append(curTime + 15)
        events.append('Success')



        numEvents = len(events)
        index = 0

        curTime = t.time()

        for i in times:
        
            if curTime > i:
                print(events[index])
            
                times.pop(index)
                events.pop(index)
                finger3=False

                JTN()

    
def JTN():
    finger2=True
    times=[]
    events= []
    print("==================")
    print("Now buying from HR")
    print("==================")


    p.click(1590,170)
    while finger2:
        JTN= p.locateCenterOnScreen('Person icon.png')
        p.click(JTN)
        print(".", end="")


        curTime = t.time()



        times.append(curTime + 15)
        events.append('Success')



        numEvents = len(events)
        index = 0

        curTime = t.time()

        for i in times:
        
            if curTime > i:
                print(events[index])
            
                times.pop(index)
                events.pop(index)
                finger2= False
                click()
    
    


def click():
    print("=================")
    print("Now auto clicking")
    print("=================")
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
            
                Research()






click()





    






      
