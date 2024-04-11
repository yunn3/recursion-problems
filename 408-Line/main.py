import math


class Point:

    def __init__(self, x, y):

        self.x = x
        self.y = y


class Line:

    def __init__(self, startPoint: Point, endPoint: Point):

        self.startPoint = startPoint
        self.endPoint = endPoint

    def getLength(self):
        # 三平方の定理を使って求める
        x_diff = self.startPoint.x - self.endPoint.x
        y_diff = self.startPoint.y - self.endPoint.y

        return math.sqrt(x_diff**2 + y_diff**2)


a = Point(3, 1)
b = Point(3, 6)
c = Point(1, 3)
d = Point(6, 15)

lineAB = Line(a, b)
lineCD = Line(c, d)

print(int(lineAB.getLength()))
print(int(lineCD.getLength()))
