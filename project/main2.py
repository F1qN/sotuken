
import random
import tkinter
from PIL import Image,ImageTk

#define
WIDTH = 3100
HEIGHT = 1682.5

CHAIR_GAP = 45 #Between Chairs
TABLE_GAP = 20

CANT_PUT_Y =[2,7,12]
CANT_PUT_X =[0]
CANT_PUT   =["7-0","7-1","7-3","7-4","7-5","7-6","8-0","8-1","3-0","3-8","3-9","6-0","6-8","6-9","9-0","9-8","9-9","12-0","12-8","12-9"]
#13*15

#Conversion for Grapics
gra_WIDTH = (WIDTH/4)
gra_HEIGHT= (HEIGHT/4)
gra_CHAIR_GAP =(CHAIR_GAP/4)
gra_TABLE_GAP = (TABLE_GAP/4)
#

def CheckPut_Point(x,y):
    check = True
    for p in CANT_PUT:
        res = p.split("-")
        checkX = int(res[0])
        checkY = int(res[1])
        if(checkX==x and checkY==y):
            check = False
            break

    return check



def CheckPut(point,xy):
    check = True
    if(xy == 0):
        for num in CANT_PUT_Y:
            if(point==num):
                check = False
                break
    if(xy == 1):
        for num in CANT_PUT_X:
            if(point==num):
                check = False
                break

    return check



world = tkinter.Tk()
world.title(u"Syokudou")
world.geometry("1280x720")
canvas  = tkinter.Canvas(world,width = 1280,height=720)
canvas.create_rectangle(0,0,(gra_WIDTH),(gra_HEIGHT),fill = 'green')
img = Image.open('objset.png')
img = ImageTk.PhotoImage(img)

canvas.place(x=100,y=100)

for y in range(13):
    if (CheckPut(y,0)):
        for x in range(15):
            if(CheckPut_Point(x,y) and CheckPut(x,1)):
                canvas.create_image((x*30)+(x*gra_CHAIR_GAP),(y*30)+(y*gra_TABLE_GAP),image=img,anchor=tkinter.NW)


world.mainloop()
