import random
import tkinter
import human
import DataConverter as dc
from PIL import Image,ImageTk

CELL_HIGHT = 10
CELL_WIDTH = 10

TABLE_HIGHT = 30
TABLE_WIDTH = 30

#define
WIDTH = 3100
HEIGHT = 1682.5

CHAIR_GAP = 40 #Between Chairs
TABLE_GAP = 40
CANT_PUT_Y =[2,7,12]
CANT_PUT_X =[]

CANT_PUT   =["0-0","0-1","0-2","0-3","0-4","0-5","0-6","0-7","0-8","0-9","0-10","0-11","0-12","7-0","7-1","7-3","7-4","7-5","7-6","8-0","8-1","3-0","3-8","3-9","6-0","6-8","6-9","9-0","9-8","9-9","12-0","12-8","12-9"]
ROUNDTABLE_PUT = ["3-8","6-8","9-8","12-8"]
ROUNDHALF_PUT = ["3-0","6-0","9-0","12-0"]
WINDOWTABLE_PUT = ["0-0"]
#13*15

#Conversion for Grapics
gra_WIDTH = (WIDTH/4)
gra_HEIGHT= (HEIGHT/4)
gra_CHAIR_GAP =(CHAIR_GAP/4)
gra_TABLE_GAP = (TABLE_GAP/4)
#



class ShockDoWorld :

    world = None
    canvas = None

    Table_img = None
    RoundTable_img = None
    RoundHalf_img = None
    WindowTable_img = None

    Slip = None

    humans = None

    def __init__(self):
        self.world = tkinter.Tk()
        self.world.title(u"Syokudou")
        self.world.geometry("1280x720")
        self.canvas  = tkinter.Canvas(self.world,width = 1280,height=720)
        self.canvas.create_rectangle(0,0,(gra_WIDTH),(gra_HEIGHT),fill = 'green')
        
        #画像データ読込
        self.Table_img       = Image.open('img/objset.png')
        self.RoundTable_img  = Image.open('img/round.png')
        self.RoundHalf_img   = Image.open('img/round_half.png')
        self.WindowTable_img = Image.open('img/windowtable.png')
        
        self.Table_img      = ImageTk.PhotoImage(self.Table_img)
        self.RoundTable_img = ImageTk.PhotoImage(self.RoundTable_img)
        self.RoundHalf_img  = ImageTk.PhotoImage(self.RoundHalf_img)
        self.WindowTable_img= ImageTk.PhotoImage(self.WindowTable_img)
        
        self.canvas.place(x=100,y=100)
        
        #Slip はマスの開始位置をずらす必要があるときに使う変数,Slipが表す長さ分だけ上に配置される。
        self.Slip = 0

        AbleStay = dc.data()
        self.humans = []

        for i in range(AbleStay.getLength()):
            self.humans.append(human.human(1,AbleStay.getX(i),AbleStay.getY(i)))

        self.world.after(10,self.update_humans)
    
    
    def CheckPut_Point(self,x,y,num):
        check = True
        if(num==0):
            LIST = CANT_PUT
        elif(num==1):
            LIST = ROUNDTABLE_PUT
        elif(num==2):
            LIST = ROUNDHALF_PUT
        elif(num==3):
            LIST = WINDOWTABLE_PUT
        else :
            LIST = CANT_PUT
        for p in LIST:
            res = p.split("-")
            checkX = int(res[0])
            checkY = int(res[1])
            if(checkX==x and checkY==y):
                check = False
                break
            
        return check
    
    def CheckPut(self,point,xy):
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

    def draw_grid(self):
        for i in range(42): #�Ֆʂ�\��
            for j in range(78):
                x = (CELL_WIDTH)*j
                y = (CELL_HIGHT)*i
                self.canvas.create_rectangle(x,y,x+CELL_WIDTH,y+CELL_HIGHT,outline="black") #�Ֆ�

    def draw_eatinghuman(self):
        for hm in self.humans:
            x,y = hm.getPoint()
            x *= CELL_WIDTH
            y *= CELL_HIGHT
            if(hm.getEatNow()):
                self.canvas.create_rectangle(x,y,x+CELL_WIDTH,y+CELL_HIGHT,fill="Red",tag = "hum")
                

    def draw_back(self):

        self.Slip = 0

        for y in range(13):
            if (self.CheckPut(y,0)):
                for x in range(15):
                    if(self.CheckPut_Point(x,y,0) and self.CheckPut(x,1)):
                        self.canvas.create_image((x*TABLE_WIDTH)+(x*gra_CHAIR_GAP),(y*TABLE_HIGHT)+(y*gra_TABLE_GAP)-self.Slip,image=self.Table_img,anchor=tkinter.NW)
                    elif(not self.CheckPut_Point(x,y,1)):
                        self.canvas.create_image((x*TABLE_WIDTH)+(x*gra_CHAIR_GAP),(y*TABLE_HIGHT)+(y*gra_TABLE_GAP)-self.Slip,image=self.RoundTable_img,anchor=tkinter.NW)
                    elif(not self.CheckPut_Point(x,y,2)):
                        self.canvas.create_image((x*TABLE_WIDTH)+(x*gra_CHAIR_GAP),(y*TABLE_HIGHT)+(y*gra_TABLE_GAP)-self.Slip,image=self.RoundHalf_img,anchor=tkinter.NW)
                    elif(not self.CheckPut_Point(x,y,3)):
                        self.canvas.create_image((x*TABLE_WIDTH)+(x*gra_CHAIR_GAP),(y*TABLE_HIGHT)+(y*gra_TABLE_GAP)-self.Slip,image=self.WindowTable_img,anchor=tkinter.NW)
            else :
                self.Slip+=TABLE_HIGHT
    def update_humans(self):
        self.canvas.delete("hum")
        for hm in self.humans:
            hm.update(self.humans)
            print(hm.getEvaluation())
        self.draw_eatinghuman()
        self.world.after(1000,self.update_humans)

    def update_all(self):
        self.draw_back()
        self.draw_grid()


        
        
