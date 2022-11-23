from geometry import Geometry
from ray import *
from aabb import *
import copy


class BVH(Geometry):
    def __init__(self, start, end, objects):
        super().__init__()
        self.left = None
        self.right = None
        self.box = None
        object_span = end - start
        temp_objects = copy.copy(objects)
        if object_span == 1:
            self.left = objects[start]
            self.right = objects[start]
        elif object_span == 2:
            self.left = objects[start]
            self.right = objects[start + 1]
        else:
            temp_objects.sort(key=lambda x: x.origin.x)
            mid = (int)(start + object_span / 2)
            self.left = BVH(start, mid, temp_objects)
            self.right = BVH(mid, end, temp_objects)

        self.box = surrounding_box(self.left.box, self.right.box)

    def intersect(self, ray, rec):
        rec = self.box.intersect(ray, rec)
        if not rec.hashit:
            return rec
        if self.left is None or self.right is None:
            return rec
        rec = self.left.intersect(ray, rec)
        rec = self.right.intersect(ray, rec)
        return rec

    def bounding_box(self):
        return self.box
