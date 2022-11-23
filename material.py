from vector import *
from Utilities import *
from ray import Ray


class Material:
    def __init__(self, color):
        self.albedo = color
        pass

    def reflect(self, ray_in, rec):
        pass


class Lambert(Material):
    def __init__(self, color):
        super().__init__(color)

    def reflect(self, ray_in, rec):
        reflected = rec.p + RandomInHemisphere(rec.normal)
        return Ray(rec.p, reflected)


class Metal(Material):
    def __init__(self, color, glossy=0):
        super().__init__(color)
        self.glossy = glossy

    def reflect(self, ray_in, rec):
        reflected = Vector.reflect(ray_in.direction, rec.normal) + RandomInHemisphere(
            rec.normal) * self.glossy
        return Ray(rec.p, reflected)


class Dielectric(Material):
    def __init__(self, eta):
        Material.__init__(self, Color(1, 1, 1))
        self.eta = eta

    def reflect(self, ray_in, rec):
        eta = 1 / self.eta
        if not rec.front_face:
            eta = self.eta
        cos_theta = Vector.dot(-ray_in.direction, rec.normal)/(ray_in.direction.mag() * rec.normal.mag())
        sin_theta = math.sqrt(1 - cos_theta**2)
        direction = Vector(0, 0, 0)
        if eta * sin_theta > 1:
            direction = Vector.reflect(ray_in.direction, rec.normal)
        else:
            direction = Vector.refract(ray_in.direction, rec.normal, eta)
        return Ray(rec.p, direction)


def Phong(light, rec, cam, incoming_dir):
    incoming_dir = Vector.unit_vector(incoming_dir)
    reflect_dir = Vector.unit_vector(Vector.reflect(incoming_dir, rec.normal))
    eye_direction = Vector.unit_vector(cam.origin - rec.p)
    cos_alpha = Vector.dot(reflect_dir, eye_direction) / (reflect_dir.mag() * eye_direction.mag())
    cos_theta = Vector.dot(rec.normal, -incoming_dir) / (rec.normal.mag() * incoming_dir.mag())
    return (light.color * max(cos_theta, 0) + light.color * (max(cos_alpha, 0) ** 5)) * light.intensity


def Blinn(light, rec, cam, incoming_dir):
    incoming_dir = Vector.unit_vector(incoming_dir)
    eye_direction = Vector.unit_vector(cam.origin - rec.p)
    halfway_vector = Vector.unit_vector(eye_direction - incoming_dir)
    cos_beta = Vector.dot(halfway_vector, rec.normal) / (halfway_vector.mag() * rec.normal.mag())
    cos_theta = Vector.dot(rec.normal, -incoming_dir) / (rec.normal.mag() * incoming_dir.mag())
    return (light.color * max(cos_theta, 0) + light.color * (max(cos_beta, 0) ** 5)) * light.intensity         #diffuse Shading + specular Shading
