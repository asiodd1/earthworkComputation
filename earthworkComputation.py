class Point:
    def __init__(self,x,y,rH):
        #rH = realHeight,gH = goalHeight,nH = needingHeight
        self.x = x
        self.y = y
        self.rH = rH
        self.gH = goalHeight
        self.nH = self.rH-goalHeight

class Line:
    def __init__(self,pointA,pointB):
        #y=ax+b
        self.a = (pointA.y-pointB.y)/(pointA.x-pointB.x)
        self.b = (pointA.x*pointB.y-pointB.x*pointA.y)/(pointA.x-pointB.x)

class Area:
    def __init__(self,area):
        self.area = area

def coodinateBase(wA):
    for i in range(len(wA)):
        pointTemp = pointList.append(Point(wA[i][0],wA[i][1],wA[i][2]))

def getLine():
    if pointList[i].

goalHeight = int(input('目標高度 : '))
print('\n建立座標點物件')

wholeArea = [(0,0,111),(1100,0,100.5),(0,650,105),(1100,650,30.5)]
pointList=[]
