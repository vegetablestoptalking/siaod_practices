import math
from random import randint, random, seed, shuffle
from tkinter import Tk, Canvas, Button


CANVAS_W, CANVAS_H = 800, 800
NODE_R = CANVAS_H * 0.005


class GUI:
    def __init__(self, root):
        self.canvas = Canvas(root, width=CANVAS_W, height=CANVAS_H, bg="white")
        self.canvas.pack()

    def draw(self, points):
        self.canvas.delete("all")
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            self.canvas.create_line(x1, y1, x2, y2)
            r = NODE_R
            self.canvas.create_oval(x1 - r, y1 - r, x1 + r, y1 + r, fill="red")


def make_random_graph(size):
    points = []
    for i in range(size):
        points.append((
            randint(NODE_R, CANVAS_W - NODE_R),
            randint(NODE_R, CANVAS_H - NODE_R)
        ))
    return points


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def cost(s):
    tour = distance(s[-1], s[0])
    for i in range(len(s) - 1):
        tour += distance(s[i], s[i + 1])
    return tour


def random_transform(x):
    x = x.copy()
    shuffle(x)
    return x


def swap_transform(x):
    x = x.copy()
    i = randint(0, len(x) - 1)
    j = randint(0, len(x) - 1)
    x[i],x[j] = x[j], x[i]
    return x


def rot_transform(x):
    # TODO
    return x.copy()


def random_search(x, steps):
    result = x
    for i in range(steps):
        x = random_transform(x)
        if cost(x) < cost(result):
            result = x
    return result


def local_search(x, steps):
    for i in range(steps):
        y = swap_transform(x)
        if cost(x) > cost(y):
            x = y
    return x


def sa_search(x, steps):
    # TODO
    return x


seed(42)
g = make_random_graph(19)

g = local_search(g, 1000)
print(cost(g))

root = Tk()
w = GUI(root)
w.draw(g)
root.mainloop()
