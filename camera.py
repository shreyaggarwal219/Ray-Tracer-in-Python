import Utilities
from vector import Vector
from ray import Ray
import math

class Camera:
    up = Vector(0,1,0)

    def __init__(self, origin, lookat, vfov, aspect_ratio):
        self.origin = origin
        self.lookat = lookat
        self.vfov = Utilities.to_Radian(vfov)
        viewport_height = 2 * math.tan(self.vfov/2)
        viewport_width = viewport_height * aspect_ratio
        self.w = Vector.unit_vector(origin - lookat)
        self.u = Vector.cross(Camera.up, self.w)
        self.v = Vector.cross(self.w, self.u)
        self.vertical = viewport_height * self.v
        self.horizontal = viewport_width * self.u
        self.upper_left = self.origin + (self.vertical / 2) - (self.horizontal / 2) - self.w

    def get_ray(self, u, v):
        return Ray(self.origin,
                   self.upper_left + self.horizontal * u - self.vertical * v - self.origin)
