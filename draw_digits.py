from digits import *

t.penup()
t.backward(250)
n = input()
#введённое число - строка. Предполагаем, что введено именно число
length = len(n)# получаем длину строки
a=[]# заводим пустой список
for i in range(length):
    a.append(int(n[i]))# заполняем список числами, полученными из введенной строки
    if a[i] == 1:       # и печатаем их с помощью черепашки
        digit_one(50)
        t.forward(20)
    elif a[i] == 2:
        digit_two(50)
        t.forward(20)
    elif a[i] == 3:
        digit_three(50)
        t.forward(20)
    elif a[i] == 4:
        digit_four(50)
        t.forward(20)
    elif a[i] == 5:
        digit_five(50)
        t.forward(20)
    elif a[i] == 6:
        digit_six(50)
        t.forward(20)
    elif a[i] == 7:
        digit_seven(50)
        t.forward(20)
    elif a[i] == 8:
        digit_eight(50)
        t.forward(20)
    elif a[i] == 9:
        digit_nine(50)
        t.forward(20)
    elif a[i] == 0:
        digit_zero(50)
        t.forward(20)
t.hideturtle()

