import Utilities
from Utilities import *
from ray import TempRec
from multiprocess import Multiprocessing as mp
import multiprocessing
from vector import *

class Image:

    def __init__(self, width, height, bg):
        self.width = width
        self.height = height
        self.pixels = [[Vector(0, 0, 0) for _ in range(width)] for _ in range(height)]
        self.bg = bg
        self.black = Color(0, 0, 0)
        self.white = Color(1, 1, 1)


    def pathTrace(self, ray, objects, obj, lights, maxDepth, cam):
        if maxDepth <= 0:
            return Color(0, 0, 0)

        rec = TempRec()
        rec = objects.intersect(ray, rec)

        if rec.hashit and rec.mat is not None:
            lightColor = lights.lightColor(rec, obj, cam)
            return Vector.mulVec(rec.emit + lightColor + self.pathTrace(rec.mat.reflect(ray, rec), objects, obj, lights,
                                                                        maxDepth - 1, cam),
                                 rec.mat.texture.value(rec.p, rec.u, rec.v))
        '''
        unit_direction = Vector.unit_vector(ray.direction)
        t = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - t) * Color(1.0, 1.0, 1.0) + t * Color(0.5, 0.7, 1.0)
        '''
        return Color(0.25, 0.25, 0.25)

    def render_from_multiprocess(self, cam, objects, obj, lights, samples_per_pixel, maxDepth):
        m = mp()
        m.split_range(self.height)

        rows_done = m.val

        for hmin, hmax in m.ranges:
            m.processes.append(
                multiprocessing.Process(target=self.render,
                                        args=(
                                            cam, objects, obj, lights, samples_per_pixel, maxDepth, hmin, hmax,
                                            rows_done,
                                            m.lock, m.q)))

        m.start_process()
        m.read(self)
        m.join_process()

    def render(self, cam, objects, obj, lights, samples_per_pixel, maxDepth, hmin, hmax, rows_done, lock, q):
        for rows in range(hmin, hmax):
            for col in range(self.width):
                color = Color(0, 0, 0)
                for s in range(samples_per_pixel):
                    u = (col + randf(-0.5, 0.5)) / (self.width - 1)
                    v = (rows + randf(-0.5, 0.5)) / (self.height - 1)
                    ray = cam.get_ray(u, v)
                    color += self.renderPixel(ray, objects, obj, lights, maxDepth, cam)
                scale = 1 / samples_per_pixel
                color = Utilities.GammaCorrect(color * scale)
                self.pixels[rows][col] = color
        self.write(hmin, hmax, rows_done, lock, q)

    def renderPixel(self, ray, objects, obj, lights, maxDepth, cam) -> 'Color':
        pixel_color = self.pathTrace(ray, objects, obj, lights, maxDepth, cam)
        return pixel_color

    def write(self, hmin, hmax, rows_done, lock, q):
        lock.acquire()
        for row in range(hmin, hmax):
            print("Rendering... {:3.2f}%".format(rows_done.value / (self.height - 1) * 100), end="\r")
            for col in range(self.width):
                pix = f"{row} {col} {self.pixels[row][col].x} {self.pixels[row][col].y} {self.pixels[row][col].z}"
                q.put(pix)
            rows_done.value += 1
        lock.release()
