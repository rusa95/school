import tkinter

CANVAS_WIDTH = 395
CANVAS_HEIGHT = 420

window = tkinter.Tk()
window.title('Tic-tac-toe')
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack()

petlistov = [[0 for i in range(5)] for i in range(5)]

kliknutie = 0

win = False

skore = [0, 0]


def grid():
    x = 0
    y = 75
    for i in range(4):
        canvas.create_line(x + 10, y + 10, 385, 10 + y, width=1)
        y += 75
    y = 0
    x = 75
    for z in range(4):
        canvas.create_line(x + 10, y + 10, x + 10, 385, width=1)
        x += 75


def gulicka(pos_x, pos_y):
    canvas.create_oval(pos_x - 25, pos_y - 25, pos_x + 25, pos_y + 25, outline='#89cff0', width=10)


def stvorcek(pos_x, pos_y):
    canvas.create_line(pos_x - 25, pos_y - 25, pos_x + 25, pos_y + 25, fill='#F4C2C2', width=10)
    canvas.create_line(pos_x + 25, pos_y - 25, pos_x - 25, pos_y + 25, fill='#F4C2C2', width=10)


def zaciatocek(coordinates):
    global petlistov, kliknutie
    pos_x = coordinates.x
    pos_y = coordinates.y
    stlpcek = (pos_x - 10) // 75
    riadocek = (pos_y - 10) // 75

    if stlpcek < 0 or riadocek < 0 or riadocek > 4 or stlpcek > 4:
        print('You missed the grid, dummy!')
        return False

    if petlistov[riadocek][stlpcek] != 0:  # ak sa nerovna nule, nemozno vykreslovat
        return False
    else:
        if kliknutie == 0:
            petlistov[riadocek][stlpcek] = 'o'
        else:
            petlistov[riadocek][stlpcek] = 'x'

    if kliknutie == 0:
        gulicka(stlpcek * 75 + 47, riadocek * 75 + 47)
        kliknutie = 1  # zmeni sa kliknutie a zacne vykreslovat stvorcek
        determinacia(riadocek, stlpcek)
    else:
        stvorcek(stlpcek * 75 + 47, riadocek * 75 + 47)
        kliknutie = 0  # zmeni sa kliknutie a zacne vykreslovat gulicku
        determinacia(riadocek, stlpcek)
    for riadok in petlistov:
        print(riadok)
    print(' ')


def restart(retardovatina):  # retardovatina - posle tam co sa presslo, a kde
    global petlistov, kliknutie, skore
    canvas.delete('all')
    if skore[0] >= 3 or skore[1] >= 3:
        canvas.unbind('<Button-1>')
        canvas.create_text(CANVAS_WIDTH // 2, 400, text=f'{skore[0]} : {skore[1]}', fill='#25283D',
                           font=('Tempus Sans ITC', 20))
        canvas.create_text(CANVAS_WIDTH // 2, 150, text='GAME OVER', fill='#25283D',
                           font=('Tempus Sans ITC', 50))
        if skore[0] >= 3:
            canvas.create_text(CANVAS_WIDTH // 2, 200, text=f'PLAYER 1 WINS', fill='#89cff0',
                               font=('Tempus Sans ITC', 25))
            canvas.create_text(CANVAS_WIDTH // 2, 370, text=f'CLICK TO PLAY AGAIN', fill='#25283D',
                               font=('Tempus Sans ITC', 15))
            skore = [0, 0]
            canvas.unbind('<Button-1>')
            canvas.bind('<Button-1>', restart)
        else:
            canvas.create_text(CANVAS_WIDTH // 2, 200, text=f'PLAYER 2 WINS', fill='#F4C2C2',
                               font=('Tempus Sans ITC', 25))
            canvas.create_text(CANVAS_WIDTH // 2, 370, text=f'CLICK TO PLAY AGAIN', fill='#25283D',
                               font=('Tempus Sans ITC', 15))
            skore = [0, 0]
            canvas.unbind('<Button-1>')
            canvas.bind('<Button-1>', restart)
    else:
        grid()
        petlistov = [[0 for i in range(5)] for i in range(5)]
        canvas.create_text(CANVAS_WIDTH // 2, 400, text=f'{skore[0]} : {skore[1]}', fill='#25283D',
                           font=('Tempus Sans ITC', 20))
        kliknutie = 0
        canvas.unbind('<Button-1>')
        canvas.bind('<Button-1>', zaciatocek)


def ciara(x1, y1, x2, y2):
    canvas.create_line(x1, y1, x2, y2, width=4, fill='red')


def determinacia(riadocek, stlpcek):  # funkcia rozhodujuca o tom, ci su v blizkosti pri sebe x alebo o.
    global petlistov, win
    try:  # stlpce
        if petlistov[riadocek][stlpcek] == petlistov[riadocek][stlpcek + 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek][stlpcek - 1]:
            win = True
            ciara(75 * (stlpcek - 1) + 15, 75 * (riadocek + 1) - 25, 75 * (stlpcek + 2) + 5,
                  75 * (riadocek + 1) - 25)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek][stlpcek + 1] and petlistov[riadocek][stlpcek + 1] == \
                petlistov[riadocek][stlpcek + 2]:
            win = True
            ciara(75 * stlpcek + 15, 75 * (riadocek + 1) - 25, 75 * (stlpcek + 3) + 5,
                  75 * (riadocek + 1) - 25)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek][stlpcek - 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek][stlpcek - 2]:
            win = True
            ciara(75 * (stlpcek - 2) + 15, 75 * (riadocek + 1) - 25, 75 * (stlpcek + 1) + 5,
                  75 * (riadocek + 1) - 25)
    except IndexError:
        pass
    try:  # riadky
        if petlistov[riadocek][stlpcek] == petlistov[riadocek + 1][stlpcek] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek - 1][stlpcek]:
            win = True
            ciara(75 * (stlpcek) + 47, 75 * (riadocek - 1) + 15, 75 * (stlpcek) + 47,
                  75 * (riadocek + 2) + 5)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek + 1][stlpcek] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek + 2][stlpcek]:
            win = True
            ciara(75 * (stlpcek) + 47, 75 * (riadocek) + 15, 75 * (stlpcek) + 47,
                  75 * (riadocek + 3) + 5)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek - 1][stlpcek] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek - 2][stlpcek]:
            win = True
            ciara(75 * (stlpcek) + 47, 75 * (riadocek - 2) + 15, 75 * (stlpcek) + 47,
                  75 * (riadocek + 1) + 5)
    except IndexError:
        pass
    try:  # diagonaly
        if petlistov[riadocek][stlpcek] == petlistov[riadocek - 1][stlpcek - 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek - 2][stlpcek - 2]:
            win = True
            ciara(75 * (stlpcek - 2) + 15, 75 * (riadocek - 2) + 15, 75 * (stlpcek + 1),
                  75 * (riadocek + 1) + 5)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek + 1][stlpcek + 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek + 2][stlpcek + 2]:
            win = True
            ciara(75 * (stlpcek) + 15, 75 * (riadocek) + 15, 75 * (stlpcek + 3),
                  75 * (riadocek + 3) - 5)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek - 1][stlpcek + 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek + 1][stlpcek - 1]:
            win = True
            ciara(75 * (stlpcek - 1) + 25, 75 * (riadocek + 2) - 5, 75 * (stlpcek + 2) - 5,
                  75 * (riadocek - 1) + 25)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek - 1][stlpcek - 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek + 1][stlpcek + 1]:
            win = True
            ciara(75 * (stlpcek - 1) + 25, 75 * (riadocek - 1) + 25, 75 * (stlpcek + 2),
                  75 * (riadocek + 2) - 5)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek + 1][stlpcek - 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek + 2][stlpcek - 2]:
            win = True
            ciara(75 * (stlpcek + 1) - 5, 75 * (riadocek) + 25, 75 * (stlpcek - 2) + 20,
                  75 * (riadocek + 3) - 5)
    except IndexError:
        pass
    try:
        if petlistov[riadocek][stlpcek] == petlistov[riadocek - 1][stlpcek + 1] and petlistov[riadocek][stlpcek] == \
                petlistov[riadocek - 2][stlpcek + 2]:
            win = True
            ciara(75 * stlpcek + 25, 75 * (riadocek + 1) - 5, 75 * (stlpcek + 3) - 5,
                  75 * (riadocek - 2) + 25)  # berie to poslednu gulicku nakreslenu

    except IndexError:
        pass
    if win == True:
        if petlistov[riadocek][stlpcek] == 'x':
            print('Pink wins.')
            win = False
            skore[1] += 1
            canvas.unbind('<Button-1>')
            canvas.bind('<Button-1>', restart)
        else:
            print('Blue wins.')
            win = False
            skore[0] += 1
            canvas.unbind('<Button-1>')
            canvas.bind('<Button-1>', restart)


grid()

canvas.create_text(CANVAS_WIDTH // 2, 400, text='TIC-TAC-TOE', fill='#095256', font=('Tempus Sans ITC', 18))

canvas.bind('<Button-1>', zaciatocek)

window.mainloop()
