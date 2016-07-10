from turtle import Turtle
default_scale = 10 #коэффициент масштабирования Чертежника, по умолчанию = 10
default_pen_size = 1 #толщина линии Чертежника, по умолчанию = 1

def init_drawman():
    global t, x_current, y_current, _drawman_scale, _drawman_pen_size
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(default_scale)
    drawman_pen_size(default_pen_size)


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale

def drawman_pen_size(pen_size):
    """
    :param pen_size: толщина линии Чертежника, диапазон от 1 до 10
    """
    global _drawman_pen_size
    if pen_size > 10:
        _drawman_pen_size = t.pensize(10)
    elif pen_size < 1:
        _drawman_pen_size = t.pensize(1)
    else:
        _drawman_pen_size = t.pensize(pen_size)


def test_drawman():
    """
    Тестирование работы Чертёжника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)

def drawman_draw_grid(color_grid):
    """
    рисует кооринтаную сетку без осей
    запоминает размер окна поля
    x_width - ширина окна поля в пикселах
    y_height - высота окна поля в пикселах
    :param color_grid: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :return:
    """
    x_width = t.screen.window_width()
    y_height = t.screen.window_height()
    t.speed(25)
    drawman_draw_Hline(x_width, y_height, color_grid)
    drawman_draw_Vline(x_width, y_height, color_grid)
    pen_up()
    to_point(0, 0)
    t.speed(1)

def drawman_draw_Vline(x_width, y_height, color):
    """
    рисование линий сетки из центра поля (т.е. из начальной позиции Чертежника)

    рисует вертикальные линии сетки отельно по каждой четверти, учитывая масштабирование Четрежника

    :param color: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :param x_width: ширина окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :param y_height: высота окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :return:
    """
    x = 0
    y = 0
    t.goto(x, y)
    while x <= x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, y_height//2)
        t.penup()
        x = x + x_width//_drawman_scale

    x = 0
    y = 0
    t.goto(x, y)
    while x >= -x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, y_height//2)
        t.penup()
        x = x - x_width//_drawman_scale

    x = 0
    y = 0
    t.goto(x, y)
    while x >= -x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, -y_height//2)
        t.penup()
        x = x - x_width//_drawman_scale

    x = 0
    y = 0
    t.goto(x, y)
    while x <= x_width//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x, -y_height//2)
        t.penup()
        x = x + x_width//_drawman_scale


def drawman_draw_Hline(x_width, y_height, color):
    """
    рисование линий сетки из центра поля (т.е. из начальной позиции Чертежника)

    рисует горизонтальные линии сетки отельно по каждой четверти, учитывая масштабирование Четрежника

    :param color: цвет линий сетки указывается пользоватлем Чертежника при вызове команды drawman_draw_grid(color)
    :param x_width: ширина окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    :param y_height: высота окна поля Чертежника, автоматически определяется при вызове команды drawman_draw_grid()
    """
    y = 0
    x = 0
    t.goto(x, y)
    while y <= y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x_width//2, y)
        t.penup()
        y = y + y_height//_drawman_scale

    y = 0
    x = 0
    t.goto(x, y)
    while y >= -y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(x_width//2, y)
        t.penup()
        y = y - y_height//_drawman_scale

    y = 0
    x = 0
    t.goto(x, y)
    while y >= -y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(-x_width//2, y)
        t.penup()
        y = y - y_height//_drawman_scale

    y = 0
    x = 0
    t.goto(x, y)
    while y <= y_height//2:
        t.pencolor(color)
        t.goto(x, y)
        t.pendown()
        t.goto(-x_width//2, y)
        t.penup()
        y = y + y_height//_drawman_scale

def pen_down():
    t.pendown()


def pen_up():
    t.penup()


def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)


def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)


init_drawman()
if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(10)