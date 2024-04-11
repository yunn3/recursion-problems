import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point: Point, end_point: Point) -> None:
        self.start_point = start_point
        self.end_point = end_point

    def get_length(self) -> float:
        x_diff = self.get_x_diff()
        y_diff = self.get_y_diff()
        # 三平方の定理で求める
        return math.sqrt(x_diff**2 + y_diff**2)

    # Recursion 提出用にキャメルケースのメソッドを用意
    def getLength(self) -> float:
        return self.get_length()

    def get_x_diff(self) -> float:
        return self.start_point.x - self.end_point.x

    def get_y_diff(self) -> float:
        return self.start_point.y - self.end_point.y


class QuadrilateralShape:
    def __init__(
        self,
        line_a_b: Line,
        line_b_c: Line,
        line_c_d: Line,
        line_d_a: Line,
    ) -> None:
        self.line_a_b = line_a_b
        self.line_b_c = line_b_c
        self.line_c_d = line_c_d
        self.line_d_a = line_d_a

    def getPerimeter(self) -> int:
        # 各辺の総和
        return int(
            self.line_a_b.get_length()
            + self.line_b_c.get_length()
            + self.line_c_d.get_length()
            + self.line_d_a.get_length(),
        )

    def getArea(self) -> int:
        # 求めたい四角形の面積をSする。ΔABCの面積をS1、ΔACDの面積をS2とする。
        # S = S1 + S2
        # 三角形の面積はヘロンの公式から求めてみる
        line_a_c = Line(
            self.line_a_b.start_point,
            self.line_b_c.end_point,
        )
        length_a_b = self.line_a_b.get_length()
        length_b_c = self.line_b_c.get_length()
        length_a_c = line_a_c.get_length()
        length_a_d = self.line_d_a.get_length()
        length_c_d = self.line_c_d.get_length()

        s_1 = 0.5 * (length_a_b + length_b_c + length_a_c)
        area_a_b_c = math.sqrt(
            s_1 * (s_1 - length_a_b) * (s_1 - length_b_c) * (s_1 - length_a_c),
        )
        s_2 = 0.5 * (length_a_c + length_a_d + length_c_d)
        area_a_c_d = math.sqrt(
            s_2 * (s_2 - length_a_c) * (s_2 - length_a_d) * (s_2 - length_c_d),
        )
        return int(round(area_a_b_c, 1) + round(area_a_c_d, 1))

    def __calc_dot_product(self, a: tuple, b: tuple) -> float:
        return a[0] * b[0] + a[1] * b[1]


lineA = Line(Point(4, 12), Point(0, 6))

lineB = Line(Point(0, 6), Point(4, 0))

lineC = Line(Point(4, 0), Point(8, 6))

lineD = Line(Point(8, 6), Point(4, 12))

rhombus = QuadrilateralShape(lineA, lineB, lineC, lineD)

print(rhombus.getPerimeter())  # --> 28

print(rhombus.getArea())  # --> 48


lineE = Line(Point(0, 0), Point(2, 2))

lineF = Line(Point(2, 2), Point(2, 6))

lineG = Line(Point(2, 6), Point(0, 4))

lineH = Line(Point(0, 4), Point(0, 0))

parallelogram = QuadrilateralShape(lineE, lineF, lineG, lineH)

print(parallelogram.getPerimeter())  # --> 13

print(parallelogram.getArea())  # --> 8


lineI = Line(Point(0, 0), Point(4, 0))

lineJ = Line(Point(4, 0), Point(6, 2))

lineK = Line(Point(6, 2), Point(6, 6))

lineL = Line(Point(6, 6), Point(0, 0))

trapezoid = QuadrilateralShape(lineI, lineJ, lineK, lineL)

print(trapezoid.getPerimeter())  # --> 19

print(trapezoid.getArea())  # --> 16


lineM = Line(Point(0, 4), Point(4, 10))

lineN = Line(Point(4, 10), Point(8, 4))

lineO = Line(Point(8, 4), Point(4, 0))

lineP = Line(Point(4, 0), Point(0, 4))

kite = QuadrilateralShape(lineM, lineN, lineO, lineP)

print(kite.getPerimeter())  # --> 25

print(kite.getArea())  # --> 40


lineQ = Line(Point(0, 0), Point(8, 0))

lineR = Line(Point(8, 0), Point(10, 12))

lineS = Line(Point(10, 12), Point(2, 6))

lineT = Line(Point(2, 6), Point(0, 0))

other = QuadrilateralShape(lineQ, lineR, lineS, lineT)

print(other.getPerimeter())  # --> 36

print(other.getArea())  # --> 66

"""
最終的に期待される出力
28
48
13
8
19
16
25
40
36
66
"""
