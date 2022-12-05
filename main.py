from vector import Vector
from image import Image
from camera import Camera
from geometry import *
from light import *
from material import *
from scene import *
from bvh import *
from light import *
from Utilities import *
from os import environ

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

    # Image
    HEIGHT = 600
    aspect_ratio = 1
    WIDTH = (int)(HEIGHT * aspect_ratio)
    samples_per_pixel = 50
    maxDepth = 10

    ambient = Color(0, 0, 0)

    im = Image(WIDTH, HEIGHT, ambient)

    # Camera
    origin = Vector(0, 0, 10)
    lookat = Vector(0, 0, -1)
    vfov = 20
    cam = Camera(origin, lookat, vfov, aspect_ratio)

    # Scene
    obj = Geometry()
    #obj = Cornell_Box(obj)
    obj = Earth_Scene(obj)
    lo = Lighting()
    im = render_Scene(im, obj, lo, cam, samples_per_pixel, maxDepth)
    renderImage(WIDTH, HEIGHT, im.pixels)


if __name__ == "__main__":
    main()
