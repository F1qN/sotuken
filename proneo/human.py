import random
from decimal import Decimal

class human:

    idenNum = None
    x = None
    y = None
    startTime = None
    eatPattern = None
    eatTime = None
    eatNow = None
    evaluation  = None
    individual = None

    def __init__(self,idenNum,x,y):
        self.idenNum = idenNum
        self.x = x
        self.y = y
        self.startTime = 0
        rand = random.randint(0,100)
        if(rand < 40):
            rand = random.randint(0,1)
            if(rand == 0):
                self.eatPattern = 1
            else:
                self.eatPattern = 3
        else:
            self.eatPattern = 2

        if(self.eatPattern == 1):
            self.eatTime = random.randint(6,10)
        elif(self.eatPattern == 2):
            self.eatTime = random.randint(11,15)
        elif(self.eatPattern == 3):
            self.eatTime = random.randint(16,20)
        else:
            self.eatTime = random.randint(11,15)

        self.eatNow = True
        self.evaluation = 0
        self.individual = 1

    def update(self,hm):
        if(self.eatNow):
            for h in hm:
                chkX ,chkY = h.getPoint()
                diffCha = abs(self.x-chkX) + abs(self.y-chkY)
                self.evaluation += Decimal(diffCha) * Decimal(self.individual)
            self.eatTime -= 1
            if(self.eatTime <= 0):
                self.eatNow = False
                



    def getIdenNum(self):
        return idenNum

    def getPoint(self):
        return self.x ,self.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getEvaluation(self):
        return self.evaluation

    def getEatNow(self):
        return self.eatNow

    def getEatTime(self):
        return self.eatTime

