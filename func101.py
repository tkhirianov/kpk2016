from drawman101 import *
novid()
col()
size()
axis()
grid()
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
