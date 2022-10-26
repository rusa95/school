import tkinter
import random

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

window = tkinter.Tk()
window.title('boats')
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

lodicky = []


def race(coordinates):
    global lodicky
    jozef = True
    while jozef:
        canvas.update()
        canvas.after(100)
        for lodicka in lodicky:
            lodicka.x += random.randint(5, 20)
            if (lodicka.x + 22) >= (CANVAS_WIDTH - 50):
                print(f'Vyhrala lodicka {lodicka.nazov}')
                jozef = False
        canvas.delete('all')
        line()
        for lodicka in lodicky:
            lodicka.draw()


def line():
    canvas.create_line(CANVAS_WIDTH - 50, 0, CANVAS_WIDTH - 50, CANVAS_HEIGHT, width=5, fill='red')


class boat:
    def __init__(self, x, y, nazov):
        self.x = x
        self.y = y
        self.nazov = nazov
        self.plachta = random.randint(-3, 3)
        canvas.create_line(x, y, x, y - 25, x + 10 + self.plachta, y - 10, x, y - 5)
        canvas.create_polygon(x - 20, y, x + 20, y, x + 10, y + 8, x - 10, y + 8)

    def draw(self):
        x = self.x
        y = self.y
        plachta = self.plachta
        canvas.create_line(x, y, x, y - 25, x + 10 + plachta, y - 10, x, y - 5)
        canvas.create_polygon(x - 20, y, x + 20, y, x + 10, y + 8, x - 10, y + 8)


for i in range(15):
    lodicky.append(boat(30, 60 + i * 50, f'lodicka{i + 1}'))

line()

canvas.bind('<Button-1>', race)
window.mainloop()
