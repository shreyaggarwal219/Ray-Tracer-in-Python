import math


class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.z}"

    def mag(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    @staticmethod
    def dot(v1, v2) -> float:
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1, v2):
        return Vector(v1.y * v2.z - v1.z * v2.y, -v1.x*v2.z + v1.z*v2.x, v1.x*v2.y - v1.y*v2.x)

    @staticmethod
    def unit_vector(vec) -> 'Vector':
        return vec / vec.mag()

    def __truediv__(self, other) -> 'Vector':
        return Vector(self.x / other, self.y / other, self.z / other)

    def __mul__(self, other) -> 'Vector':
        return Vector(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other) -> 'Vector':
        return Vector(self.x * other, self.y * other, self.z * other)

    @staticmethod
    def mulVec(vec1, vec2) -> 'Vector':
        return Vector(vec1.x * vec2.x, vec1.y * vec2.y, vec1.z * vec2.z)

    def __add__(self, other) -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other) -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    @staticmethod
    def reflect(v, n):
        return v - 2 * Vector.dot(v, n) * n

    @staticmethod
    def refract(v, n, eta):
        cos_theta = -Vector.dot(v, n)/(v.mag() * n.mag())
        r_perp = eta * (v + cos_theta*n)
        r_par = -math.sqrt(abs(1-(r_perp.mag() **2)))*n
        return r_par + r_perp

    def near_zero(self):
        s = math.e ** (-8)
        return (abs(self.x) < s) and (abs(self.y) < s) and (abs(self.z) < s)

    @staticmethod
    def dist(vec1, vec2):
        return math.sqrt((vec1.x - vec2.x) ** 2 + (vec1.y - vec2.y) ** 2 + (vec1.z - vec2.z) ** 2)


class Color(Vector):
    pass
