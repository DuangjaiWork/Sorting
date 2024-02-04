from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Rectangle
from pyglet.graphics import Batch
from pyglet import clock

class Renderer(Window):
    def __init__(self):
        super().__init__(790, 820, "Bubble sort")
        self.batch = Batch()
        self.x = [3, 4, 2, 1, 6, 5]
        self.bars = [Rectangle(100 + e * 100, 100, 80, i * 100, batch=self.batch) for e, i in enumerate(self.x)]
        self.steps = self.bubble_sort()

    def bubble_sort(self):
        n = len(self.x)
        steps = []
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.x[j] > self.x[j + 1]:
                    self.x[j], self.x[j + 1] = self.x[j + 1], self.x[j]
                    steps.append(list(self.x))
        return steps

    def on_update(self, deltatime):
        if self.steps:
            current_step = self.steps.pop(0)
            for i, bar in enumerate(self.bars):
                bar.height = current_step[i] * 100

    def on_draw(self):
        self.clear()
        for i, bar in enumerate(self.bars):
            bar.color = (255, 0, 0, 255) if self.x[i] != i + 1 else (255, 255, 255, 255)
            bar.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 1)
run()