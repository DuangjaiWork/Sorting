from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import random

class Renderer(Window):
    def __init__(self):
        super().__init__(940, 650, "Merge Sort")
        self.set_location(100, 100)
        self.batch = Batch()
        self.num_bars = 100
        self.x = random.sample(range(1, self.num_bars + 1), self.num_bars)
        self.bars = [Rectangle(20 + e * 9, 60, 8, i*5, batch=self.batch) for e, i in enumerate(self.x)]
        self.animation_generator = self.merge_sort_animation(0, len(self.x) - 1)

    def merge_sort_animation(self, l, r):
        if l < r:
            mid = (l + r) // 2
            yield from self.merge_sort_animation(l, mid)
            yield from self.merge_sort_animation(mid + 1, r)
            yield from self.merge(l, mid, r)

    def merge(self, l, mid, r):
        left, right = self.x[l:mid + 1], self.x[mid + 1:r + 1]
        i, j, k = 0, 0, l
        while i < len(left) and j < len(right):
            self.bars[l + i].color = (255, 0, 0, 255)
            self.bars[mid + 1 + j].color = (255, 0, 0, 255)
            yield

            if left[i] <= right[j]:
                self.x[k] = left[i]
                i += 1
            else:
                self.x[k] = right[j]
                j += 1

            k += 1
            self.update_bars()

        while i < len(left):
            self.x[k] = left[i]
            i += 1
            k += 1
            self.update_bars()

        while j < len(right):
            self.x[k] = right[j]
            j += 1
            k += 1
            self.update_bars()

    def update_bars(self):
        self.bars = [Rectangle(20 + e * 9, 60, 8, i*5, batch=self.batch, color=(255, 255, 255, 255)) for e, i in enumerate(self.x)]

    def on_update(self, dt):
        try:
            next(self.animation_generator)
        except StopIteration:
            pass

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 0.01)
run()
