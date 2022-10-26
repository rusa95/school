import tkinter
import time

CANVAS_WIDTH = 900
CANVAS_HEIGHT = 900
number_of_trains = 5

window = tkinter.Tk()
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

wagon_col = 'orange'
wag_win_col = 'red'
wheel_col = 'black'
loc_col = 'orange'
cab_color = 'red'
chimney_color = 'red'

def wagon(x, y):
    canvas.create_rectangle(x, y, x + 100, y + 50, fill=wagon_col)
    canvas.create_rectangle(x + 5, y + 10, x + 45, y + 35, fill=wag_win_col)
    canvas.create_rectangle(x + 55, y + 10, x + 95, y + 35, fill=wag_win_col)
    canvas.create_line(x - 10, y + 25, x, y + 25)
    canvas.create_line(x - 10, y + 30, x, y + 30)
    canvas.create_oval(x + 5, y + 40, x + 35, y + 70, fill=wheel_col)
    canvas.create_oval(x + 65, y + 40, x + 95, y + 70, fill=wheel_col)


def locomotive(x, y):
    c = x
    canvas.create_rectangle(x - 10, y - 10, x + 89, y + 50, fill= loc_col)
    canvas.create_oval(x + 65, y + 45, x + 90, y + 70, fill=wheel_col)
    canvas.create_oval(x + 40, y + 45, x + 65, y + 70, fill=wheel_col)
    canvas.create_oval(x + 15, y + 45, x + 40, y + 70, fill=wheel_col)
    canvas.create_oval(x - 10, y + 45, x + 15, y + 70, fill=wheel_col)
    canvas.create_rectangle(x + 40, y - 10, x + 89, y - 40, fill=cab_color)
    canvas.create_rectangle(x + 5, y - 10, x + 25, y - 30, fill=chimney_color)
    for t in range(5):
        canvas.create_line(c + 5, y - 35, c + 10, y - 50,)
        c += 5



x = 100
c, y = x, x
while True:
    canvas.delete('all')
    time.sleep(0.0003)
    locomotive(x, 100)
    for i in range(number_of_trains):
        wagon(x + 100 + i * 111, 100)
    x -= 5
    c -= 5
    if x < -900:
        break
    canvas.update()

window.mainloop()


