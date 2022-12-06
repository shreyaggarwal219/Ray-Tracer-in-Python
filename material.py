from vector import *
from Utilities import *
from ray import Ray


class Material:
    def __init__(self, texture, normal_map=None):
        self.texture = texture
        self.normal_map = normal_map
        pass

    def reflect(self, ray_in, rec):
        pass


class Lambert(Material):
    def __init__(self, texture, normal_map=None):
        super().__init__(texture, normal_map)
        #self.albedo = texture.color

    def reflect(self, ray_in, rec):
        reflected = rec.p + RandomInHemisphere(rec.normal)
        return Ray(rec.p, reflected)


class Metal(Material):
    def __init__(self, texture, glossy=0):
        super().__init__(texture)
        self.glossy = glossy

    def reflect(self, ray_in, rec):
        reflected = Vector.reflect(ray_in.direction, rec.normal) + RandomInHemisphere(
            rec.normal) * self.glossy
        return Ray(rec.p, reflected)


class Dielectric(Material):
    def __init__(self, eta):
        Material.__init__(self, SolidTexture(Color(1, 1, 1)))
        self.eta = eta

    def reflect(self, ray_in, rec):
        eta = 1 / self.eta
        if not rec.front_face:
            eta = self.eta
        cos_theta = Vector.dot(-ray_in.direction, rec.normal) / (ray_in.direction.mag() * rec.normal.mag())
        sin_theta = math.sqrt(1 - cos_theta ** 2)
        direction = Vector(0, 0, 0)
        if eta * sin_theta > 1:
            direction = Vector.reflect(ray_in.direction, rec.normal)
        else:
            direction = Vector.refract(ray_in.direction, rec.normal, eta)
        return Ray(rec.p, direction)


class Texture():
    def __init__(self):
        pass

    def value(self, p, u, v):
        pass


class SolidTexture(Texture):
    def __init__(self, color):
        super().__init__()
        self.color = color

    def value(self, p, u, v):
        return self.color


class CheckerTexture(Texture):
    def __init__(self, color1, color2):
        super().__init__()
        self.color1 = color1
        self.color2 = color2

    def value(self, p, u, v):
        sine = math.sin(p.x * 100) * math.sin(p.y * 100) * math.sin(p.z * 100)
        if sine < 0:
            return self.color1
        else:
            return self.color2


class ImageTexture(Texture):
    def __init__(self, image: str):
        super().__init__()
        self.image = read_Image(image)
        self.width = self.image.shape[1]
        self.height = self.image.shape[0]
        self.color_channels = self.image.shape[2]

    def value(self, p, u, v):
        u = clampf(u, 0, 1)
        v = 1 - clampf(v, 0, 1)
        color_scale = 1 / 255
        i = int(u * self.width)
        j = int(v * self.height)
        if i >= self.width:
            i = self.width - 1
        if j >= self.height:
            j = self.height - 1
        return Color(self.image[j][i][0] * color_scale,
                     self.image[j][i][1] * color_scale,
                     self.image[j][i][2] * color_scale)

class Normal_Map():
    def __init__(self, normal_map: str):
        super().__init__()
        self.normal_map = read_Image(normal_map)
        self.width = self.normal_map.shape[1]
        self.height = self.normal_map.shape[0]

    def get_normal(self, normal, tangent, p, u, v):
        bitangent = Vector.cross(normal, tangent)
        v = 1-v
        i = int(u * self.width)
        j = int(v * self.height)
        if i >= self.width:
            i = self.width - 1
        if j >= self.height:
            j = self.height - 1

        color_scale = 1 / 255
        normal_map_pixel = Vector(self.normal_map[j][i][0], self.normal_map[j][i][1], self.normal_map[j][i][2]) * color_scale
        normal_map_pixel = 2 * normal_map_pixel - Vector(1,1,1)
        new_normal = Vector(0,0,0)
        '''
        new_normal.x = Vector.dot(tangent, normal_map_pixel)
        new_normal.y = Vector.dot(bitangent, normal_map_pixel)
        new_normal.z = Vector.dot(normal, normal_map_pixel)
        '''
        new_normal.x = tangent.x * normal_map_pixel.x + bitangent.x * normal_map_pixel.y + normal.x * normal_map_pixel.z
        new_normal.y = tangent.y * normal_map_pixel.x + bitangent.y * normal_map_pixel.y + normal.y * normal_map_pixel.z
        new_normal.z = tangent.z * normal_map_pixel.x + bitangent.z * normal_map_pixel.y + normal.z * normal_map_pixel.z
        return Vector.unit_vector(new_normal)

def Phong(light, rec, cam, incoming_dir):
    incoming_dir = Vector.unit_vector(incoming_dir)
    reflect_dir = Vector.unit_vector(Vector.reflect(incoming_dir, rec.normal))
    eye_direction = Vector.unit_vector(cam.origin - rec.p)
    cos_alpha = Vector.dot(reflect_dir, eye_direction) / (reflect_dir.mag() * eye_direction.mag())
    cos_theta = Vector.dot(rec.normal, -incoming_dir) / (rec.normal.mag() * incoming_dir.mag())
    return (light.color * max(cos_theta, 0) + light.color * (max(cos_alpha, 0) ** 10)) * light.intensity


def Blinn(light, rec, cam, incoming_dir):
    incoming_dir = Vector.unit_vector(incoming_dir)
    eye_direction = Vector.unit_vector(cam.origin - rec.p)
    halfway_vector = Vector.unit_vector(eye_direction - incoming_dir)
    cos_beta = Vector.dot(halfway_vector, rec.normal) / (halfway_vector.mag() * rec.normal.mag())
    cos_theta = Vector.dot(rec.normal, -incoming_dir) / (rec.normal.mag() * incoming_dir.mag())
    return (light.color * max(cos_theta, 0) + light.color * (
            max(cos_beta, 0) ** 10)) * light.intensity  # diffuse Shading + specular Shading
