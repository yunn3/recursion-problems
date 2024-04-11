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

    def getShapeType(self, ax, ay, bx, by, cx, cy, dx, dy):
        

    def quadrilaterals_draw(self,shape_type):
        