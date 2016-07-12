import tkinter

def click_ball(event):
    """ Обработчик событий мышки для игрового холста canvas
    :param event: событие с координатами клика
    :return: ничего
    """

    # event.x, event.y)


def create_random_ball():
    canvas.create_oval(x, y, x+2*R, y+2*R, width=1, fill=random_color())


root = tkinter.Tk()

canvas = tkinter.Canvas(root, background='white', width=400, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

for i in range(10):

root.mainloop()
print("Эта строка будет достигнута только при выходе из приложения.")