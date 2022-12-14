from ray import TempRec, Ray
from material import *
import Utilities


# Light Objects
class Light:
    def __init__(self, pos, color, intensity):
        self.pos = pos  # Light Position
        self.color = color  # Light Color
        self.intensity = intensity  # Light Intensity

    def scatter(self, rec, cam):
        return Color(0, 0, 0)  # Radiance by Light


class DirectionLight(Light):
    def __init__(self, pos, direction, color, intensity):
        super().__init__(pos, color, intensity)
        self.direction = direction

    def scatter(self, rec, cam):
        return Blinn(self, rec, cam, self.direction)


class PointLight(Light):
    def __init__(self, pos, color, intensity):
        super().__init__(pos, color, intensity)

    def scatter(self, rec, cam):
        return Blinn(self, rec, cam, rec.p - self.pos) / (Vector.dist(self.pos, rec.p) ** 2)


class SpotLight(Light):
    def __init__(self, pos, direction, totalwidth, falloffwidth, color, intensity):
        super().__init__(pos, color, intensity)
        self.direction = direction
        self.totalwidth = totalwidth
        self.falloffwidth = falloffwidth

    def scatter(self, rec, cam):
        point_dir = rec.p - self.pos
        cos_theta = Vector.dot(point_dir, self.direction) / (point_dir.mag() * self.direction.mag())
        theta = 2 * math.acos(cos_theta)
        falloff = 0
        if theta > self.totalwidth:
            falloff = 0
        elif theta < self.falloffwidth:
            falloff = 1
        else:
            falloff = (self.totalwidth - theta) / (self.totalwidth - self.falloffwidth)
        return (Blinn(self, rec, cam, self.direction) * falloff) / (Vector.dist(self.pos, rec.p) ** 2)


class LightObjects:
    def __init__(self, soft_shadows):
        self.lights = []
        self.soft_shadows = soft_shadows  # Soft Shadows

    def add(self, light):
        self.lights.append(light)  # Add Lights to the list

    def lightColor(self, rec, objects, cam):
        lightColor = Color(0, 0, 0)
        for light in self.lights:
            rec2 = TempRec()
            for obj in objects:
                rec2 = obj.intersect(Ray(rec.p, light.pos - rec.p + Utilities.RandomInSphere() * self.soft_shadows), rec2)
                s = 1  # Shadow Term
                if rec2.hashit:
                    s = 0
            lightColor += s * (light.scatter(rec, cam))
        return lightColor
