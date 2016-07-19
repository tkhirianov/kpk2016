import tkinter
from random import choice, randint
from math import cos, sin, pi
import time
import signal

ball_initial_number = 10
ball_minimal_radius = 10
ball_maximal_radius = 40

#ball_available_colors = '0123456789ABCDEF'#['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
#balls_coord = []#список координат шариков
#balls_num = []#список номеров шариков

ball_available_colors = ['green', 'blue', 'red', 'lightgray', '#FF00FF', '#FFFF00']
ball_bonus_for_color = [       2,      2,     3,           1,         1,         1]
balls = list()
step_fly = 1.5
bonus = 0

def accumulation_of_bonus(color):
    """
    За подбитые шарики основного цвета дается 2 балл,
    за шарики дополнительных цветов - 1 балл
    :param color:
    :return:
    """
    bonus = ball_bonus_for_color[ball_available_colors.index(color)]
    label_bonus["text"] =  str(int(label_bonus["text"]) + bonus)


def click_ball(event):
    """
    Обработчик событий от мышки для игрового холста
    :param event:мышка указывет
     По клику мышкой нужно удалять тот объект, на который
     А также засчитывать его очки
    :return:
    """
    obj = canvas.find_closest(event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(obj)
    R = (x2 - x1) / 2
    xc = x1 + R
    yc = y1 + R
    i = 0
    while (i < len(balls)) and (obj[0] != balls[i][1]):
        i += 1
    if i < len(balls) and (xc - event.x)**2 + (yc - event.y) ** 2 <= R**2:
        accumulation_of_bonus(canvas.itemcget( obj[0], "fill"))
        canvas.delete(balls[i][1])
        balls[:i+1] = balls[:i]
        create_random_ball()

def move_all_balls():
    """
    передвигат все шарики на чуть-чуть
    :return:
    """
    for obj in canvas.find_all():
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        canvas.move(obj, dx, dy)

def create_random_ball():
    """
    создает шарик в случайном месте игрового холста
    шарик не выходит за границу игрового поля
    :return:
    """
    global balls
    R = randint(ball_minimal_radius, ball_maximal_radius)
    x = randint(0+R, int(canvas['width'])-1-R)
    y = randint(0+R, int(canvas['width'])-1-R)
    angle = randint(0,359)
    id_oval = canvas.create_oval(x-R,y-R,x+R, y+R, width=1, fill=random_color())
    balls.append([angle, id_oval])


def random_color():
    """
    случайный цвет из некоторого набора цветов
    :return:
    """
    return choice(ball_available_colors)

def init_ball_catch_game():
    """
     Создает необхоимое для игры количство шариков,по которым нужно будет кликать

     """
    for i in range(ball_initial_number):
        create_random_ball()


def init_main_window():
    """
    Инициализация главного окна
        :return:
    """
    global root, frame_bonus,frame_canvas, label_bonus, canvas
    root  = tkinter.Tk()
    frame_bonus = tkinter.Frame(root)
    label_caption = tkinter.Label(frame_bonus, text="  Накопленные очки  ", width=20, font="Calibri 14")
    label_bonus = tkinter.Label(frame_bonus, text="0", font="Calibri 14")
    label_caption.grid(row=0, column=0)
    label_bonus.grid(row=0, column=1)
    frame_bonus.pack()

    frame_canvas = tkinter.Frame(root)
    frame_canvas.pack()

    canvas = tkinter.Canvas(frame_canvas, background='white', width=400, height=400)
    canvas.bind('<Button>', click_ball)
    canvas.pack()

def gradus_to_radians(angle_in_gradus):
    return angle_in_gradus * pi / 180

def move_balls():
    for i in range(len(balls)):
        x1, y1, x2, y2 = canvas.coords(balls[i][1])
        if y1 <= 0:
            balls[i][0] = 360 - balls[i][0]
        elif y2 >= 400:
            balls[i][0] = 360 - balls[i][0]
        elif x1 <= 0:
            balls[i][0] = 180 - balls[i][0]
        elif x2 >= 400:
            balls[i][0] = 180 - balls[i][0]
        dx = step_fly * cos(gradus_to_radians(balls[i][0]))
        dy = step_fly * sin(gradus_to_radians(balls[i][0]))
        canvas.move(balls[i][1],dx,  dy)



def main():
     move_balls()
     root.after(30, main)

if __name__ == "__main__":
    init_main_window()
    init_ball_catch_game()
    main()
    root.mainloop()

    print("Приходите поиграть еще!")

