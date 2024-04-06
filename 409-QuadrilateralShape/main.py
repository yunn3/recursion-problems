import math


class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y


class Line:

    def __init__(self, startPoint, endPoint):

        self.startPoint = startPoint
        self.endPoint = endPoint

    def getLength(self):
        # 三平方の定理を使って求める
        x_diff = self.startPoint.x - self.endPoint.x
        y_diff = self.startPoint.y - self.endPoint.y

        return math.sqrt(x_diff**2 + y_diff**2)


class QuadrilateralShape:

    def __init__(self, lineAB, lineBC, lineCD, lineDA):

        self.lineAB = lineAB
        self.lineBC = lineBC
        self.lineCD = lineCD
        self.lineDA = lineDA
