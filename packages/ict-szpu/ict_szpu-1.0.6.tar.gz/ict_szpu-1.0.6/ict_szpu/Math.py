import math

def drawRound(centerPoint:[float,float,float],radius:float,numPoints:int):
    """
    计算圆形的坐标点
    :param centerPoint:圆心坐标点
    :param radius:半径
    :param numPoints:生成点的数量
    :return:返回list[float,float,float]
    """
    points=[]
    for i in  range(numPoints):
        angleInRadians=math.pi*2/numPoints*i
        x=radius*math.sin(angleInRadians)
        y=radius*math.cos(angleInRadians)
        points.append([x+centerPoint[0],y+centerPoint[1],0+centerPoint[2]])

    return  points


def drawElliptic(center:[float,float,float],radiusX:float,radiusY:float,detalangle:float):
    """
    计算椭圆的坐标点
    :param center: 中心点
    :param radiusX: x半径
    :param radiusY: y半径
    :param detalangle: 间隔角度
    :return:返回list[float,float,float]
    """
    points=[]
    angle=0
    while angle<=math.pi*2:
        x=center[0]+radiusX*math.sin(angle)
        y=center[1]-radiusY*math.cos(angle)
        points.append([x,y,center[2]])
        angle+=detalangle

    return  points


def drawSin(center:[float,float,float],A:float,pointNum:float,cycle:int):
    """
    计算sin坐标点
    :param center: 起点原点
    :param A: y轴系数
    :param pointNum: 一个周期内点的数量（不得小于5，点越多，形状越像）
    :param cycle: 周期数
    :return:返回list[float,float,float]
    """
    points=[]
    if pointNum<=5:
        print("一个周期点数不得小于5")
        return points

    x=0
    detal=2*math.pi/pointNum
    while x<=math.pi*2*cycle:
        y=math.sin(x)*A
        points.append([x+center[0], y+center[1], center[2]])
        x+=detal

    return  points