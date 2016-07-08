import turtle


def init_drawman():
    global t, x_current, y_current, _drawman_scale
    default_scale = 0
    while default_scale<10 or default_scale>50:
            print('Введите число от 10 до 50 (масштаб координатной сетки)')
            default_scale=int(input())
    t=turtle.Turtle()
    x_current=0
    y_current=0
    drawman_scale(default_scale)
    turtle.setup(20*default_scale,20*default_scale)#устанавливаем размеры экрана
    grid(default_scale)
    axis(default_scale)
    x_current=0
    y_current=0
    t.goto(x_current,y_current)

def axis(scale): #координатные оси ( масштаб)
    # ось Х
    pen_up()
    t.goto(-scale*10, 0)
    pen_down()
    t.goto(scale*10-10,0)
    # стрелочка на оси Х
    x,y=t.pos()
    t.begin_fill()
    t.goto(x-10,y+10)
    t.goto(x-10,y-10)
    t.goto(x,y)
    t.end_fill()
    #  ось У
    pen_up()
    t.goto(0,-scale*10)
    pen_down()
    t.goto(0,scale*10-10)
    # стрелочка на оси У
    x,y=t.pos()
    t.begin_fill()
    t.goto(x-10,y-10)
    t.goto(x+10,y-10)
    t.goto(x,y)
    t.end_fill()
    pen_up()

def grid(scale):    # рисуем сетку (масштаб)
    t.color ('lightgray')
    x=-10*scale # вертикальные
    for k in range(20):
        pen_up()
        t.goto(x,-scale*10)
        pen_down()
        t.goto(x, scale*10)
        x+=scale
    y=10*scale # горизонтальные
    for k in range(20):
        pen_up()
        t.goto(-scale*10, y)
        pen_down()
        t.goto(scale*10, y)
        y-=scale
    t.color('black')
    pen_up()


def drawman_scale(scale):
    global _drawman_scale
    _drawman_scale = scale

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