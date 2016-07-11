from turtle import Turtle
default_scale = 1
def init_drawman():
    ''' Инициализация черепашки '''
    global t, x_current, y_current, _drawman_scale
    shag=40
    vod=0.5
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale(shag,vod)


def drawman_scale(shag,vod):
    global _drawman_scale, _shag,_vod
    '''
    Масштаб 
    shag - шаг сетки
    vod - единиц в одном делении сетки
    '''
    _shag=shag
    _vod=vod
    _drawman_scale = shag/vod
    # print(_shag,_vod,_drawman_scale)


def test_drawman():
    """
    Тестирование работы Чертёжника
    """
    novid()
    col()
    size()
    axis()
    # grid()
    edin()

    pen_down()
    # График функции
    col('lightblue')
    pen_width(wid=3)
    x = -5.0
    pen_up()
    y=x**2
    to_point(x, y)
    pen_down()
    while x <= 5:
        x += 0.2
        y=x**2
        to_point(x,y)
        
    pen_up()

    
    # Возврат в начало
    x_current = 0
    y_current = 0
    to_point(0, 0)
    pen_down()
    pen_width(4)
    col('red')
    for i in range(5):
        on_vector(1,2)
        on_vector(0,-2)


def novid():
    global t
    t.hideturtle()

def vid():
    global t
    t.showtirtle()

def pen_down():
    global t
    t.pendown()

def pen_up():
    global t
    t.penup()

def on_vector(dx, dy):
    ''' Сместиться на вектор '''
    global t,x_current, y_current,_drawman_scale
    #  Определение текущих координат черепашки
    x_current,  y_current=t.position()
    x_current=x_current+_drawman_scale*dx
    y_current=y_current+_drawman_scale*dy
    # print('вход вектор: ',x_current, y_current)
    t.goto(x_current, y_current)
    # print('выход вектор: ',t.position())

def to_point(x, y):
    ''' Сместиться в точку с учетом масштаба '''
    global t,x_current, y_current,_drawman_scale
    x_current = x
    y_current = y
    # print('goto')
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)

def col(c='red'):
    ''' Цвет'''
    global t
    t.pencolor(c)

def size():
     '''Размеры холста'''
     global t,w,h, _drawman_scale,_shag, _vod
     w=20*_shag
     h=20*_shag
     t.screen.screensize(w,h)

def pen_width(wid=2):
    '''Ширина пера'''
    global t
    t.width(wid)

def axis():
    global t,w,h,_drawman_scale,_vod
    pass
    t.speed(10)
    # t.turtlesize(2)
    # Вертикальные линии
    t.width(3)
    t.home()

    # Горизонтальные линии
     # t.reset()
     # t.tracer(0)
    t.color('#000000')
#
    t.write('  0,0')
#
    x=0
    y=-10*_shag
    coords=" "+str(x)+", "+str(-10*_vod)
    t.goto(x, y)
    t.write(coords)

#    Начинаем оси рисовать
    t.down()
    x=0
    y=10*_shag
    coords=str(x)+", "+str(10*_vod)
    t.goto(x, y-_shag/2)
    t.left(90)
    t.stamp()
    t.right(90)
    t.write(coords)
#
    t.up()
    x=-10*_shag
    y=0
    coords=str(-10*_vod)+", "+str(y)
    t.goto(x, y)
    t.write(coords)
#
    t.down()
    x=10*_shag
    y=0
    coords=str(10*_vod)+", "+str(y)
    t.goto(x, y)

    t.stamp()
    t.write(coords)
#
def grid():
    global t,w,h,_drawman_scale,_shag
    pass
    
    t.width(1)
    t.speed(10)
     # Вертикальные линии
    # shag=50*_drawman_scale
    x=-w/2
    y=h/2
    col('gray')
    while x<=w/2:
        t.up()
        t.goto(x,y)
        t.down()
        if x!=0:
            t.goto(x,-h/2)
        x+=_shag
    else:
        t.up()

     # Горизонтальные линии
    x=-w/2
    y=h/2
    # col('lightngray')
    while y>=-h/2:
        t.up()
        t.goto(x,y)
        t.down()
        if y!=0:
            t.goto(w/2,y)
        y-=_shag
    else:
        t.up()

def edin():
    global t,w,h,_drawman_scale,_shag,_vod
    # print ('Вошли в шаг')
    t.color('#000000')
    t.up()
    #edin=shag # Единичный отрезок типо
    x=_shag
    y=0
    coords=" "+str(_vod)
    t.goto(_shag, y)
    # t.down()
    t.write(coords)
    x=0
    y=_shag
    coords="  "+str(_vod)
    t.goto(x, _shag)
    t.write(coords)



init_drawman()
if __name__ == '__main__':
    import time # Отсюда вынимаем sleep(sec.)
    '''  Вызываем функцию тестирования чертежника в главно модуле '''
    test_drawman()
    # t.mainloop()
    time.sleep(8)
