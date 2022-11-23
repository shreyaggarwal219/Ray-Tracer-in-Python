from vector import *
from ray import Ray


class AABB():
    def __init__(self, minimum: Vector, maximum: Vector):
        super().__init__()
        self.minimum = minimum
        self.maximum = maximum

    def intersect(self, ray, rec):
        tmin = rec.min
        tmax = rec.max
        t0 = min((self.minimum.x - ray.origin.x) / ray.direction.x, (self.maximum.x - ray.origin.x) / ray.direction.x)
        t1 = max((self.minimum.x - ray.origin.x) / ray.direction.x, (self.maximum.x - ray.origin.x) / ray.direction.x)
        tmin = max(tmin, t0)
        tmax = min(tmax, t1)
        t0 = min((self.minimum.y - ray.origin.y) / ray.direction.y, (self.maximum.y - ray.origin.y) / ray.direction.y)
        t1 = max((self.minimum.y - ray.origin.y) / ray.direction.y, (self.maximum.y - ray.origin.y) / ray.direction.y)
        tmin = max(tmin, t0)
        tmax = min(tmax, t1)
        t0 = min((self.minimum.z - ray.origin.z) / ray.direction.z, (self.maximum.z - ray.origin.z) / ray.direction.z)
        t1 = max((self.minimum.z - ray.origin.z) / ray.direction.z, (self.maximum.z - ray.origin.z) / ray.direction.z)
        tmin = max(tmin, t0)
        tmax = min(tmax, t1)
        if tmin >= tmax:
            return rec
        rec.hashit = True
        return rec


def surrounding_box(box0: AABB, box1: AABB):
    small_point = Vector(min(box0.minimum.x, box1.minimum.x),
                         min(box0.minimum.y, box1.minimum.y),
                         min(box0.minimum.z, box1.minimum.z))
    big_point = Vector(max(box0.maximum.x, box1.maximum.x),
                       max(box0.maximum.y, box1.maximum.y),
                       max(box0.maximum.z, box1.maximum.z))
    return AABB(small_point, big_point)
