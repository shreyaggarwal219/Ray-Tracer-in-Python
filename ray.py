import math

from vector import *


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def point_at(self, t):
        return self.origin + self.direction * t


class TempRec:
    def __init__(self):
        self.min = 0.001
        self.max = math.inf
        self.t = math.inf
        self.p = -1
        self.normal = Vector(0, 0, 0)
        self.tangent = Vector(0,0,0)
        self.bitangent = Vector(0,0,0)
        self.hashit = False
        self.mat = None
        self.front_face = False
        self.emit = Color(0,0,0)
        self.u = 0
        self.v = 0

    def set_face_normal(self, ray):
        if Vector.dot(self.normal,ray.direction) >= 0:
            self.front_face = False
            return False
        return True

