import Utilities
from vector import Vector
from ray import Ray
import math


class Camera:
    up = Vector(0, 1, 0)                                                # Camera Up Axis

    def __init__(self, origin, lookat, vfov, aspect_ratio):
        # Positionable Camera
        self.origin = origin                                            # Camera Origin
        self.lookat = lookat                                            # Point where Camera looks
        self.vfov = Utilities.to_Radian(vfov)                           # Vertical Field of View
        # Viewport
        viewport_height = 2 * math.tan(self.vfov / 2)                   # Viewport Height
        viewport_width = viewport_height * aspect_ratio                 # Viewport Width
        # Camera Basis Vector
        self.w = Vector.unit_vector(origin - lookat)
        self.u = Vector.unit_vector(Vector.cross(Camera.up, self.w))
        self.v = Vector.unit_vector(Vector.cross(self.w, self.u))
        # Viewport Vectors
        self.vertical = viewport_height * self.v
        self.horizontal = viewport_width * self.u
        self.upper_left = self.origin + (self.vertical / 2) - (self.horizontal / 2) - self.w    # Upper Leeft Corner of the Viewport

    def get_ray(self, u, v):
        return Ray(self.origin,
                   self.upper_left + self.horizontal * u - self.vertical * v - self.origin)
