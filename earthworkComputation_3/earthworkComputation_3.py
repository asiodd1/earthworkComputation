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

class Area:#每塊矩形設為一個面積物件，以左下點為面積物件位置座標點，
    def __init__(self,pointA,i):
        self.Location = (pointA.x,pointA.y)
        try:
            self.area = (partnerPoint[i][0].x - pointList[i].x) * (partnerPoint[i][1].y - pointList[i].y)
        except Exception:
            self.area = 0
        else:
            pass
        finally:
            #print("第 %d 點: "%i,end=' ')
            #print(self.Location,end=' ')
            #print('area is %d'%self.area)
            pass
        if self.area > 0:
            self.volume = self.area * (pointList[i].nH + partnerPoint[i][0].nH + partnerPoint[i][1].nH + partnerPoint[i][2].nH)/4
        else:
            self.volume = 0

def coordinateBase(wA):#將座標資料設為點物件Point並存入串列pointList
    for i in range(len(wA)):
        pointList.append(Point(wA[i][0],wA[i][1],wA[i][2]))

def findPartnerPoint(i, pointList):#找到相鄰三點，右點、上點、右上點，若無則回傳None
    selfPoint = pointList[i]
    getRightPoint = 0
    getUpPoint = 0
    getDiagonalPoint = 0
    dx = 1
    dy = 1
    j = 0
    while dx <= (max([pointList[k].x for k in range(len(pointList))])-min([pointList[k].x for k in range(len(pointList))])):
        for j in range(len(pointList)):
            if pointList[i].x + dx == pointList[j].x and pointList[i].y == pointList[j].y:
                rightSidePoint = pointList[j]
                getRightPoint = 1
                break
            else:
                rightSidePoint = None
                pass
        dx = dx + 1
        if rightSidePoint != None :
            break
        else:
            pass
    j = 0
    while getUpPoint == 0:
        for j in range(len(pointList)):
            if pointList[i].y + dy == pointList[j].y and pointList[i].x == pointList[j].x:
                upSidePoint = pointList[j]
                getUpPoint = 1
                break
            elif dy > (max([pointList[k].y for k in range(len(pointList))])-min([pointList[k].y for k in range(len(pointList))])):
                upSidePoint = None
                getUpPoint = 1
            else:
                pass
        dy = dy + 1
    j = 0
    #if point is None, first solution
    '''while getDiagonalPoint == 0:
        for j in range(len(pointList)):
            if rightSidePoint == None or upSidePoint == None:
                diagonalPoint = None
                getDiagonalPoint = 1
            elif pointList[j].x == rightSidePoint.x and pointList[j].y == upSidePoint.y:
                diagonalPoint = pointList[j]
                getDiagonalPoint = 1
            else:
                pass'''
    #second solution
    '''while getDiagonalPoint == 0:

        try:
            for j in range(len(pointList)):
                if pointList[j].x == rightSidePoint.x and pointList[j].y == upSidePoint.y:
                    diagonalPoint = pointList[j]
                else:
                    pass
        except AttributeError as error:
                diagonalPoint = None
        else:
            pass
        finally:
            getDiagonalPoint = 1'''
    #third solution
    try:
        for j in range(len(pointList)):
            if pointList[j].x == rightSidePoint.x and pointList[j].y == upSidePoint.y:
                diagonalPoint = pointList[j]
            else:
                pass
    except AttributeError as error:
        diagonalPoint = None
    else:
        pass
    finally:
        pass
    return rightSidePoint,upSidePoint,diagonalPoint

def findGoalHeightPoint():
    goalHeightPoint=[]
    for i in range(len(pointList)):
        try:
            if pointList[i].nH * partnerPoint[i][0].nH <= 0:
                goalHeightPoint.append(Point(pointList[i].x+int((partnerPoint[i][0].x-pointList[i].x)*abs(pointList[i].nH)/(abs(pointList[i].nH)+abs(partnerPoint[i][0].nH))),pointList[i].y,goalHeight))
                print(i,1)
            else:
                pass
            if pointList[i].nH * partnerPoint[i][1].nH <= 0:
                goalHeightPoint.append(Point(pointList[i].x,pointList[i].y+int((partnerPoint[i][1].y-pointList[i].y)*abs(pointList[i].nH)/(abs(pointList[i].nH)+abs(partnerPoint[i][1].nH))),goalHeight))
                print(i,2)
            else:
                pass
            if partnerPoint[i][0].nH * partnerPoint[i][2].nH <= 0:
                goalHeightPoint.append(Point(partnerPoint[i][0].x,partnerPoint[i][0].y+int((partnerPoint[i][2].y-partnerPoint[i][0].y)*abs(partnerPoint[i][0].nH)/(abs(partnerPoint[i][0].nH)+abs(partnerPoint[i][2].nH))),goalHeight))
                print(i,3)
            else:
                pass
            if partnerPoint[i][1].nH * partnerPoint[i][2].nH <= 0:
                goalHeightPoint.append(Point(partnerPoint[i][1].x+int((partnerPoint[i][2].x-partnerPoint[i][1].x)*abs(partnerPoint[i][1].nH)/(abs(partnerPoint[i][1].nH)+abs(partnerPoint[i][2].nH))),partnerPoint[i][1].y,goalHeight))
                print(i,4)
            else:
                pass
        except:
            pass
    return goalHeightPoint#有些線段會重複計算導致有同一線段出現許多同點物件，甚至有同一線段因為兩次基準點不同而出現不同的零高點物件
###
goalHeight = float(input('目標高度 : '))

print('\n輸入座標點及高程')
wholeArea = [(0,0,111),(1100,0,100.5),(0,650,105),(1100,650,30.5),(600,275,98),(1100,275,80),(600,650,91),(950,275,80),(950,650,47),(600,0,101)]

pointList=[]
coordinateBase(wholeArea)
pointList = tuple(pointList)#存好點物件後先將pointList改成tuple以免後續動到

partnerPoint={}
for i in range(len(pointList)):
    partnerPoint[i] = findPartnerPoint(i,pointList)

lineSet=set()
for i in range(len(pointList)):
    if partnerPoint[i][0] != None:
        lineSet.add((pointList[i],partnerPoint[i][0]))
    if partnerPoint[i][1] != None:
        lineSet.add((pointList[i],partnerPoint[i][1]))
    if partnerPoint[i][2] != None:
        lineSet.add((partnerPoint[i][0],partnerPoint[i][2]))
        lineSet.add((partnerPoint[i][1],partnerPoint[i][2]))
