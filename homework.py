# Connecting satellites
#Calculate the end time when next > no_of_sats and print the time you took to complete the game in the screen as a text
import pgzrun
import random
from time import time
start=0
total=0
end=0
start=time()

WIDTH=600
HEIGHT=500
no_of_sat=10
sats=[]
lines=[]
next=0

for i in range(no_of_sat):
    sattalite=Actor("sattalite")
    sattalite.x=random.randint(10,590)
    sattalite.y=random.randint(1,490)
    sats.append(sattalite)
def draw():
    global total
    screen.blit("galaxy",(0,0))
    number=1
    for i in sats:
        i.draw()
        screen.draw.text(str(number),(i.x,i.y+10))
        number=number+1
    for i in lines:
        screen.draw.line(i[0],i[1],"cyan")
    if next< no_of_sat:
        total=time()-start
        total=round(total,2)
        screen.draw.text(str(total),(10,10))
def on_mouse_down(pos):
    global sats,lines,next
    if next<no_of_sat:
        if sats[next].collidepoint(pos):
            if next:
                p1=sats[next-1].pos
                p2=sats[next].pos
                lines.append((p1,p2))
            next=next+1
            print(lines)
        else:
            lines=[]
            next=0
pgzrun.go()