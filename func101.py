from drawman101 import *
import math
shag=80
vod=0.5
drawman_scale(shag,vod)
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
y=math.sin(x)
to_point(x, y)
pen_down()
while x <= 5:
    x += 0.2
    y=math.sin(x)
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
