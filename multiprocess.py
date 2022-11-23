import multiprocessing as mp
from vector import *


class Multiprocessing:
    def __init__(self):
        self.cpuCount = mp.cpu_count()
        self.processes = []
        self.ranges = []
        self.lock = mp.Lock()
        self.q = mp.Queue(maxsize=10000)
        self.val = mp.Value('i', 0)

    def split_range(self, count):
        parts = self.cpuCount
        d, r = divmod(count, parts)
        for i in range(parts):
            self.ranges.append((i * d + min(i, r), (i + 1) * d + min(i + 1, r)))

    def start_process(self):
        for process in self.processes:
            process.start()

    def join_process(self):
        for process in self.processes:
            process.join()

    def read(self, image):
        if mp.current_process().name == 'MainProcess':
            num = image.width * image.height
            while num > 0:
                msg = self.q.get()
                if msg == "DONE":
                    break
                pix = msg.split()
                row = int(pix[0])
                col = int(pix[1])
                x = float(pix[2])
                y = float(pix[3])
                z = float(pix[4])
                image.pixels[row][col] = Color(x, y, z)
                num = num - 1
