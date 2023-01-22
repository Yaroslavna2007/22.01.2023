from tkinter import *
import time

root = Tk()
root.title("Balls")

canvas = Canvas(root, width = 500, height = 500)
canvas.pack()

ball1 = canvas.create_oval(250, 10, 260, 20)
ball2 = canvas.create_oval(250, 10, 260, 20)
ball3 = canvas.create_oval(250, 10, 260, 20)

xDir1 = -1
yDir1 = 1
xDir2 = -1
yDir2 = 1
xDir3 = -1
yDir3 = 1
while True:
    canvas.move(ball1, 5 * xDir1, 2 * yDir1)
    canvas.move(ball2, 3 * xDir2, 4 * yDir2)
    canvas.move(ball3, 6 * xDir3, 7 * yDir3)
    time.sleep(0.02)
    c = canvas.coords(ball1)
    d = canvas.coords(ball2)
    q = canvas.coords(ball3)
    if c[0] <= 0:
        xDir1 = 1
    if d[0] <= 0:
        xDir2 = 1
    if q[0] <= 0:
        xDir3 = 1
    elif c[2] >= 500:
        xDir1 = -1
    elif d[2] >= 500:
        xDir2 = -1
    elif q[2] >= 500:
        xDir3 = -1
    if c[3] >= 500:
        yDir1 = -1
    if d[3] >= 500:
        yDir2 = -1
    if q[3] >= 500:
        yDir3 = -1
    elif c[1] <= 0:
        yDir1 = 1
    elif d[1] <= 0:
        yDir2 = 1
    elif q[1] <= 0:
        yDir3 = 1
    root.update()
#объединить условия не получилось:(