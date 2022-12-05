from vector import *
from aabb import *
import math


class Geometry:
    def __init__(self):
        self.objects = []

    def add(self, obj):
        self.objects.append(obj)

    def bounding_box(self):
        pass

    def intersect(self, ray, rec):
        pass

    def get_uv(self, p):
        pass


class Sphere(Geometry):
    def __init__(self, origin, radius, mat, isemissive=False):
        super().__init__()
        self.origin = origin
        self.radius = radius
        self.mat = mat
        self.box = self.bounding_box()
        self.isemissive = isemissive

    def intersect(self, ray, rec):
        o = ray.origin - self.origin
        a = Vector.dot(ray.direction, ray.direction)
        b = 2 * Vector.dot(ray.direction, o)
        c = Vector.dot(o, o) - self.radius * self.radius
        discriminant = b * b - 4 * a * c
        if discriminant >= 0:
            t = (-b - math.sqrt(discriminant)) / (2 * a)
            if rec.min <= t < rec.max:
                rec.normal = Vector.unit_vector(ray.point_at(t) - self.origin)
                rec.front_face = rec.set_face_normal(ray)
                rec.t = t
                rec.p = ray.point_at(t)
                rec.max = t
                rec.hashit = True
                rec.mat = self.mat
                rec.emit = self.emit()
                rec.u, rec.v = self.get_uv(rec.normal)
        return rec

    def emit(self):
        if self.isemissive:
            return self.mat.albedo
        return Color(0, 0, 0)

    def bounding_box(self):
        return AABB(self.origin - Vector(self.radius, self.radius, self.radius),
                    self.origin + Vector(self.radius, self.radius, self.radius))

    def get_uv(self, p):
        theta = math.acos(-p.y)
        phi = math.atan2(-p.z, p.x) + math.pi
        u = phi / (2 * math.pi)
        v = theta / math.pi
        return u, v


class xyRectangle(Geometry):
    def __init__(self, x1, y1, x2, y2, k, mat, isemissive=False):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.k = k
        self.mat = mat
        self.isemissive = isemissive
        self.box = self.bounding_box()
        self.origin = Vector((x1 + x2) / 2, (y1 + y2) / 2, k)

    def intersect(self, ray, rec):
        super().__init__()
        t = (self.k - ray.origin.z) / ray.direction.z
        if t < rec.min or t > rec.max:
            return rec
        x = ray.origin.x + t * ray.direction.x
        y = ray.origin.y + t * ray.direction.y
        if x < self.x1 or x > self.x2 or y < self.y1 or y > self.y2:
            return rec
        rec.normal = Vector(0, 0, 1)
        rec.front_face = rec.set_face_normal(ray)
        rec.t = t
        rec.p = ray.point_at(t)
        rec.max = t
        rec.hashit = True
        rec.mat = self.mat
        rec.emit = self.emit()
        rec.u, rec.v = self.get_uv(rec.p)
        return rec

    def emit(self):
        if self.isemissive:
            return self.mat.albedo
        return Color(0, 0, 0)

    def bounding_box(self):
        return AABB(Vector(self.x1, self.y1, self.k - 0.01), Vector(self.x2, self.y2, self.k + 0.01))

    def get_uv(self, p):
        u = (p.x - self.x1) / (self.x2 - self.x1)
        v = (p.y - self.y1) / (self.y2 - self.y1)
        return u, v


class yzRectangle(Geometry):
    def __init__(self, y1, z1, y2, z2, k, mat, isemissive=False):
        super().__init__()
        self.y1 = y1
        self.z1 = z1
        self.y2 = y2
        self.z2 = z2
        self.k = k
        self.mat = mat
        self.isemissive = isemissive
        self.box = self.bounding_box()
        self.origin = Vector(k, (y1 + y2) / 2, (z1 + z2) / 2)

    def intersect(self, ray, rec):
        super().__init__()
        t = (self.k - ray.origin.x) / ray.direction.x
        if t < rec.min or t > rec.max:
            return rec
        y = ray.origin.y + t * ray.direction.y
        z = ray.origin.z + t * ray.direction.z
        if y < self.y1 or y > self.y2 or z < self.z1 or z > self.z2:
            return rec
        rec.normal = Vector(1, 0, 0)
        rec.front_face = rec.set_face_normal(ray)
        rec.t = t
        rec.p = ray.point_at(t)
        rec.max = t
        rec.hashit = True
        rec.mat = self.mat
        rec.emit = self.emit()
        return rec

    def emit(self):
        if self.isemissive:
            return self.mat.albedo
        return Color(0, 0, 0)

    def bounding_box(self):
        return AABB(Vector(self.k - 0.01, self.y1, self.z1), Vector(self.k + 0.01, self.y2, self.z2))


class zxRectangle(Geometry):
    def __init__(self, x1, z1, x2, z2, k, mat, isemissive=False):
        super().__init__()
        self.x1 = x1
        self.z1 = z1
        self.x2 = x2
        self.z2 = z2
        self.k = k
        self.mat = mat
        self.isemissive = isemissive
        self.box = self.bounding_box()
        self.origin = Vector((x1 + x2) / 2, k, (z1 + z2) / 2)

    def intersect(self, ray, rec):
        t = (self.k - ray.origin.y) / ray.direction.y
        if t < rec.min or t > rec.max:
            return rec
        x = ray.origin.x + t * ray.direction.x
        z = ray.origin.z + t * ray.direction.z
        if x < self.x1 or x > self.x2 or z < self.z1 or z > self.z2:
            return rec
        rec.normal = Vector(0, -1, 0)
        rec.front_face = rec.set_face_normal(ray)
        rec.t = t
        rec.p = ray.point_at(t)
        rec.max = t
        rec.hashit = True
        rec.mat = self.mat
        rec.emit = self.emit()
        return rec

    def emit(self):
        if self.isemissive:
            return self.mat.albedo
        return Color(0, 0, 0)

    def bounding_box(self):
        return AABB(Vector(self.x1, self.k - 0.01, self.z1), Vector(self.x2, self.k + 0.01, self.z1))
