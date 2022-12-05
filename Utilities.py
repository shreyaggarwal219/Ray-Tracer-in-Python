import math
import random
from vector import *
import imageio


def randf(minimum, maximum):
    return (random.random()) * (maximum - minimum) + minimum


def clampf(num, minimum, maximum):
    return max(min(maximum, num), minimum)


def RandomInSphere():
    while True:
        vec = Vector(randf(-1, 1), randf(-1, 1), randf(-1, 1))
        if vec.mag() * vec.mag() >= 1:
            continue
        return Vector.unit_vector(vec)


def RandomInHemisphere(normal):
    in_unit_sphere = RandomInSphere()
    if Vector.dot(normal, in_unit_sphere) > 0:
        return in_unit_sphere
    return -in_unit_sphere


def GammaCorrect(color):
    return Color(math.sqrt(color.x), math.sqrt(color.y), math.sqrt(color.z))


def to_byte(color):
    return round(max(min(color * 255, 255), 0))


def to_Radian(degree):
    return (math.pi / 180) * degree


def to_Degree(radians):
    return 180 / math.pi * radians


def read_Image(image):
    img = imageio.imread(image)
    return img
