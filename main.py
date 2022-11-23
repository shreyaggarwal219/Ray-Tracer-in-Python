from vector import Vector
from image import Image
from camera import Camera
from geometry import *
from light import *
from material import *
from bvh import *
from light import *
from Utilities import *
from os import environ
import time

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


def create_window(width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RayTracing")
    return screen


def renderImage(width, height, pixels):
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RayTracing")
    running = True
    done = False
    while running:
        if not done:
            for j in range(height):
                for i in range(width):
                    surface.set_at((i, j), (to_byte(pixels[j][i].x),
                                            to_byte(pixels[j][i].y),
                                            to_byte(pixels[j][i].z)))
            pygame.display.flip()
            done = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    exit()


def main():
    WIDTH = 600
    aspect_ratio = 1
    HEIGHT = round(WIDTH / aspect_ratio)
    samples_per_pixel = 10
    maxDepth = 5

    background_color = Color(0, 0, 0)
    im = Image(WIDTH, HEIGHT, background_color)
    origin = Vector(0, 0, 1)
    lookat = Vector(0,0,-1)
    vfov = 90
    cam = Camera(origin, lookat, vfov, aspect_ratio)
    obj = Geometry()
    '''
    obj.add(xyRectangle(-1, -1, 1, 1, -2, Lambert(Color(0.73, 0.73, 0.73)), True))
    obj.add(yzRectangle(-1, -1, 1, 1, -0.5, Lambert(Color(0.65, 0.05, 0.05))))
    obj.add(yzRectangle(-1, -1, 1, 1, 0.5, Lambert(Color(0.05, 0.65, 0.05))))
    obj.add(zxRectangle(-1, -1, 1, 1, -0.5, Lambert(Color(0.73, 0.73, 0.73)), True))
    obj.add(zxRectangle(-1, -1, 1, 1, 0.5, Lambert(Color(0.73, 0.73, 0.73)), True))
    obj.add(zxRectangle(-0.5, -0.5, 0.5, 0.5, 0.45, Lambert(Color(10, 10, 10)), True))
  '''
    for i in range(20):
        obj.add(Sphere(Vector(randf(-1,1), randf(-1,1), randf(-1,1)), randf(0,0.2), Lambert(Color(randf(0,1), randf(0,1), randf(0,1)))))
    #obj.add(Sphere(Vector(-0.5, 0, -1), 0.25, Dielectric(1.5)))
    '''
    obj.add(Sphere(Vector(0.5, 0, -1), 0.25, Metal(Color(0.8, 0.6, 0.2), 0)))
    obj.add(Sphere(Vector(0, -100.5, -1), 100, Lambert(Color(0.8, 0.8, 0))))
    obj.add(Sphere(Vector(0,0,-1),0.25, Lambert(Color(1,0,0))))
    '''
    bvh = BVH(0, len(obj.objects), obj.objects)
    soft_shadows = 0
    ambient = Color(0.1, 0.1, 0.1)
    lo = LightObjects(ambient, soft_shadows)
    lo.add(PointLight(Vector(0, 0.4, 0), Color(0, 0, 1), 1))
    lo.add(DirectionLight(Vector(10, 10, 10), Vector(-1, -1, -1), Color(0.1, 0.1, 0.1), 1))
    #lo.add(SpotLight(Vector(0, 2, 0), Vector(0, -1, 0), to_Radian(50),to_Radian(40), Color(1, 1, 1), 10))

    start_time = time.time()
    im.render_from_multiprocess(cam, bvh, lo, samples_per_pixel, maxDepth)
    print(f"Total Time Taken: {time.time() - start_time}")

    renderImage(WIDTH, HEIGHT, im.pixels)


if __name__ == "__main__":
    main()
