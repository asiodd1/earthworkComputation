class Point:#座標點物件
    def __init__(self,x,y,rH):
        #rH = realHeight,gH = goalHeight,nH = needingHeight
        self.x = x
        self.y = y
        self.rH = rH
        self.gH = goalHeight
        self.nH = self.rH-goalHeight

class Line:
    def __init__(self,pointA,pointB):
        
        if pointA.x == pointB.x:
            #0=x+b
            self.a = 1
            self.b = -pointA.x
        else:
            #y=ax+b
            self.a = (pointA.y-pointB.y)/(pointA.x-pointB.x)
            self.b = (pointA.x*pointB.y-pointB.x*pointA.y)/(pointA.x-pointB.x)

class Area:
    def __init__(self,area):
        self.area = area

def coordinateBase(wA):#將座標資料設為點物件Point並存入串列pointList
    for i in range(len(wA)):
        pointTemp = pointList.append(Point(wA[i][0],wA[i][1],wA[i][2]))

def getLine(pointList):
    i=4
    selfPoint = pointList[i]
    getRightPoint = 0
    getUpPoint = 0
    dx = 1
    dy = 1
    j = 0
    while getRightPoint == 0:
        for j in range(len(pointList)):
            if pointList[i].x + dx == pointList[j].x and pointList[i].y == pointList[j].y:
                rightSidePoint = pointList[j]
                getRightPoint = 1
                break
            else:
                pass
        dx = dx + 1
    j = 0
    while getUpPoint == 0:
        for j in range(len(pointList)):
            if pointList[i].y + dy == pointList[j].y and pointList[i].x == pointList[j].x:
                upSidePoint = pointList[j]
                getUpPoint = 1
                break
            else:
                pass
        dy = dy + 1
    return rightSidePoint,upSidePoint

goalHeight = int(input('目標高度 : '))
print('\n建立座標點物件')

wholeArea = [(0,0,111),(1100,0,100.5),(0,650,105),(1100,650,30.5),(600,275,98),(1100,275,80),(600,650,91),(950,275,80),(950,650,47),(600,0,101)]
pointList=[]
coordinateBase(wholeArea)
