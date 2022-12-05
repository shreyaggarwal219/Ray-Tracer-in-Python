from bvh import *
from light import *
from Utilities import *
from geometry import *
import time


def Cornell_Box(obj):
    obj.add(xyRectangle(-1, -1, 1, 1, -2, Lambert(SolidTexture(Color(0.73, 0.73, 0.73)))))  # Front Plane
    obj.add(xyRectangle(-1, -1, 1, 1, 1, Lambert(SolidTexture(Color(0.73, 0.73, 0.73)))))  # Back Plane
    obj.add(yzRectangle(-1, -1, 1, 1, -0.5, Lambert(SolidTexture(Color(0.65, 0.05, 0.05)))))  # Left Plane
    obj.add(yzRectangle(-1, -1, 1, 1, 0.5, Lambert(SolidTexture(Color(0.05, 0.65, 0.05)))))  # Right Plane
    obj.add(zxRectangle(-1, -1, 1, 1, -0.5, Lambert(SolidTexture(Color(0.73, 0.73, 0.73)))))  # Bottom Plane
    obj.add(zxRectangle(-1, -1, 1, 1, 0.5, Lambert(SolidTexture(Color(0.73, 0.73, 0.73)))))  # Top Plane
    return obj


def Lighting():
    soft_shadows = 1
    lo = LightObjects(soft_shadows)
    # lo.add(PointLight(Vector(0, 0.4, 0), Color(0, 0, 1), 1))
    # lo.add(DirectionLight(Vector(10, 10, 10), Vector(-1, -1, -1), Color(0.1, 0.1, 0.1), 1))
    # lo.add(SpotLight(Vector(0, 2, 0), Vector(0, -1, 0), to_Radian(50),to_Radian(40), Color(1, 1, 1), 10))
    return lo


def render_Scene(im, obj, lo, cam, spp, depth):
    bvh = BVH(0, len(obj.objects), obj.objects)
    start_time = time.time()
    im.render_from_multiprocess(cam, bvh, lo, spp, depth)
    print("Total Time Taken: {:3.2f}".format(time.time() - start_time))
    return im


def Reflection_Scene(obj):
    obj.add(Sphere(Vector(-0.27, 0.25, -1), 0.2, Metal(SolidTexture(Color(0.8, 0.6, 0.2)), 0)))
    obj.add(Sphere(Vector(0.27, 0.25, -1), 0.2, Metal(SolidTexture(Color(0.12, 0.32, 0.72)), 0)))
    obj.add(Sphere(Vector(0, -0.25, -1), 0.2, Metal(SolidTexture(Color(0.9, 0.4, 0.89)), 0)))
    return obj


def Diffuse_Scene(obj):
    obj.add(Sphere(Vector(0, 0, -1), 0.3, Lambert(SolidTexture(Color(0.8, 0.6, 0.2)))))
    # obj.add(Sphere(Vector(0.27, 0.25, -1), 0.2, Lambert(SolidTexture(Color(0.12, 0.32, 0.72)), 0)))
    return obj


def Glossy_Scene(obj):
    obj.add(Sphere(Vector(-0.27, 0.25, -1), 0.2, Metal(SolidTexture(Color(0.8, 0.6, 0.2)), 0.5)))
    obj.add(Sphere(Vector(0.27, 0.25, -1), 0.2, Metal(SolidTexture(Color(0.12, 0.32, 0.72)), 0.5)))
    obj.add(Sphere(Vector(0, -0.25, -1), 0.2, Metal(SolidTexture(Color(0.9, 0.4, 0.89)), 0.5)))
    return obj


def Refraction_Scene(obj):
    obj.add(Sphere(Vector(0, -100, -1), 100, Lambert(SolidTexture(Color(0.8, 0.8, 0.2)))))
    obj.add(Sphere(Vector(0, 0.5, -1), 0.5, Dielectric(2)))
    return obj


def Random_Spheres():
    obj = Geometry()
    for i in range(20):
        obj.add(Sphere(Vector(randf(-2, 2), randf(-2, 2), -1), randf(0, 0.4),
                       Lambert(Color(randf(0, 1), randf(0, 1), randf(0, 1)))))
    for i in range(20):
        obj.add(Sphere(Vector(randf(-2, 2), randf(-2, 2), -1), randf(0, 0.4),
                       Metal(Color(randf(0, 1), randf(0, 1), randf(0, 1)))))
