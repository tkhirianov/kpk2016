#-*- coding: utf-8 -*

"""
Доделать
 выбор скорости
 показать, если ли другие варианты, давать выбирать их
 кнопку пояснение (аудио)
 кнопку подсказка (
"""


"""
Модуль "Робот" для обучения программированию. Версия 2.0
1. знакомство с командами управления и закраски, обход стены
2. процедуры (функции)
3. условие (ветвление)
4. for
5. while дойти до стены, обойти стену, обойти две стены, пройти по закрашенным, по стене, закрасить всё поле
6. while закрасить коридоры
7. переменная, счетчик, текст в ячейках, while до стены и обратно
8. закрасить отмеченные (использование if) (есть одна задача на установку стен)
9. закрасить треугольниками, найти сумму, закрасить четные, пройти спиралью
10. поиск пути, закрасить все. Рекурсия (вводная задача рекурсии 7-0)

Разрешено любое использование при упоминании авторства и сайта progras.ru.
Часть задач была "подсмотрена" в PascalABC

Сайт: progras.ru
skype: boris_vlasenko
email: boris-vlasenko@yandex.ru
phone: +7(905)505-49-49


Пожелания к новой версии:
1. Добавить "пульт прямого управления"
2. Сделать кнопку для перезапуска задачи без закрытия формы
3. Сделать кнопку для прямого перехода в форум

# Далее - Чертежник, черепушка, еще что-нибудь (робот без клеток, например)
# Робота на JS и HTML5
# Робота в Вконтак - обучение программированию.
# Войну Роботов во Вконтакт (обучение программированию)
"""
from tkinter import Tk, Canvas, Label, Button, Frame
from random import randrange as rnd
import  time, os
if __name__ != 'robot':
    print("Этот файл запускать не следует.")
    if not os.path.exists('task.py'):
        f1 = open('task.py','w')
        f1.write("""#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1-1')
def task():
	pass
	#------- пишите код здесь -----
	
	
	
	
	#------- пишите код здесь -----
r.start(task)

#Отступ слева (tab) сохранять!
#r.help() - Список команд и краткие примеры
#r.demo() - показать решение этой задачи (только результат, не текст программы)
#r.demoAll() - показать все задачи (примерно 20 минут)

#r.rt() - вправо
#r.rt(3)- вправо на 3
#r.dn() - вниз
#r.up() - вверх
#r.lt() - влево
#r.pt() - закрасить  Paint

#r.cl() - закрашена ли клетка? Color
#r.fr() - свободно ли справа? freeRight
#r.fl() - свободно ли слева?  freeLeft
#r.fu() - свободно ли сверху? freeUp
#r.fd() - свободно ли снизу?  freeDown

#r.wr() - стена ли справа? freeRight
#r.wl() - стена ли слева?  freeLeft
#r.wu() - стена ли сверху? freeUp
#r.wd() - стена ли снизу?  freeDown


#red - красный
#blue - синий
#yellow - желтый
#green - зеленый
""")
        f1.close()
        if os.path.exists('task.py'): print("Был создан файл task.py - запустите его")
        else: print("""Не удалось создать task.py. Попробуйте создать его самостоятельно с таким содержанием:
#----начало файла task.py------------------------
#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task1-1')
r.help() # Список команд. Уберите, если не нужно
#------- пишите код здесь vvvv -----

#------- пишите код здесь ^^^^ ----- 
r.end()
#----конец файла task.py------------------------
        """)
    else: print("Запустите task.py")
    print("""    

Сайт: progras.ru
skype: boris_vlasenko
email: boris-vlasenko@yandex.ru
phone: +7(905)505-49-49
""")

class rmap():
    _var = [1]
    _nc = 0
    _nr = 0
    _r = 0
    _c = 0
    _size = 0
    _w = 0
    _d = 0
    _NoneUpdate = False
    _Nonelabel = False
    _Nonegettext = False
    _field = []
    _endPoint = (0,0)

    _robot = '' # рисунок Робота (синее кольцо)
    _park = ''

    _canvas = ''
    sleep = 0
    _task = ''
    _solve = ''
    _test = ''
    _res = ''
    _bum = 0

    m = []
    m.append('task1-1')
    m.append('task1-2')
    m.append('task1-3')
    m.append('task1-4')
    m.append('task1-5')

    m.append('task2-1')
    m.append('task2-2')
    m.append('task2-3')
    m.append('task2-4')
    m.append('task2-5')

    m.append('task3-1')
    m.append('task3-2')
    m.append('task3-3')
    m.append('task3-4')
    m.append('task3-5')
    m.append('task3-6')
    m.append('task3-7')
    m.append('task3-8')
    m.append('task3-9')
    m.append('task3-10')

    m.append('task4-1')
    m.append('task4-2')
    m.append('task4-3')
    m.append('task4-4')
    m.append('task4-5')
    m.append('task4-6')
    m.append('task4-7')
    m.append('task4-8')
    m.append('task4-9')
    m.append('task4-10')
    m.append('task4-11')
    m.append('task4-12')
    m.append('task4-13')
    m.append('task4-14')
    m.append('task4-15')
    m.append('task4-16')

    m.append('task5-1')
    m.append('task5-2')
    m.append('task5-3')
    m.append('task5-4')
    m.append('task5-5')
    m.append('task5-6')
    m.append('task5-7')
    m.append('task5-8')
    m.append('task5-9')
    m.append('task5-10')
    m.append('task5-11')
    m.append('task5-12')
    m.append('task5-13')
    m.append('task5-14')

    m.append('task6-1')
    m.append('task6-2')
    m.append('task6-3')
    m.append('task6-4')
    m.append('task6-5')
    m.append('task6-6')
    m.append('task6-7')
    m.append('task6-8')

    m.append('task7-0')
    m.append('task7-1')
    m.append('task7-2')
    m.append('task7-3')
    m.append('task7-4')
    m.append('task7-5')
    m.append('task7-6')
    m.append('task7-7')

    m.append('task8-1')
    m.append('task8-2')
    m.append('task8-3')
    m.append('task8-4')
    m.append('task8-5')
    m.append('task8-6')
    m.append('task8-7')
    m.append('task8-8')
    m.append('task8-9')
    m.append('task8-10')
    m.append('task8-11')
    m.append('task8-12')
    m.append('task8-13')
    m.append('task8-14')
    m.append('task8-15')
    m.append('task8-16')
    m.append('task8-17')
    m.append('task8-18')
    m.append('task8-19')
    m.append('task8-20')
    m.append('task8-21')
    m.append('task8-22')
    m.append('task8-23')
    m.append('task8-24')
    m.append('task8-25')
    m.append('task8-26')
    m.append('task8-27')
    m.append('task8-28')
    m.append('task8-29')
    m.append('task8-30')

    m.append('task9-1')
    m.append('task9-2')
    m.append('task9-2')
    m.append('task9-3')
    m.append('task9-4')
    m.append('task9-5')
    m.append('task9-6')
    m.append('task9-7')
    m.append('task9-8')
    m.append('task9-9')
    m.append('task9-10')

    m.append('task10-1')
    m.append('task10-2')
    m.append('task10-3')
    m.append('task10-4')
    m.append('task10-5')  

    class _v: # будет содержать изображение текста и квадратиков закраски и меток. Чтобы можно было "поднимать изображение"
        text = '' 
        label = '' 
        color = ''

    class _Tcell():
        color = ''
        text = ''
        label = '' # color
        wUp = False
        wLeft = False
        v = ''

    def help(self):
        """ Вывести список команд Робота
Примеры использования по команде r.help_full()
"""
        print("""
Пояснение по каждой команде: print команда.__doc__
Например:
print r.color.__doc__

---=: Команды перемещения :=---
r.rt() # Вправо
r.lt() # Влево
r.dn() # Вниз
r.up() # Вверх
r.jumpTo(r,c) # Прыжок в точку. Без особых указаний в задачах не использовать
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

---=: Команды изменения среды :=---
r.pt([цвет]) # Закрасить указанным цветом. По умолчанию зеленым
r.sw(направление) # Установить стену с указанной стороны
r.settext(тест) # Вписать в клетку текст
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

---=: Команды обратной связи :=---
r.cl() # Каким цветом закрашена клетка? r.color()
r.label() # Какого цвета метка в клетке?
r.gettext() # Какой текст в клетке?

r.getCoords() # Где Робот?
r.getCoordR() # В какой строке Робот?
r.getCoordС() # В каком столбце Робот?

r.fu() # Сверху свободно?
r.fd() # Снизу свободно?
r.fr() # Справа свободно?
r.fl() # Слева свободно?

r.wu() # Сверху стена?
r.wd() # Снизу стена?
r.wr() # Справа стена?
r.wl() # Слева стена?

r.isPark # Робот на парковке?
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

---=: Дополнительно :=---
r.sleep = 0.4 # Установить размер задержки после каждого хода. Меньше значение - быстрее Робот.
r._NoneUpdate = False # Отключить прорисовку поля
r._NoneUpdate = True # Включить прорисовку поля
r.demo() # Показать, что нужно сделать в текущей задаче
r.demoAll() # Показать все задачи (с решениями, по очереди)
r.randcolor() # Генерировать случайный цвет
-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=

""")

    def help_full(self):
        """ Примеры. Для получения списка команд r.help()
Примеры использования по команде r.help_full()
Больше информации по каждой команде: print команда.__doc__
Например:
print r.color.__doc__
"""
        print("""
Не реализовано в данной версии. 
Если нужно - пишите на boris-vlasenko@yandex.ru или на сайте progras.ru
""")

    def demo(self):
        """Показать выполнение задачи
Пример использования:
#-------------------
r.demo()
#-------------------

Для уcкорения использовать r.sleep = 0.01
В задании 10-3(4/5) можно отключить обновление экрана
#-------------------
r._NoneUpdate = True
r.demo()
r._NoneUpdate = False
#-------------------
"""
        global r
        r = self
        exec(self._solve)

    def demoAll(self):
        """Показать выполнение всех заданий в автоматическом режиме
Пример использования:

#-------------------
r.demoAll()
#-------------------

Для того, чтобы Робот двигался быстрее, используйте
#-------------------
r.sleep = 0 
r.demoAll()
#-------------------

"""
        global r
        r = self
        for x in r.m:
            r.lm(x)
            print(x)
            r.demo()
            r.test()
            r.pause()
          
    def __init__(self):
        self._w = 4 # толщина стен
        self._d = 4 # на столько меньше клетки закраска (с каждой стороны)
        self.sleep = 0.1 # замедление
        self._font_size = self._size // 2
        self._tk = Tk()
        self._tk.geometry('+0+0')
        x = (self._tk.winfo_screenwidth() - self._tk.winfo_reqwidth()) / 3
        y = (self._tk.winfo_screenheight() - self._tk.winfo_reqheight()) / 4
        self._tk.wm_geometry("+%d+%d" % (x, y))
        self._tk.title('Robot-hobot')
        self._canvas = Canvas(self._tk, width=(self._size*(self._nc+1)), height=(self._size*(self._nr+1)), bg="gray")

        buttons = Frame(self._tk)

        self.task = Label (self._tk, justify = 'left')
        self.res = Label (self._tk, justify = 'left')

        self._but_start = Button(buttons,text = 'start',width=10,height=1)
        self._but_start.bind('<ButtonRelease-1>',self.but1)

        self._but_demo = Button(buttons,text = 'demo',width=10,height=1)
        self._but_demo.bind('<ButtonRelease-1>',self.but_demo)

        self._but_reload = Button(buttons,text = 'reload',width=10,height=1)
        self._but_reload.bind('<ButtonRelease-1>',self.but_reload)

        self._but_load_next = Button(buttons,text = 'load next',width=10,height=1)
        self._but_load_next.bind('<ButtonRelease-1>',self.but_load_next)

        buttons.grid(row=0, column=0, sticky = "w") 
        self._canvas.grid(row=1, column=0, sticky = "e")
        self._but_start.pack(side = "left")
        self._but_demo.pack(side = "left")
        self._but_reload.pack(side = "left")
        self._but_load_next.pack(side = "left")
        self.task.grid(row=3, column=0, sticky = "w")
        self.res.grid(row=4, column=0, sticky = "w")

##        self.loadmap()
    def but_load_next(self,event):
    	print ("load next")
    	self.lm(self.m[self.m.index(self._cur_map)+1])
    	
    def but_demo(self,event):
        print ("demo")
        self.demo()
        self.test()
		
    def but1(self,event):
    	print ('start')
    	#self.lm(self._cur_map)
    	self.solve_task()
    	self.test()
    	
    def but_reload(self,event):
        print ("reload")
        self.lm(self._cur_map)

            
    def clear (self):
        "Очистка данных (без перерисовки)"
        self._canvas.delete('all')
        self._field = []
        self._park = []
        self._Nonelabel = False
        self._NoneisPark = False
        self._Nonesettext = False
        self._test = ''
        self._res = ''
        self._bum = 0

        for r in range(1,self._nr+2):
            row = []
            for c in range(1,self._nc+2):
                row.append (self._Tcell())
            self._field.append(row)

        for r in range (1,self._nr):
            for c in range(1,self._nc):
                self._field[r][c].text = ''
                self._field[r][c].color = ''
                self._field[r][c].label = ''
                self._field[r][c].wUp = False
                self._field[r][c].wLeft = False
                self._field[r][c].v = self._v()
                
        for c in range (1,self._nc):
            self._field[1][c].wUp = True
            self._field[self._nr][c].wUp = True

        for r in range (1,self._nr):
            self._field[r][1].wLeft = True
            self._field[r][self._nc].wLeft = True

        self._solve = ''
        self._r = 1
        self._c = 1

    def _paintMap(self): 
        "Перерисовка  по имеющимся данным"
        remc = self._c
        remr = self._r
        size = self._size
        sleep = self.sleep
        self.sleep = 0

        self._bg = [self._canvas.create_rectangle(1,1,(size*(self._nc+1)), (size*(self._nr+1)), fill="gray")]
        # создать поле
        
        for r in range (1, self._nr+1):
            self._bg.append(self._canvas.create_line(size,r*size,self._nc*size,r*size))
            if r < self._nr: self._canvas.create_text(size/2,r*size+size/2,text=r)
        for c in range (1, self._nc+1):
            self._bg.append(self._canvas.create_line(c*size,size,c*size,self._nr*size))
            if c < self._nc: self._bg.append(self._canvas.create_text(c*size+size/2,size/2,text=c))
        # клетки и номера столбцов и строк

        for r in range (1,self._nr): 
            for c in range(1,self._nc):
                self._r = r
                self._c = c
                if  self._field[r][c].wUp: # стена сверху
                    self.setWall('up')
                if  self._field[r][c].wLeft: # стена слева
                    self.setWall('left')
                if  self._field[r][c].color != '' : # закраска
                    self.paint(self._field[r][c].color)
                if  self._field[r][c].label != '' : # метка0000
                    d = self._d 
                    x1 = self._size*(c)
                    x2 = self._size*(c+1)
                    y1 = self._size*(r)
                    y2 = self._size*(r+1)
                    self._canvas.delete(self._field[r][c].v.label)
                    self._field[r][c].v.label = self._canvas.create_rectangle(x1+d,y1+d,x2-d,y2-d, width = d-1, outline = self._field[r][c].label)
                    self._canvas.lift(self._robot)
                self.settext(self._field[r][c].text) # текст

        for self._c in range (1,self._nc): 
                if  self._field[self._nr][self._c].wUp: # стена сверху
                    self.setWall('down')

        for self._r in range (1,self._nr): 
                if  self._field[self._r][self._nc].wLeft: # стена слева
                    self.setWall('right')

        r = self._endPoint[0]
        c = self._endPoint[1]
        self._canvas.delete(self._park)
        self._park = self._canvas.create_oval (c*size+6,r*size+6, c*size+size-6,r*size+size-6, width = 3, outline = 'yellow')
        # конечная точка
        
        self.jumpTo((remr,remc))
        self._task = '\n'+self._task
        self.task.config(text = self._task)
        self.res.config(text = 'Проверка еще не выполнялась')
        self._update()
        self.sleep = sleep
        #self.pause()

        
    def _update(self):
        "Обновить canvas"
        if not self._NoneUpdate:
            self._canvas.update()
            time.sleep(self.sleep)
        

    def test(self):
        """Проверить, выполнено ли задание. 
Возвращает истину, если выполнено или ложь, если не выполнено.
"""
        t = w = p = l = True # w -стены, p - парковка, l - закраска, t - текст
        if self._test != '-':
            if self._test == '':
                r = c = 1
                while  l  and (r <= self._nr) and (c <= self._nc):
                    if self._field[r][c].label != self._field[r][c].color:
                        l = False
                    if (c < self._nc):
                        c +=1
                    else:
                        c = 1
                        r += 1
                if self._endPoint != self.getCoords():
                    p = False
            else:
                exec(self._test)
    #        print (l,p) # переделать на вывод значка результата и комментария
            self._res = '\n'
            self._res += '-------------------------------------'
            self._res += '\n'
            if t and w and l and p: self._res += 'Задача выполнена верно'
            if not l: self._res += 'Закрашены не все клетки или закрашены не тем цветом\n'
            if not p: self._res += 'Робот не на Парковке (желтый круг)\n'
            if not w: self._res += 'Установлены не все стены или установлены в неправильных местах\n'
            if not t: self._res += 'Текст в ячейках не вписан или вписан неправильно\n'
            if self._bum: self._res += 'Робот разбился (врезался в стену)\n'
            self.res.config(text = self._res)
        else:
            self._res += '\n'
            self._res += '-------------------------------------'
            self._res += '\n'
            self._res += 'Нет автоматической проверки'
            self.res.config(text = self._res)

        self._update()
        return t and w and p and l

    def start(self,fun):
        #self.test()
        self.solve_task = fun
        self._tk.mainloop()

    def full_test(self):
        "Выполнение полного текста, со всеми вариантами поля."
        z = self._var
        for x in z:
            print(self._cur_map,'['+str(x)+'/'+str(self._var[-1])+']', end=' ')
            self.pause()
            if not self.test():
                print("fail")
                break
            else:
                print("ok")
            if x != z[-1]:
                self.lm(self._cur_map,x)
        print("end of test")

##Робот    

    def pause(self,t=1):
        """Приостановка выполнения программы. Пауза в секундах. 
#-------------------
r.pause() # пауза в одну секунду
#-------------------
r.pause(2) # пауза две секунды
#-------------------
"""
        time.sleep(t)
		
    def left(self, a = 1):
        """Шаг влево
#-------------------
r.left()
#-------------------
r.lt()
#-------------------
r.lt(3) 
#-------------------
"""
        if a == 1:
            if self.freeLeft():
                self._c -= 1
                self._canvas.move(self._robot,-self._size*a,0)
                self._update()
            else:
                self._stop()
        else :
            for z in range(0,a):
                self.left()

    def right(self, a = 1):
        """ Шаг вправо        
#-------------------
r.right()
#-------------------
r.rt()
#-------------------
r.rt(5)
#-------------------
"""        
        if a == 1:
            if self.freeRight():
                self._c += 1
                self._canvas.move(self._robot,self._size*a,0)
                self._update()
            else:
                self._stop()
                
        else :
            for z in range(0,a):
                self.right()
        
    def up(self, a = 1):
        """Шаг вверх
#-------------------
r.up()
#-------------------
r.up(3)
#-------------------
"""
        if a == 1:
            if self.freeUp():
                self._r -= 1
                self._canvas.move(self._robot,0,-self._size*a)
                self._update()
            else:
                self._stop()
        else :
            for z in range(0,a):
                self.up()
        
    def down(self, a = 1):
        """ Шаг вниз
#-------------------
r.down()
#-------------------
r.dn()
#-------------------
r.dn(4)
#-------------------
"""
        if a == 1:
            if self.freeDown():
                self._r += 1
                self._canvas.move(self._robot,0,self._size*a)
                self._update()
            else:
                self._stop()
        else :
            for z in range(0,a):
                self.down()
                
    def jumpTo(self,coord=(1,1)):
        """Прыжок в клетку с указанными координами. Через стены.
#-------------------
r.jumpTo((2,3)) # Робот окажется в третьем столбце второй строки
#-------------------
"""

        r = coord[0]
        c = coord[1]
        if ( 0 < r < self._nc) and (0 < c < self._nc):
            self._r = r
            self._c = c
            size = self._size
            self._canvas.coords(self._robot, c*size+4,r*size+4, c*size+size-4,r*size+size-4)
            self._canvas.lift(self._robot)
            self._update()
        else:
            print("Попытка переместиться за пределы поля. Отказано.")

    def paint (self, color = 'green'):
        """ Закрасить текущую клетку выбранным цветом. Если цвет не указан, то зеленым
#-------------------
r.paint() # Закрасит текущую клетку зеленым цветом
#-------------------
r.pt() # Закрасит текущую клетку зеленым цветом
#-------------------
r.pt('red') # Закрасит текущую клетку красным цветом
#-------------------
r.pt(r.randcolor()) # Закрасит текущую клетку случайным цветом
#-------------------
r.pt(r.label()) # Закрасит текущую клетку цветом метки в этой клетке
#-------------------
"""
        d = self._d+1
        self._field[self._r][self._c].color = color

        x1 = self._size*(self._c)
        x2 = self._size*(self._c+1)
        y1 = self._size*(self._r)
        y2 = self._size*(self._r+1)
        self._canvas.delete(self._field[self._r][self._c].v.color)
        self._field[self._r][self._c].v.color = self._canvas.create_rectangle(x1+d,y1+d,x2-d,y2-d, width = 0, fill = color)
        self._canvas.lift(self._field[self._r][self._c].v.text)
        self._canvas.lift(self._robot)
        self._canvas.lift(self._park)
        self._update()

    def setWall (self, target):
        """ Установить стену с указанной стороны
#-------------------
r.sw('up') # Установить стену сверху
#-------------------
r.sw('left') # Установить стену слева 
#-------------------
r.sw('down') # Установить стену снизу
#-------------------
r.sw('right') # Установить стену справа
#-------------------
"""
        size = self._size
        w = self._w
        if target == 'up':
            r = self._r
            c = self._c
            x1 = size*(c)-1
            x2 = size*(c+1)+1
            y1 = size*(r)
            y2 = size*(r+1)
            self._field[r][c].wUp = True
            self._canvas.create_line(x1,y1,x2,y1, width = w)
        elif target == 'left':
            r = self._r
            c = self._c
            x1 = size*(c)
            x2 = size*(c+1)
            y1 = size*(r)-1
            y2 = size*(r+1)+1
            self._field[r][c].wLeft = True
            self._canvas.create_line(x1,y1,x1,y2, width = w)
        elif target == 'down':
            r = self._r+1
            c = self._c
            x1 = size*(c)-1
            x2 = size*(c+1)+1
            y1 = size*(r)
            y2 = size*(r+1)
            self._field[r][c].wDown = True
            self._canvas.create_line(x1,y1,x2,y1, width = w)
        elif target == 'right':
            r = self._r
            c = self._c+1
            x1 = size*(c)
            x2 = size*(c+1)
            y1 = size*(r)-1
            y2 = size*(r+1)+1
            self._field[r][c].wRight = True
            self._canvas.create_line(x1,y1,x1,y2, width = 4)
        self._update()

    def wallUp (self):
        """ Возвращает истину, если сверху есть стена
#-------------------
if r.wallUp(): r.pt() # Закрасить, если сверху стена
#-------------------
if r.wu(): r.pt() # Закрасить, если сверху стена
#-------------------
if r.wu(): 
    r.pt() # Закрасить, если сверху стена
    r.rt() # Перейти вправо
#-------------------
while r.wu(): # Идти вправо, пока сверху есть стена
    r.rt()
"""
        return self._field[self._r][self._c].wUp 

    def wallDown (self):
        """ Возвращает истину, если снизу есть стена
#-------------------
if r.wallDown(): r.pt() # Закрасить, если снизу стена
#-------------------
if r.wd(): r.pt() # Закрасить, если снизу стена
#-------------------
if r.wd(): 
    r.pt() # Закрасить, если снизу стена
    r.rt() # Перейти вправо
#-------------------
while r.wd(): # Идти вправо, пока снизу есть стена
    r.rt()
"""
        return self._field[self._r+1][self._c].wUp 

    def wallLeft (self):
        """ Возвращает истину, если слева есть стена
#-------------------
if r.wallLeft(): r.pt() # Закрасить, если слева стена
#-------------------
if r.wl(): r.pt() # Закрасить, если слева стена
#-------------------
if r.wl(): 
    r.pt() # Закрасить, если слева стена
    r.dn() # Перейти вниз
#-------------------
while r.wl(): # Идти вниз, пока слева есть стена
    r.dn()
"""
        return self._field[self._r][self._c].wLeft

    def wallRight (self):
        """ Возвращает истину, если справа есть стена
#-------------------
if r.wallRight(): r.pt() # Закрасить, если справа стена
#-------------------
if r.wr(): r.pt() # Закрасить, если справа стена
#-------------------
if r.wr(): 
    r.pt() # Закрасить, если справа стена
    r.dn() # Перейти вниз
#-------------------
while r.wr(): # Идти вниз, пока справа есть стена
    r.dn()
"""
        return self._field[self._r][self._c+1].wLeft

    def freeUp (self):
        """ Возвращает истину, если сверху свободно (нет стены)
#-------------------
if r.freeUp(): r.pt() # Закрасить, если сверху свободно
#-------------------
if r.fu(): r.up() # Шагнуть вверх, если сверху свободно
#-------------------
if r.fu(): 
    r.up() # Шагнуть вверх
    r.pt() # Закрасить
    r.dn() # Перейти вниз
#-------------------
while r.fu(): # Идти вверх, пока сверху свободно
    r.up()
"""
        return not self._field[self._r][self._c].wUp 

    def freeDown (self):
        """ Возвращает истину, если снизу свободно (нет стены)
#-------------------
if r.freeDown(): r.pt() # Закрасить, если снизу свободно
#-------------------
if r.fd(): r.dn() # Шагнуть вверх, если снизу свободно
#-------------------
if r.fd(): 
    r.dn() # Шагнуть снизу
    r.pt() # Закрасить
    r.up() # Перейти вверх
#-------------------
while r.fd(): # Идти вниз, пока снизу свободно
    r.dn()
"""
        return not self._field[self._r+1][self._c].wUp 

    def freeLeft (self):
        """ Возвращает истину, если слева свободно (нет стены)
#-------------------
if r.freeLeft(): r.pt() # Закрасить, если слева свободно
#-------------------
if r.fl(): r.lt() # Шагнуть влево, если слева свободно
#-------------------
if r.fl(): 
    r.lt() # Шагнуть влево
    r.pt() # Закрасить
    r.rt() # Перейти вправо
#-------------------
while r.fl(): # Идти влево, пока слева свободно
    r.lt()
"""
        return not self._field[self._r][self._c].wLeft

    def freeRight (self):
        """ Возвращает истину, если снизу свободно (нет стены)
#-------------------
if r.freeDown(): r.pt() # Закрасить, если снизу свободно
#-------------------
if r.fd(): r.dn() # Шагнуть вверх, если снизу свободно
#-------------------
if r.fd(): 
    r.dn() # Шагнуть снизу
    r.pt() # Закрасить
    r.up() # Перейти вверх
#-------------------
while r.fd(): # Идти вниз, пока снизу свободно
    r.dn()
"""
        return not self._field[self._r][self._c+1].wLeft

    def getCoords(self):
        " Возвращает координаты в виде (row,column)"
        return (self._r,self._c)

    def getCoordR(self):
        " Возвращает номер строки, в которой находиться Робот"
        return self._r

    def getCoordC(self):
        " Возвращает номер столбца, в которой находиться Робот"
        return self._c

    def isPark (self):
        " Возвращает истину, если Робот находиться на парковке"
        if self._NoneisPark: self.null()
        else: return self._endPoint == self.getCoords()

    def color (self):
        """ Возвращает цвет, которым закрашена клетка
Можно использовать для проверки, закрашена ли клетка:
#-------------------
# Закрасить, если сверху закрашено
r.up()
if r.color():
    r.dn()
    r.pt()
else:
    r.dn()
#-------------------
if r.color() == 'red': r.rt() # Вправо, если закрашено красным
#-------------------
"""
        return self._field[self._r][self._c].color
    
    def randcolor (self):
        """ Возвращает случайный цвет
#-------------------
r.pt(r.randcolor()) # Закрасить случайным цветом
#-------------------
# Закрасить соседнюю клетку тем же цветом, что и текущая
x = r.color()
r.rt()
r.pt(x)
#-------------------
"""
        cr = rnd(1,255,10)
        cg = rnd(1,255,10)
        cb = rnd(1,255,10)
        color =  "#%02X%02X%02X" %(cr,cg,cb)
        return str(color)


    def label (self):
        """ Возвращает цвет метки текущей клетки
#-------------------
if r.label() == 'red': r.pt('red') # Закрасить клетку красным, если метка красная
#-------------------
"""
        if self._Nonelabel: self.null()
        else: return self._field[self._r][self._c].label
    
    def gettext(self):
        """ Возвращает текст, записанный в ячейке. 
#-------------------
if r.gettext() != '': r.rt() # Перейти вправо, если в ячейке есть какой-нибудь текст
#-------------------
if r.gettext() == '3': r.rt() # Перейти вправо, если в ячейке записано 3
#-------------------
n = r.gettext()
if n: r.rt(n) # Перейти вправо на количество шагов, указанное в клетке
#-------------------
"""
        if self._Nonegettext: self.null()
        else: return self._field[self._r][self._c].text
    
    def settext(self,text):
        """ Записать текст в клетку
#-------------------
r.settext(3)
#-------------------
"""
        self._field[self._r][self._c].text = text
        d = 1
        x1 = self._size*(self._c)
        x2 = self._size*(self._c+1)
        y1 = self._size*(self._r)
        y2 = self._size*(self._r+1)
        self._canvas.delete(self._field[self._r][self._c].v.text)
        self._field[self._r][self._c].v.text =  self._canvas.create_text(self._c*self._size+self._size/2,self._r*self._size+self._size/2,text =
                                 self._field[self._r][self._c].text, font = ('Helvetica', self._font_size,'bold'))
        self._update()

    def _stop (self):
        print ("Bum!")
        self._bum = 1
        self._canvas.delete(self._robot)
        x = self._c
        y = self._r
        
        self._robot = self._canvas.create_oval(
            x*self._size+2*self._d,y*self._size+2*self._d,
            x*self._size+self._size-2*self._d,y*self._size+self._size-2*self._d,
            fill = '#FF0000')

        self.end()
        
    def null (self, *args):
        print('Эта команда запрещена к использованию в данной задаче. Ищите другой способ')
        return ''


    def loadmap(self,mn=m[0],variant=0):
        """ Загрузить карту (задачу)
#-------------------
r.loadmap('task10-5')
#-------------------
r.lm('task10-5') # Загрузить задачу по названию
#-------------------
r.lm(r.m[5]) # Загрузить задачу по номеру
#-------------------
# Вывести полный список названий и номеров заданий
for x in r.m:
    print r.m.index(x),x
#-------------------
"""
        self._tk.title(mn)
        self._cur_map = mn
        if mn == 'blank1':
            self._nc = 10
            self._nr = 10
            self._r = 1
            self._c = 1
            self._size = 40
            self.clear()
                
        elif mn == 'blank2':
            self._nc = 20
            self._nr = 20
            self._r = 1
            self._c = 1
            self._size = 25

            self.clear()
            
        elif mn == 'blank3':
            self._nc = 60
            self._nr = 40
            self._r = 1
            self._c = 1
            self._size = 15

            self.clear()
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task1-1':
            self._nc = 10
            self._nr = 7
            self._r = 1
            self._c = 1
            self._size = 30

            self.clear()
            self._solve = """
r.rt()
r.rt()
r.dn()
"""
            self._endPoint = (2,3)
            self._task = 'Робот должен дойти до отмеченной клетки\n'
            self._task += self._solve 
            self._task += 'скобки после команд писать обязательно! \n'
           
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task1-2':
            self._nc = 10
            self._nr = 10
            self._r = 1
            self._c = 1
            self._size = 30

            self.clear()
            self._field[3][3].label = 'green'
            self._endPoint = (4,5)
            self._solve = """
r.rt()
r.rt()
r.dn()
r.dn()
r.pt()
r.dn()
r.rt()
r.rt()
"""
            
            self._task = 'Робот должен дойти до клетки, отмеченной желтым кругом \n  Клетку, омеченную зеленым - закрасить зеленым \n \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task1-3':
            self._nc = 15
            self._nr = 15
            self._r = 1
            self._c = 1
            self._size = 30
            self.clear()
            self._field[1][5].label = 'green'
            self._field[4][1].label = 'red'
            self._endPoint = (4,5)
            self._solve = """
r.rt(4)
r.pt()
r.lt(4)
r.dn(3)
r.pt('red')
r.rt(4)
"""            
            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n'
            self._task += 'Клетку, омеченную зеленым - закрасить зеленым (green), \nкрасную - красным (red) \n \n'
            self._task += 'r.pt("red") - закрасить красным \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task1-4':
            self._nc = 15
            self._nr = 15
            self._r = 1
            self._c = 1
            self._size = 30
            self.clear()
            self._field[2][1].label = 'red'
            self._field[2][2].label = 'orange'
            self._field[2][3].label = 'yellow'
            self._field[2][4].label = 'green'
            self._field[2][5].label = 'cyan'
            self._field[2][6].label = 'blue'
            self._field[2][7].label = 'magenta'
            self._endPoint = (2,8)
            self._solve = """
r.dn()
r.pt('red')
r.rt()
r.pt('orange')
r.rt()
r.pt('yellow')
r.rt()
r.pt('green')
r.rt()
r.pt('cyan')
r.rt()
r.pt('blue')
r.rt()
r.pt('magenta')
r.rt()
"""            
            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n'
            self._task += 'Закрасить цветами - red, orange, yellow, green, cyan, blue, magenta \n'
            self._task += 'Название цвета - в кавычках, внутри скобок:  r.pt("cyan")'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task1-5':
            self._nc = 15
            self._nr = 15
            self._r = 1
            self._c = 1
            self._size = 30

            self.clear()
            self._field[1][4].wLeft = True
            self._field[2][4].wLeft = True
            self._endPoint = (1,8)
            self._solve = """
r.dn(2)
r.rt(7)
r.up(2)
"""            
            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n'
            self._task += 'Сквозь стены робот ходить не может. Стены нужно обходить\n'
            self._task += 'Следующая задача: task2-1'

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task2-1':
            self._nc = 10
            self._nr = 10
            self._r = 1
            self._c = 1
            self._size = 30

            self.clear()
            c = 1
            r = 1
            rcount  = 1
            ccount  = 1
            self._field[r + rcount+1][c+ccount+1].label = 'green'
            self._field[r + rcount+2][c+ccount+1].label = 'green'
            self._field[c + rcount][r+ccount+1].label = 'green'
            self._field[c + rcount+1][r+ccount].label = 'green'
            self._field[c + rcount+1][r+ccount+2].label = 'green'
            self._solve = """
r.sleep = 0.1
r.dn()
r.rt(2)
r.pt()
r.dn()
r.pt()
r.lt()
r.pt()
r.rt(2)
r.pt()
r.lt()
r.dn()
r.pt()
r.lt()
r.up(2)
"""

            
            self._endPoint = (2,2)
            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n Закрасить отмеченные. \n'
            self._task += 'Для ускорения робота использовать r.sleep = 0\n'

        ##-------------------------------------------------------------------------------------------------------
        elif mn == 'task2-2':
            self._nc = 20
            self._nr = 10
            self._r = 1
            self._c = 1
            self._size = 25
                
            self.clear()

            c = r = 1
            rcount  = 1
            for ccount in range(0,5):
                self._field[r + rcount+1][c+ccount*4+1].label = 'green'
                self._field[r + rcount+2][c+ccount*4+1].label = 'green'
                self._field[c + rcount][r+ccount*4+1].label = 'green'
                self._field[c + rcount+1][r+ccount*4].label = 'green'
                self._field[c + rcount+1][r+ccount*4+2].label = 'green'
            self._endPoint = (2,17)
            self._solve = """
r.sleep = 0
def fig():
    r.rt()
    r.pt()
    r.dn()
    r.pt()
    r.lt()
    r.pt()
    r.rt(2)
    r.pt()
    r.lt()
    r.dn()
    r.pt()
    r.lt()
    r.up(2)
def step():
    r.rt(4)
    
r.dn()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
"""   
        
            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n Закрасить отмеченные'
            """
            self._task += 'Для выполнения повторяющихся действий можно использовать процедуры \n'
            self._task += 'def sq() \n'
            self._task += '    r.rt()\n'
            self._task += '    r.pt("red")\n'
            self._task += '    .. и т.д (один элемент) \n'
            self._task += 'sq() # вызовы процедуры\n'
            self._task += 'sq() \n'
            self._task += 'sq() \n'
            self._task += 'sq() \n'
            """

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task2-3':
            self._nc = 40
            self._nr = 10
            self._r = 1
            self._c = 1
            self._size = 20

            self.clear()

            c = r = 1
            rcount  = 1
            for ccount in range(0,10):
                self._field[r + rcount+1][c+ccount*4+1].label = 'green'
                self._field[r + rcount+2][c+ccount*4+1].label = 'green'
                self._field[c + rcount][r+ccount*4+1].label = 'green'
                self._field[c + rcount+1][r+ccount*4].label = 'green'
                self._field[c + rcount+1][r+ccount*4+2].label = 'green'
            
            self._endPoint = (2,1)
            self._solve = """
r.sleep = 0
def fig():
    r.rt()
    r.pt()
    r.dn()
    r.pt()
    r.lt()
    r.pt()
    r.rt(2)
    r.pt()
    r.lt()
    r.dn()
    r.pt()
    r.lt()
    r.up(2)
def step():
    r.rt(4)
    
r.dn()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
step()
fig()
r.lt(36)
"""   

          
            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n Использовать процедуру\n'
            self._task += 'Для выполнения повторяющихся действий можно использовать процедуры \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task2-4':
            self._nc = 40
            self._nr = 20
            self._r = 1
            self._c = 1
            self._size = 20
 
                
            self.clear()

            c = r = 1
            for rcount in range(0,5):
                for ccount in range(0,10):
                    self._field[r + rcount*4+1][c+ccount*4+1].label = 'green'
                    self._field[r + rcount*4+2][c+ccount*4+1].label = 'green'
                    self._field[c + rcount*4][r+ccount*4+1].label = 'green'
                    self._field[c + rcount*4+1][r+ccount*4].label = 'green'
                    self._field[c + rcount*4+1][r+ccount*4+2].label = 'green'
            
            self._endPoint = (17,1)
            self._solve = """
r.sleep = 0
global fig
def fig():
    r.rt()
    r.pt()
    r.dn()
    r.pt()
    r.lt()
    r.pt()
    r.rt(2)
    r.pt()
    r.lt()
    r.dn()
    r.pt()
    r.lt()
    r.up(2)

def line():
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.lt(36)
line()
r.dn(4)
line()
r.dn(4)
line()
r.dn(4)
line()
r.dn(4)
line()
"""   


            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n Использовать процедуру\n'
            self._task += 'Для выполнения повторяющихся действий можно использовать процедуры \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task2-5':
            self._nc = 40
            self._nr = 20
            self._r = 1
            self._c = 1
            self._size = 20

            self.clear()

            c = r = 1
            for rcount in range(0,5):
                for ccount in range(0,10):
                    self._field[r + rcount*4+1][c+ccount*4+1].label = 'yellow'
                    self._field[r + rcount*4+2][c+ccount*4+1].label = 'red'
                    self._field[c + rcount*4][r+ccount*4+1].label = 'red'
                    self._field[c + rcount*4+1][r+ccount*4].label = 'red'
                    self._field[c + rcount*4+1][r+ccount*4+2].label = 'red'
            
            self._endPoint = (17,1)
            self._solve = """
r.sleep = 0
global fig
def fig():
    r.rt()
    r.pt('red')
    r.dn()
    r.pt('yellow')
    r.lt()
    r.pt('red')
    r.rt(2)
    r.pt('red')
    r.lt()
    r.dn()
    r.pt('red')
    r.lt()
    r.up(2)

def line():
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.rt(4)
    fig()
    r.lt(36)
line()
r.dn(4)
line()
r.dn(4)
line()
r.dn(4)
line()
r.dn(4)
line()
"""   

            self._task = 'Робота - до клетки, отмеченной желтым кругом.\n Использовать процедуру\n'
            self._task += 'Для выполнения повторяющихся действий можно использовать процедуры \n'
            self._task += 'След. задача: task3-1'

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-1':
            self._nc = 10
            self._nr = 10
            self._size = 30
                
            self.clear()

            self._var = [1,2]
            print(variant)
            if variant == 1:
                self._r = 2
                self._c = 2
                self._field[2][3].wLeft = True
                self._endPoint = (2,2)
                print("!!!!!!!!!!!!")
                print(variant)
            else:
                self._r = 2
                self._c = 2
                self._field[2][4].wLeft = True
                self._endPoint = (2,3)
                
            self._solve = """
if r.fr(): r.rt()
"""             
            
            self._task = 'Если справа нет стены, то сделать шаг вправо \n'
            self._task += 'Использовать r.fr() или r.isPark() \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-2':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()

            self._r = 2
            self._c = 2
            if rnd(2) == 1:
                self._field[2][2].wUp = True
                self._endPoint = (2,2)
            else:
                self._field[1][2].wUp = True
                self._endPoint = (1,2)

            self._solve = """
if r.fu(): r.up()
"""             

            self._task = 'Если сверху свободно, то сделать шаг вверх'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-3':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()

            self._r = 2
            self._c = 2
            rand = rnd(4)
            
            if rand == 1:
                self._field[2][2].wUp = False
                self._field[3][2].wUp = True
                self._field[2][2].wLeft = True
                self._field[2][3].wLeft = True
                self._endPoint = (1,2)
            elif rand ==2:
                self._field[2][2].wUp = True
                self._field[3][2].wUp = False
                self._field[2][2].wLeft = True
                self._field[2][3].wLeft = True
                self._endPoint = (3,2)
            elif rand ==3:
                self._field[2][2].wUp = True
                self._field[3][2].wUp = True
                self._field[2][2].wLeft = False
                self._field[2][3].wLeft = True
                self._endPoint = (2,1)
            elif rand ==0:
                self._field[2][2].wUp = True
                self._field[3][2].wUp = True
                self._field[2][2].wLeft = True
                self._field[2][3].wLeft = False
                self._endPoint = (2,3)

            self._solve = """
if r.fu(): r.up()
elif r.fd(): r.dn()
elif r.fr(): r.rt()
elif r.fl(): r.lt()
"""             

            self._task = 'С трех сторон стены. Выйти в свободную сторону'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-4':
            self._nc = 10
            self._nr = 10
            self._size = 30
                
            self.clear()

            self._r = 4
            self._c = 2
            if rnd(2): 
                self._field[3][2].wUp = True
                self._field[4][2].label = 'green'
            self._endPoint = (4,2)
            self._Nonelabel = True
            self._task = 'Если в клетке над роботом сверху стена, то закрасить текущую клетку \n'
            self._solve = """
if r.fu(): 
    r.up()
    if r.wu(): 
        r.dn()
        r.pt()
    else:
        r.dn()
"""
               
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-5':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 2
            rand = rnd(4)
            if rand == 1: 
                self._field[3][2].wUp = True
                self._field[6][2].wUp = True
                self._field[4][2].label = 'green'
            elif rand == 2:
                self._field[3][2].wUp = True
            elif rand == 3:
                self._field[6][2].wUp = True
            self._endPoint = (4,2)
            self._Nonelabel = True
            self._solve = """
w = True
r.up()
if r.fu(): w = False
r.dn()
if w:
    r.dn()
    if r.fd(): w = False
    r.up()
if w: r.pt()
"""

            self._task = 'Если в клетке над роботом сверху стена и в клетке под роботом снизу стена, \nто закрасить текущую клетку \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-6':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 2
            rand = rnd(4)
            if rand == 1: 
                self._field[3][2].wUp = True
                self._field[3][2].color = 'green'
                self._field[3][2].label = 'green'
            elif rand ==2 :
                self._field[3][2].wUp = True
            elif rand ==3 :
                self._field[3][2].color = 'green'
                self._field[3][2].label = 'green'
                self._field[4][2].label = 'green'
            elif rnd(2): 
                self._field[4][2].wUp = True
            self._endPoint = (4,2)
            self._Nonelabel = True
            self._solve = """
p = False
if r.fu(): 
    r.up()
    if r.fu() and r.color(): p = True
    r.dn()
    if p: r.pt()
"""         
            self._task = 'Если клетка сверху закрашена и над ней нет стены, \nто закрасить текущую клетку \n'
               
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-7':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 2
            rand = rnd(4)
            if rand == 1: 
                self._field[3][2].wUp = True
                if rnd(2):
                    self._field[3][2].color = 'blue'
                    self._field[3][2].label = 'blue'
                else:
                    self._field[3][2].color = 'red'
                    self._field[3][2].label = 'red'
                    self._field[4][2].label = 'green'
            elif rand ==2 :
                self._field[3][2].wUp = True
            elif rand ==3 :
                self._field[3][2].color = 'red'
                self._field[3][2].label = 'red'
            self._endPoint = (4,2)
            self._Nonelabel = True
            self._solve = """
p = False
r.up()
if r.wu() and r.color() =='red': p = True
r.dn()
if p: r.pt()
"""         

            self._task = 'Если клетка сверху закрашена красным и над ней стена, \nто закрасить текущую клетку \n'
               
        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task3-8':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 2
            rand = rnd(5)
            col = ''
            if rand == 1: 
                col = 'yellow'
            elif rand == 2:
                col = 'cyan'
            elif rand == 3:
                col = 'magenta'
            elif rand == 4:
                col = 'red'
            self._field[3][2].color = col
            self._field[3][2].label = col
            self._field[4][2].label = col
            self._endPoint = (4,2)
            self._Nonelabel = True
            self._solve = """
r.up()
col = r.color()
r.dn()
r.pt(col)  
"""


            self._task = 'Если клетка сверху закрашена, \nто закрасить текущую клетку тем же цветом\n'
           
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-9':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            r = 4
            c = 4
            self._r = r
            self._c = c
            if rnd(2): 
                self._field[r][c+1].color = 'green'
                self._field[r][c+1].label = 'green'

                self._field[r][c-1].color = 'green'
                self._field[r][c-1].label = 'green'

                self._field[r-1][c].color = 'green'
                self._field[r-1][c].label = 'green'
                
                self._field[r+1][c].color = 'green'
                self._field[r+1][c].label = 'green'
                
                self._field[r][c].label = 'green'
            else:
                if rnd(2):
                    self._field[r][c+1].color = 'green'
                    self._field[r][c+1].label = 'green'
                if rnd(2):
                    self._field[r][c-1].color = 'green'
                    self._field[r][c-1].label = 'green'
                if rnd(2):
                    self._field[r-1][c].color = 'green'
                    self._field[r-1][c].label = 'green'
                else:
                    self._field[r+1][c].color = 'green'
                    self._field[r+1][c].label = 'green'
            self._endPoint = (r,c)
            self._Nonelabel = True
            self._solve = """

r.rt()
if not r.color(): r.lt()
else:
    r.lt(2)
    if not r.color(): r.rt()
    else:
        r.rt()
        r.up()
        if not r.color(): r.dn()
        else:
            r.dn(2)
            if not r.color(): r.up()
            else: 
                r.up()
                r.pt()
"""

            self._task = 'Если в соседние клетки (с 4-х сторон) закрашены, \nто закрасить текущую клетку \n'
               
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task3-10':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            
            r = 4
            c = 4
            self._r = r
            self._c = c
            if rnd(2): 
                if rnd(2):
                    self._field[r][c+1].color = 'green'
                    self._field[r][c+1].label = 'green'
                else:
                    self._field[r][c+1].wLeft = True

                if rnd(2):
                    self._field[r][c-1].color = 'green'
                    self._field[r][c-1].label = 'green'
                else:
                    self._field[r][c].wLeft = True

                if rnd(2):
                    self._field[r-1][c].color = 'green'
                    self._field[r-1][c].label = 'green'
                else:
                    self._field[r][c].wUp = True
                    
                if rnd(2):
                    self._field[r+1][c].color = 'green'
                    self._field[r+1][c].label = 'green'
                else:
                    self._field[r+1][c].wUp = True
                
                self._field[r][c].label = 'green'
            else:
                rand = rnd(4)
                if rand == 0:
                    self._field[r][c+1].color = 'green'
                    self._field[r][c+1].label = 'green'
                    self._field[r][c+1].wLeft = True

                    self._field[r][c-1].color = 'green'
                    self._field[r][c-1].label = 'green'
                    self._field[r][c].wLeft = True
                    
                    self._field[r+1][c].color = 'green'
                    self._field[r+1][c].label = 'green'
                    
                elif rand == 1:
                    self._field[r][c+1].color = 'green'
                    self._field[r][c+1].label = 'green'
                    self._field[r][c+1].wLeft = True

                    self._field[r][c-1].color = 'green'
                    self._field[r][c-1].label = 'green'
                    
                    self._field[r+1][c].color = 'green'
                    self._field[r+1][c].label = 'green'
                    self._field[r+1][c].wUp = True

                elif rand == 2:
                    self._field[r][c+1].color = 'green'
                    self._field[r][c+1].label = 'green'

                    self._field[r][c-1].color = 'green'
                    self._field[r][c-1].label = 'green'
                    self._field[r][c].wLeft = True
                    
                    self._field[r+1][c].color = 'green'
                    self._field[r+1][c].label = 'green'
                    self._field[r+1][c].wUp = True

                elif rand == 3:
                    self._field[r-1][c].color = 'green'
                    self._field[r-1][c].label = 'green'

                    self._field[r][c-1].color = 'green'
                    self._field[r][c-1].label = 'green'
                    
                    self._field[r+1][c].color = 'green'
                    self._field[r+1][c].label = 'green'
                    self._field[r+1][c].wUp = True
            self._endPoint = (r,c)
            self._Nonelabel = True
            self._solve = """

p = True
if r.fr(): 
    r.rt()
    if not r.color(): p = False
    r.lt()
if p and r.fl():
    r.lt()
    if not r.color(): p = False
    r.rt()
if p and r.fu():
    r.up()
    if not r.color(): p = False
    r.dn()
if p and r.fd():
    r.dn()
    if not r.color(): p = False
    r.up()
if p: r.pt()

"""

            self._task = 'Если все соседние клетки, в которые можно попасть, закрашены, \nто закрасить текущую клетку \n'
            self._task += 'След. задача: task4-1'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-1':
            self._nc = 35
            self._nr = 15
            self._size = 25
            self.clear()

            self._r = 2
            self._c = 1
            self._endPoint = (2,30)
            
            for c in range(2,30):
                self._field[2][c].label = 'green'

            self._Nonelabel = True
            self._solve = """
r.rt()
for x in range(28):
    r.pt()
    r.rt()
"""
            self._task = 'Закрасить клетки \n'
            self._task += 'Использовать цикл for: \n'
            self._task += '... \n'
            self._task += 'for z in range(1,29): \n'
            self._task += '    r.pt() \n'
            self._task += '    r.rt() \n'
            self._task += '... \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-2':
            self._nc = 30
            self._nr = 20
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 1
            self._endPoint = (5,2)
            for c in range(2,29):
                self._field[2][c].label = 'green'
                self._field[3][c].label = 'green'
                self._field[4][c].label = 'green'
            self._Nonelabel = True
            self._solve = """
r.sleep = 0
r.rt()
for z in range(3):
    for x in range(27):
        r.pt()
        r.rt()
    r.lt(27)
    r.dn()
"""

            self.sleep = 0.05
            self._task = 'Закрасить клетки. '
            self._task += 'Использовать цикл for  \n'
            self._task += 'Придумать два способа решения\n'
            self._task += 'Для ускорения можно изменить задержку \nr.sleep = 0.01 \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-3':
            self._nc = 30
            self._nr = 16
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            for c in range(2,29):
                for r in range (2,14):
                    self._field[r][c].label = 'green'
            self._Nonelabel = True
            self._solve = """
r.sleep = 0
r.rt()
for z in range(12):
    for x in range(27):
        r.pt()
        r.rt()
    r.lt(27)
    r.dn()
"""

            self.sleep = 0.01
            self._task = 'Закрасить клетки'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-4':
            self._nc = 30
            self._nr = 16
            self._size = 30
            self._field = []
            self.clear()
            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            for c in range(2,29):
                for r in range (2,14):
                    cr = rnd(1,255,10)
                    cg = rnd(1,255,10)
                    cb = rnd(1,255,10)
                    self._field[r][c].label = "#%02X%02X%02X" %(cr,cg,cb)
            self._solve = """
r.sleep = 0
r.rt()
for z in range(12):
    for x in range(27):
        r.pt(r.label())
        r.rt()
    r.lt(27)
    r.dn()
"""

            self._task = 'Закрасить клетки указанными цветам \n'
            self._task += 'r.paint(r.label()) \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-5':
            self._nc = 30
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            
            self._solve = """
r.sleep = 0
r.rt()
for z in range(12):
    for x in range(27):
        r.pt(r.randcolor())
        r.rt()
    r.lt(27)
    r.dn()
"""


            self._task = 'Закрасить клетки случайными цветам \n'
            self._task += 'r.pt(r.randcolor())\n'
            self._test = '''
p = l = True
r = c = 1
cc = 0
colors = set()
while  (r <= self._nr) and (c <= self._nc):
    colors.add(self._field[r][c].color)
    if (c < self._nc):
        c +=1
    else:
        c = 1
        r += 1
if self._endPoint != self.getCoords():
    p = False
if len(colors) < 30: l = False
'''
      
        ##-----------------------------------------------------------
        elif mn == 'task4-6':
            self._nc = 30
            self._nr = 16
            self._size = 30

            self.clear()

            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            self._solve = """
r.sleep = 0
r.rt()
for z in range(12):
    col = r.randcolor()
    for x in range(27):
        r.pt(col)
        r.rt()
    r.lt(27)
    r.dn()       
"""

            self._task = 'Закрасить клетки случайными цветами по строкам\n'
            self._task += 'Каждая строка - одним (любым, случайным) цветом\n'
            self._test = '''
p = l = True
r = c = 1
line_colors = set()
for r in range(2,self._nr):
    line_colors.add(self._field[r][3].color)
    colors = set()
    for c in range(self._nc):
        colors.add(self._field[r][c].color)
    if (len(colors) > 2): l = False
if (len(line_colors) < 5): l = False
    
if self._endPoint != self.getCoords():
    p = False
'''

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-7':
            self._nc = 30
            self._nr = 16
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 1
            self._endPoint = (2,29)
            self._solve = """
r.sleep = 0
r.rt()
for z in range(27):
    col = r.randcolor()
    for x in range(12):
        r.pt(col)
        r.dn()
    r.up(12)
    r.rt()       
"""
            self._task = 'Закрасить клетки случайными цветами по столбцам\n'
            self._task += 'Каждый столбец - одним (любым) цветом'
            self._test = '''
p = l = True
r = c = 1
column_colors = set()
for c in range(2,self._nc):
    column_colors.add(self._field[3][c].color)
    colors = set()
    for r in range(self._nr):
        colors.add(self._field[r][c].color)
    if (len(colors) > 2): l = False
if (len(column_colors) < 5): l = False
    
if self._endPoint != self.getCoords():
    p = False
'''
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-8':
            self._nc = 30
            self._nr = 16
            self._size = 30

            self.clear()

            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            
            for row in range(2,14):
                for column in range (2,29):
                    cr = 0
                    cg = 0
                    cb = (column-2)*(255/28)
                    self._field[row][column].label = "#%02X%02X%02X" %(cr,cg,cb)

            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            self._solve = """
r.sleep = 0
r.rt()
for row in range(12):
    for column in range(27):
        cr = 0
        cg = 0
        cb = column*(255/28)
        r.pt("#%02X%02X%02X" %(cr,cg,cb))
        r.rt()
    r.lt(27)
    r.dn()       
"""

            self._task = '(необязательно)Закрасить клетки цветом, плавно переходящим из черного в синий \n'
            self._task += 'Использовать цикл for.  \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-9':
            self._nc = 30
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            
            for row in range(2,14):
                for column in range (2,29):
                    cr = 255 - (column-2)*(255/28)
                    cg = 255 - (column-2)*(255/28)
                    cb = 255
                    self._field[row][column].label = "#%02X%02X%02X" %(cr,cg,cb)

            self._solve = """
r.sleep = 0
r.rt()
for row in range(12):
    for column in range(27):
        cr = 255 - column*(255/28)
        cg = 255 - column*(255/28)
        cb = 255
        r.pt("#%02X%02X%02X" %(cr,cg,cb))
        r.rt()
    r.lt(27)
    r.dn()       
"""

            self._task = '(необязательно)Закрасить клетки цветом, плавно переходящим из белого в синий \n'
            self._task += 'Использовать цикл for.  \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-10':
            self._nc = 30
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 2
            self._c = 1
            self._endPoint = (14,2)
            
            for c in range(2,29):
                for r in range (2,14):
                    cr = 255 - (c-2)*(255/28)
                    cg = (r-2)*(255/13)
                    cb = (c-2)*(255/28)
                    self._field[r][c].label = "#%02X%02X%02X" %(cr,cg,cb)
            self._solve = """
r.sleep = 0
r.rt()
for row in range(12):
    for column in range(27):
        cr = 255 - column*(255/28)
        cg = row*(255/13)
        cb = column*(255/28)
        r.pt("#%02X%02X%02X" %(cr,cg,cb))
        r.rt()
    r.lt(27)
    r.dn()       
"""
            self._task = '(необязательно)Закрасить клетки цветом, плавно переходящим одного в другой \n'
            self._task += 'Использовать цикл for.  \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-11':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 1
            self._c = 1
            self._endPoint = (15,2)
            
            for r in range (2,15):
                for c in range(2,r+1):
                    self._field[r][c].label = 'red'
            self._solve = """
r.sleep = 0
r.rt()
for row in range(1,15): 
    for column in range(1,row):
        r.pt('red')
        r.rt()
    r.lt(row-1)
    r.dn()
"""


            self._task = 'Закрасить клетки \n'
            self._task += 'Использовать цикл for. \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-12':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 1
            self._c = 1
            self._endPoint = (15,15)
            
            for r in range (2,15):
                for c in range(r+1,15):
                    self._field[r][c].label = 'red'
            self._solve = """
r.sleep = 0
r.rt()
r.dn()
for row in range(1,14): 
    r.rt()
    for column in range(1,14-row):
        r.pt('red')
        r.rt()
    r.lt(14-row-1)
    r.dn()
"""

            self._task = 'Закрасить клетки \n'
            self._task += 'Использовать цикл for. \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-13':
            self._nc = 20
            self._nr = 16
            self._size = 30

            self.clear()

            self._r = 1
            self._c = 1
            self._endPoint = (15,14)
            self._solve = """
r.sleep = 0
r.rt(13)
for row in range(1,15): 
    for column in range(1,row):
        r.pt('red')
        r.lt()
    r.rt(row-1)
    r.dn()
"""
            
            for r in range (2,15):
                for c in range(16-r,15):
                    self._field[r][c].label = 'red'


            self._task = 'Закрасить клетки \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-14':
            self._nc = 20
            self._nr = 20
            self._size = 30
            self.clear()

            self._r = 1
            self._c = 1
            self._endPoint = (1,1)
            
            for c in range (1,self._nc,2):
                for r in range(1,self._nr,2):
                    self._field[r][c].label = 'green'
            self._solve = """
r.sleep = 0
def line():
    for col in range(9):
        r.pt()
        r.rt(2)
    r.pt()
    r.lt(18)

for row in range(9):
    line()
    r.dn(2)
line()           
r.up(18)
"""

            self._task = 'Закрасить клетки \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-15':
            self._nc = 20
            self._nr = 20
            self._size = 30
            self.clear()

            self._r = 1
            self._c = 1
            self._endPoint = (1,1)
            bb = True
            for c in range (1,self._nc):
                for r in range(1,self._nr):
                    if bb:
                        self._field[r][c].label = 'green'
                    bb = not bb
            self._solve = """
r.sleep = 0
def line():
    for col in range(9):
        r.pt()
        r.rt(2)
    r.pt()
    r.lt(18)

def line2():
    r.rt()
    for col in range(8):
        r.pt()
        r.rt(2)
    r.pt()
    r.lt(17)

for row in range(9):
    line()
    r.dn()
    line2()
    r.dn()
line()           
r.up(18)
"""
            self._task = 'Закрасить клетки\n'
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task4-16':
            self._nc = 25
            self._nr = 15
            self._r = 1
            self._c = 1
            self._size = 20

            self.clear()

            c = r = 2
            for rcount in range(0,3):
                for ccount in range(0,6):
                    self._field[r+rcount][c+ccount].label = 'green'
            c = 2
            r = 8
            for rcount in range(0,6):
                for ccount in range(0,4):
                    self._field[r+rcount][c+ccount].label = 'green'
            c = 10
            r = 2
            for rcount in range(0,4):
                for ccount in range(0,9):
                    self._field[r+rcount][c+ccount].label = 'green'
            c = 10
            r = 8
            for rcount in range(0,6):
                for ccount in range(0,6):
                    self._field[r+rcount][c+ccount].label = 'green'

            c = 20
            r = 2
            for rcount in range(0,12):
                for ccount in range(0,4):
                    self._field[r+rcount][c+ccount].label = 'green'
            
            self._endPoint = (1,1)
            self._Nonelabel = True
            self._solve = """
r.sleep = 0.01
def sq(nr=3,nc=3):
    for rr in range(nr):
        for cc in range(nc):
            r.pt()
            r.rt()
        r.lt(nc)
        r.dn()
    r.up(nr)
r.rt()
r.dn()    
sq(3,6)
r.dn(6)
sq(6,4)
r.rt(8)
sq(6,6)
r.up(6)
sq(4,9)
r.rt(10)
sq(12,4)
r.lt(19)
r.up()
"""   

            self._task = 'Закрасить\n'
            self._task += 'Размер и расположение прямоугольников не меняется \n'
            self._task += 'Использовать процедуру с параметром \n'
            self._task += 'След. задача: task5-1'            

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-1':
            self._nc = 20
            self._nr = 15
            self._size = 30
            self.clear()

            self._r = 1
            self._c = 9
            rr = rnd(5,14)
            self._endPoint = (rr,9)
            for c in range(1,10):
                self._field[rr+1][c+4].wUp = True
            self._solve = """
while r.fd():
    r.dn()
"""
            
            self._task = 'Дойти до стены. Расстояние неизвестно \n'
            self._task += 'while r.fd():\n'
            self._task += '    r.dn()'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-2':
            self._nc = 20
            self._nr = 14
            self._size = 30
            self.clear()

            self._r = 3
            self._c = 2
            cr = rnd(5,18)
            self._endPoint = (3,cr)
            for c in range(2,cr):
                self._field[4][c].wUp = True
            self._solve = """

while r.wd(): r.rt()
"""
            
            self._task = 'Дойти до конца стены. Расстояние неизвестно \n'
            self._task += 'Использовать цикл while. \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-3':
            self._nc = 20
            self._nr = 14
            self._size = 30
            self.clear()

            self._r = 3
            self._c = 3
            cr = rnd(6,18)
            self._endPoint = (3,cr)
            for c in range(4+rnd(3),cr):
                self._field[4][c].wUp = True
            self._solve = """

while r.fd(): r.rt()
while r.wd(): r.rt()
"""            
            self._task = 'Дойти до конца стены. Расстояние неизвестно \n'
            self._task += 'Использовать цикл while. \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-4':
            self._nc = 20
            self._nr = 18
            self._size = 30
            self.clear()

            self._r = 1
            self._c = 1
            cr = rnd(3,15)
            rr = rnd(6,15)
            self._endPoint = (rr,1)
            for c in range(1,cr):
                self._field[rr][c].wUp = True
            self._solve = """

while r.fd(): r.dn()
while r.wd(): r.rt()
r.dn()
while r.fl(): r.lt()
"""             
            self._task = 'Обойти стену. Размеры стены и расстояние до нее неизвестны. Стена одна \n'
            self._task += 'Использовать цикл while. \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-5':
            self._nc = 20
            self._nr = 17
            self._size = 30
            self.clear()

            self._r = 1
            dc = rnd(2,4)
            self._c = 10 
            rr = rnd(4,12)
            self._endPoint = (rr,10-dc-1)
            for c in range(10-dc,10+dc):
                self._field[rr][c].wUp = True
            self._solve = """

while r.fd(): r.dn()
while r.wd(): r.rt()
r.dn()
r.lt()
while r.wu(): r.lt()
"""             
            
            self._task = 'Обойти стену. Расстояние и размеры стены неизвестны. Стена одна \n'
            self._task += 'Использовать цикл while. \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-6':
            self._nc = 20
            self._nr = 15
            self._size = 30
            self.clear()

            self._r = 4
            self._c = 4
            dc = rnd(6,16)
            self._endPoint = (4,dc+4)
            for c in range(0,dc):
                if rnd(0,2) == 1:
                    self._field[4][4+c].wUp = True
                self._field[4+1][4+c].wUp = True
            self._solve = """
while r.wd(): r.rt()
"""             
            self._task = 'Выйти из коридора. Размеры стен неизвестны. В стене сверху есть проемы \n'
            self._task += 'Использовать цикл while. \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-7':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 4
            self._c = 4
            dc = rnd(6,16)
            self._endPoint = (4,dc+4)
            for c in range(0,dc):
                if rnd(0,2) == 1:
                    self._field[4][4+c].wUp = True
                else:
                    self._field[4+1][4+c].wUp = True
            self._solve = """
while r.wd() or r.wu(): r.rt()
"""            
            self._task = 'Выйти из коридора. Есть проемы сверху или снизу\n'
            self._task += 'Использовать цикл while.'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-8':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 4
            self._c = 4
            dc = rnd(6,16)
            self._endPoint = (4,dc+4)
            for c in range(dc):
                self._field[4][4+c].color = self._field[4][4+c].label = 'yellow'

            self._solve = """
while r.color(): r.rt()
"""            
            self._task = 'Дойти до конца закрашенного ряда\n'
            self._task += 'Использовать цикл while. \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-9':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 4
            self._c = 4
            dc = rnd(8,16)
            dr = rnd(8,10)
            self._endPoint = (dr+4,dc+4)
            for c in range(dc):
                for r in range(dr):
                    self._field[4+r][4+c].color = self._field[4+r][4+c].label = 'yellow'

            self._solve = """
while r.color(): r.rt()
r.lt()
while r.color(): r.dn()
r.rt()
"""            
            self._task = 'Дойти до правого нижнего угла закрашенного прямоугольника\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-10':
            self._nc = 5+rnd(8)
            self._nr = 5+rnd(8)
            self._size = 25
            self.clear()

            self._r = 1
            self._c = 1
            self._endPoint = (self._nr-1,1)
            self.sleep = 0.01

            for r in range(1,self._nr):
                for c in range(1,self._nc):
                    self._field[r][c].label = 'green'

            self._solve = """
while r.fd():
    while r.fr():
        r.pt()
        r.rt()
    r.pt()
    while r.fl(): r.lt()
    r.dn()
while r.fr():
    r.pt()
    r.rt()
r.pt()
while r.fl(): r.lt()
"""            
            self._task = 'Закрасить всё поле\nРазмеры поля неизвестны'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-11':
            self._nc = 15
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 8
            self._c = 3

            r1 = rnd(2,5)
            c1 = rnd(self._c+1,self._c+5)
            c2 = rnd(c1+1,self._nc-2)

            r = self._r
            c = c1
            self._field[r][c].color = self._field[r][c].label =  'green'
            r = c1
            self._field[r][c].color = self._field[r][c].label =  'green'
            c = c2
            self._field[r][c].color = self._field[r][c].label =  'green'
            self._endPoint = (r,c)
            self._solve = """
while not r.color(): r.rt()
r.up()
while not r.color(): r.up()
r.rt()
while not r.color(): r.rt()
"""
            self.sleep = 0.1
            self._task = 'Дойти до третьей закрашенной клетки (вправо, вверх, вправо)\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-12':
            self._nc = 15
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 8
            self._c = 3
            for x in range(1,4+rnd(7)):
                self._field[self._r][self._c+x].wLeft = True
                self._endPoint = (self._r,self._c+x)
            self._solve = """
while r.wr():
    r.up()
    r.rt()
    r.dn()
"""
            self.sleep = 0.04
            self._task = 'Дойти до конца забора\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-13':
            self._nc = 15
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 8
            self._c = 3
            for x in range(1,4+rnd(7),2):
                self._field[self._r][self._c+x].wLeft = True
                self._endPoint = (self._r,self._c+x)
            self._solve = """
while r.wr():
    r.up()
    r.rt()
    r.rt()
    r.dn()
r.lt()
"""
            self.sleep = 0.04
            self._task = 'Дойти до конца забора\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task5-14':
            self._nc = 15
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 6
            self._c = 3
            for x in range(1,6+rnd(4)):
                for y in range(1+rnd(4)):
                    self._field[self._r-y][self._c+x].wLeft = True
                self._endPoint = (self._r,self._c+x)
            self._solve = """
while r.wr():
    while r.wr(): r.up()
    r.rt()
    r.dn()
    while r.wl(): r.dn()
    r.up()
"""
            self.sleep = 0.04
            self._task = 'Дойти до конца забора\n'
            self._task += 'След. задача task6-1'

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-1':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            self._r = 4
            self._c = 3
            dc = rnd(6,16)
            self._endPoint = (4,3)
            for c in range(0,dc):
                    self._field[4][4+c].wUp = True
                    self._field[4+1][4+c].wUp = True
                    self._field[4][4+c].label = 'green'
            self._field[4][4+dc].wLeft = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.wd(): 
    r.pt()
    r.lt()

"""
            self._Nonelabel = True
            self._task = 'Закрасить коридор и вернуться\n'
            self._task += 'r.label() в этой и других задачах группы 6- не использовать'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-2':
            self._nc = 20
            self._nr = 16
            self._size = 30
            self.clear()

            dc = rnd(6,16)
            self._r = 4
            self._c = 3 + int(dc/2)
            self._endPoint = (4,4)
            for c in range(0,dc):
                    self._field[4][4+c].wUp = True
                    self._field[4+1][4+c].wUp = True
                    self._field[4][4+c].label = 'green'
            self._field[4][4+dc].wLeft = True
            self._field[4][4].wLeft = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.fl(): 
    r.pt()
    r.lt()
r.pt()
"""                    
            self._Nonelabel = True
            self._task = 'Закрасить коридор\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-3':
            self._nc = 20
            self._nr = 18
            self._size = 25
            self.clear()

            dup = rnd(2,8)
            ddown = rnd(2,8)
            dleft = rnd(2,8)
            dright = rnd(2,8)
            self._r = 9
            self._c = 9
            self._endPoint = (9,9)
            for c in range(9-dleft,9+dright):
                    self._field[9][c].wUp = True
                    self._field[9+1][c].wUp = True
                    self._field[9][c].label = 'green'
            for r in range(9-dup,9+ddown):
                    self._field[r][9].wLeft = True
                    self._field[r][9+1].wLeft = True
                    self._field[r][9].label = 'green'
                    
            self._field[9][9+dright].wLeft = True
            self._field[9][9-dleft].wLeft = True
            self._field[9-dup][9].wUp = True
            self._field[9+ddown][9].wUp = True
            self._field[9][9].wUp = False
            self._field[9][9].wLeft = False
            self._field[9+1][9].wUp = False
            self._field[9][9+1].wLeft = False
            self._field[9][9].label = ''
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.fl(): 
    if r.wd(): r.pt()
    r.lt()
r.pt()
while r.wd(): r.rt()
while r.fd(): r.dn()
r.pt()
while r.fu():
    r.up()
    if r.wr(): r.pt()
while r.wr(): r.dn()
"""                    
                    
            self._Nonelabel = True
            
            self._task = 'Закрасить коридоры и вернуться\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-4':
            self._nc = 20
            self._nr = 18
            self._size = 25
            self.clear()

            dright = rnd(8,17)
            self._r = 9
            self._c = 2
            self._endPoint = (9,2)

            def kor(cr,cc, way = 'up', length =1):
                if way == 'up':
                    for r in range(1,1+length):
                        self._field[cr-r][cc].wLeft = True
                        self._field[cr-r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr-r][c].wUp = True
                if way == 'down':
                    for r in range(1,1+length):
                        self._field[cr+r][cc].wLeft = True
                        self._field[cr+r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr+r][c].wUp = True


            for c in range(3,2+dright):
                self._field[9+1][c].wUp = True
                if rnd(1,4) != 2:
                    self._field[9][c].wUp = True
                else:
                    kor(9,c,length=1)
                    
            self._field[9][2+dright].wLeft = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.wd(): 
    if r.fu(): 
        r.up()
        r.pt()
        r.dn()
    r.lt()
"""  
            self._Nonelabel = True
            
            self._task = 'Закрасить коридоры по одной клетке и вернуться\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-5':
            self._nc = 20
            self._nr = 18
            self._size = 25
            self.clear()

            dright = rnd(8,17)
            self._r = 9
            self._c = 2
            self._endPoint = (9,2)

            def kor(cr,cc, way = 'up', length =1):
                if way == 'up':
                    for r in range(1,1+length):
                        self._field[cr-r][cc].wLeft = True
                        self._field[cr-r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr-r][c].wUp = True
                if way == 'down':
                    for r in range(1,1+length):
                        self._field[cr+r][cc].wLeft = True
                        self._field[cr+r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr+r][c].wUp = True


            for c in range(3,2+dright):
                self._field[9+1][c].wUp = True
                if rnd(1,4) != 2:
                    self._field[9][c].wUp = True
                else:
                    kor(9,c,length=3)
                    
            self._field[9][2+dright].wLeft = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.wd(): 
    if r.fu(): 
        r.up(3)
        for x in range(3):
            r.pt()
            r.dn()
    r.lt()
"""  
            self._Nonelabel = True
            
            self._task = 'Закрасить коридоры по три клетки и вернуться\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-6':
            self._nc = 20
            self._nr = 18
            self._size = 25
            self.clear()

            dright = rnd(8,17)
            self._r = 9
            self._c = 2
            self._endPoint = (9,2)

            def kor(cr,cc, way = 'up', length =1):
                if way == 'up':
                    for r in range(1,1+length):
                        self._field[cr-r][cc].wLeft = True
                        self._field[cr-r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr-r][c].wUp = True
                if way == 'down':
                    for r in range(1,1+length):
                        self._field[cr+r][cc].wLeft = True
                        self._field[cr+r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr+r][c].wUp = True


            for c in range(3,2+dright):
                self._field[9+1][c].wUp = True
                if rnd(1,4) != 2:
                    self._field[9][c].wUp = True
                else:
                    kor(9,c,length=rnd(2,6))
                    
            self._field[9][2+dright].wLeft = True

            self._Nonelabel = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.wd(): 
    if r.fu(): 
        while r.fu(): r.up()
        while r.fd():
            r.pt()
            r.dn()
    r.lt()
"""              
            self._task = 'Закрасить коридоры (длина неизвестна) и вернуться\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-7':
            self._nc = 20
            self._nr = 18
            self._size = 25
            self.clear()

            dright = rnd(8,17)
            self._r = 9
            self._c = 2
            self._endPoint = (9,2)

            def kor(cr,cc, way = 'up', length =1):
                if way == 'up':
                    for r in range(1,1+length):
                        self._field[cr-r][cc].wLeft = True
                        self._field[cr-r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr-r][c].wUp = True
                if way == 'down':
                    for r in range(1,1+length):
                        self._field[cr+r][cc].wLeft = True
                        self._field[cr+r][cc+1].wLeft = True
                        self._field[cr+r][cc].label = 'green'
                    self._field[cr+r+1][c].wUp = True


            for c in range(3,2+dright):
                rand = rnd(1,4)
                if rand == 1:
                    self._field[9][c].wUp = True
                    self._field[9+1][c].wUp = True
                elif rand == 2:
                    kor(9,c,way = 'down', length=rnd(2,6))
                    self._field[9][c].wUp = True
                else:
                    kor(9,c,length=rnd(2,6))
                    self._field[9+1][c].wUp = True
                    
            self._field[9][2+dright].wLeft = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while r.wd() or r.wu(): 
    if r.fu(): 
        while r.fu(): r.up()
        while r.fd():
            r.pt()
            r.dn()
    if r.fd(): 
        while r.fd(): r.dn()
        while r.fu():
            r.pt()
            r.up()
    r.lt()
"""              
   
            self._Nonelabel = True
            
            self._task = 'Закрасить коридоры (длина неизвестна) и вернуться\n Коридоры либо вверх, либо вниз'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task6-8':
            self._nc = 20
            self._nr = 20
            self._size = 25
            self.clear()

            dright = rnd(8,17)
            self._r = 9
            self._c = 2
            self._endPoint = (9,2)

            def kor(cr,cc, way = 'up', length =1):
                if way == 'up':
                    for r in range(1,1+length):
                        self._field[cr-r][cc].wLeft = True
                        self._field[cr-r][cc+1].wLeft = True
                        self._field[cr-r][cc].label = 'green'
                    self._field[cr-r][c].wUp = True
                if way == 'down':
                    for r in range(1,1+length):
                        self._field[cr+r][cc].wLeft = True
                        self._field[cr+r][cc+1].wLeft = True
                        self._field[cr+r][cc].label = 'green'
                    self._field[cr+r+1][c].wUp = True


            for c in range(3,2+dright):
                rand = rnd(1,6)
                if rand <= 2:
                    self._field[9][c].wUp = True
                    self._field[9+1][c].wUp = True
                elif rand == 3:
                    kor(9,c,way = 'down', length=rnd(2,6))
                    self._field[9][c].wUp = True
                elif rand == 4:
                    kor(9,c,length=rnd(2,6))
                    self._field[9+1][c].wUp = True
                elif rand == 5:
                    kor(9,c,way = 'down', length=rnd(2,6))
                    kor(9,c,length=rnd(2,6))
                    
            self._field[9][2+dright].wLeft = True
            self.sleep = 0.04
            self._solve = """
while r.fr(): r.rt()
while not r.isPark(): 
    if r.fu(): 
        while r.fu(): r.up()
        while r.wl():
            r.pt()
            r.dn()
    if r.fd(): 
        while r.fd(): r.dn()
        while r.wl():
            r.pt()
            r.up()
    r.lt()
"""  
            self._Nonelabel = True
            
            self._task = 'Закрасить коридоры (длина неизвестна) и вернуться\n Коридоры могут вверх и вниз одновременно \n'
            self._task += 'След. задача: task7-0'

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-0':
            self._nc = 20
            self._nr = 15
            self._size = 28
            self.clear()

            dright = rnd(2,7)
            ddown =  rnd(8,10)
            self._r = 2
            self._c = 10
            self._endPoint = (self._r,self._c)

            for c in range (self._c-dright,self._c+dright):
                self._field[self._r + ddown][c].wUp = True
            self._field[self._r + ddown-1][self._c].label = 'green'
            self.sleep = 0.04
            self._solve = """
global stepD
sp = " "
def stepD(sp):
    r.dn()
    print sp + "r.dn()"
    if r.fd(): 
        print sp + u"stepD вход"
        sp += "    "
        stepD(sp)
        sp = sp[:-4]
        print sp + u"stepD выход"
    else: 
        print sp + "r.pt()"
        r.pt()
    print sp + "r.up()"
    r.up()

stepD(sp)
"""
            
            self._task = 'Дойти до стены, закрасить и вернуться (расстояние неизвестно). \nИспользовать рекурсивную процедуру \n'
            self._task += """
def stepD():
    r.dn()
    if r.fd(): 
        stepD(sp)
    else: 
        r.pt()
    r.up()
stepD()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-1':
            self._nc = 20
            self._nr = 15
            self._size = 28
            self.clear()

            dright = rnd(2,7)
            ddown =  rnd(8,10)
            self._r = 2
            self._c = 10
            self._endPoint = (self._r+ddown-1,self._c)

            for c in range (self._c-dright,self._c+dright):
                self._field[self._r + ddown][c].wUp = True
            self.sleep = 0.04
            self._solve = """
a = 0
while r.fd():
    r.dn()
    a = a + 1
    r.settext(a)

"""
            
            self._task = 'Дойти до стены (расстояние неизвестно). В каждую клетку вписать номер шага \n'
            self._task += self._solve

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-2':
            self._nc = 20
            self._nr = 18
            self._size = 28
            self.clear()

            dright = rnd(2,7)
            ddown =  rnd(8,10)
            self._r = 2
            self._c = 10
            self._endPoint = (self._r,self._c)

            for c in range (self._c-dright,self._c+dright):
                self._field[self._r + ddown][c].wUp = True
            self._field[self._r + ddown-1][self._c].label = 'green'
            self.sleep = 0.04
            self._NoneisPark = True
            self._solve = """
            
a = 0
while r.fd():
    r.dn()
    a = a + 1
r.pt()
r.up(a)
"""            
            self._task = 'Расстояние до стены неизвестно.\nДойти до стены и вернуться в ту же точку \n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-3':
            self._nc = 20
            self._nr = 18
            self._size = 30
            self.clear()

            dright = rnd(2,7)
            ddown =  rnd(5,8)
            self._r = 2
            self._c = 10
            self._endPoint = (self._r+ddown*2-1,self._c)
            
            self.sleep = 0.1
            self._NoneisPark = True
            self._solve = """
            
a = 0
while r.fd():
    r.dn()
    a = a + 1
b = 0
while r.wd():
    r.rt()
    b = b + 1
r.dn(a+1)
r.lt(b)
"""            
      
            for c in range (self._c-dright,self._c+dright):
                self._field[self._r + ddown][c].wUp = True
            
            self._task = 'Расстояние до стены неизвестно.\nОбойти до стены и остановиться на таком же расстоянии от стены\n'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-4':
            self._nc = 11
            self._nr = 10
            self._size = 30
            self.clear()

            self._r = 2+rnd(6)
            self._c = 2+rnd(6)
            self.sleep = 0.01
            self._NoneisPark = True

            if abs(self._c) < 6:
                self._endPoint = (self._r,1)
            else:
                self._endPoint = (self._r,self._nc-1)

            self._solve = """
a = 0
while r.fr(): 
    r.rt()
    a += 1
b = -a
while r.fl():
    r.lt()
    b = b + 1
if b > a:
    while r.fr(): r.rt()
"""            
            self._task = 'Переместиться к ближайшей стене'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-5':
            self._nc = 20 + rnd(25)
            self._nr = 6
            self._size = 22
            self.clear()
            self._r = 3

            self._c = 1
            self.sleep = 0.01
            self._NoneisPark = True
            n = 1
            d = 1
            for c in range(1,self._nc-1):
                if d == n:
                    self._field[self._r][c].label = 'green'
                    n += 1
                    d = 1
                d += 1

            self._endPoint = (self._r,self._nc-1)

            self._Nonelabel = True
            self._solve = """
n = 1
d = 1
while r.fr(): 
    if d == n:
        r.pt()
        n += 1
        d = 1
    d += 1
    r.rt()
"""            
            self._task = 'Закрасить клетки (интервал увеличивается)'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-6':
            self._nc = 20 + rnd(25)
            self._nr = 6
            self._size = 22
            self.clear()
            self._r = 3

            self._c = 1
            self.sleep = 0.1
            d = 0
            for c in range(2,self._nc):
                if rnd(2):
                    self._field[self._r][c].label = 'green'
                    self._field[self._r][c].color = 'green'
                    d += 1
                    if d == 5: self._endPoint = (self._r,c)

            self._Nonelabel = True
            self._NoneisPark = True
            self._solve = """
d = 0
while d < 5: 
    if r.color(): 
        d+= 1
    r.rt()
r.lt()
"""            
            self._task = 'Остановится на 5-й закрашенной клетке'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task7-7':
            self._nc = 35
            self._nr = 6
            self._size = 24
            self.clear()
            self._r = 3

            self._c = 1
            self.sleep = 0.1
            d = 0
            for c in range(2,self._nc):
                if rnd(3):
                    self._field[self._r][c].label = 'green'
                    self._field[self._r][c].color = 'green'
                    d += 1
                    if d == 3: 
                        self._endPoint = (self._r,c)
                        d += 1
                else:
                    if d < 3: d = 0
            if d < 3: 
                self._endPoint = (self._r,self._nc-1)

            self._NoneisPark = True
            self._Nonelabel = True
            self._solve = """
d = 0
while (d < 3) and r.fr(): 
    if r.color(): d+= 1
    else: d = 0
    r.rt()
if d == 3:r.lt()
"""            
            self._task = 'Остановится на 3-й подряд закрашенной клетке\n'
            self._task += 'Если нет 3-х подряд закрашенных клеток, то у правой стены\n'
            self._task += 'Следующая задача: task8-1'

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-1':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,35):
                self._field[self._r][c].wUp = True
                self._field[self._r+1][c].wUp = True
                if rnd(2):
                    self._field[self._r+1][c].wUp = False
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fd(): r.pt()
    r.rt()           
if r.fd(): r.pt()     
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-2':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,35):
                self._field[self._r][c].wUp = True
                self._field[self._r+1][c].wUp = True
                if rnd(2):
                    self._field[self._r][c].wUp = False
                    self._field[self._r][c].label = 'green'
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu(): r.pt()
    r.rt()           
if r.fu(): r.pt()     
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-3':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,35):
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                    self._field[self._r][c].label = 'green'
                if rnd(2):
                    self._field[self._r][c].wUp = True
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
w = 1
while r.fr() or w <= 2:
    if r.wu() or r.wd(): r.pt()
    if r.fr(): 
        r.rt()
    else:
        w += 1
        

"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task8-4':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                if rnd(2):
                    self._field[self._r][c].wUp = True
                if self._field[self._r][c].wUp and self._field[self._r+1][c].wUp:
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.wu() and r.wd(): r.pt()
    r.rt()           

"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task8-5':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if not rnd(3):
                    self._field[self._r+1][c].wUp = True
                if not rnd(2):
                    self._field[self._r][c].wUp = True
                if not self._field[self._r][c].wUp and not self._field[self._r+1][c].wUp:
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu() and r.fd(): r.pt()
    r.rt()           
"""
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-6':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if not rnd(3):
                    self._field[self._r+1][c].wUp = True
                if not rnd(3):
                    self._field[self._r][c].wUp = True
                if not self._field[self._r][c].wUp and self._field[self._r+1][c].wUp:
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu() and r.wd(): r.pt()
    r.rt()           
"""
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-7':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if not rnd(3):
                    self._field[self._r+1][c].wUp = True
                if not rnd(3):
                    self._field[self._r][c].wUp = True
                if not self._field[self._r][c].wUp or not self._field[self._r+1][c].wUp:
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if not (r.wd() and r.wu()): r.pt()
    r.rt()           
"""
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-8':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if rnd(2):
                    self._field[self._r][c].color = 'green'
                    self._field[self._r][c].label = 'green'
                if rnd(2):
                    self._field[self._r][c].wUp = True
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                if self._field[self._r][c].color and  not self._field[self._r][c].wUp:
                    self._field[self._r-1][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu() and r.color(): 
        r.up()
        r.pt()
        r.dn()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-9':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                self._field[self._r+1][c].wUp = True
                if rnd(2):
                    self._field[self._r][c].wUp = True
                else:
                    if rnd(2):
                        self._field[self._r-1][c].wUp = True
                if  not self._field[self._r][c].wUp and self._field[self._r-1][c].wUp:
                    self._field[self._r-1][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu(): 
        r.up()
        if r.wu(): r.pt()
        r.dn()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task8-10':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                else: 
                    self._field[self._r+1][c].label = 'green'
                if rnd(2):
                    self._field[self._r][c].wUp = True
                else: 
                    self._field[self._r-1][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu(): 
        r.up()
        r.pt()
        r.dn()
    if r.fd():
        r.dn()
        r.pt()
        r.up()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task8-11':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                else: 
                    self._field[self._r+1][c].label = 'green'
                if rnd(2):
                    self._field[self._r][c].wUp = True
                else: 
                    self._field[self._r-1][c].label = 'green'
                if self._field[self._r+1][c].wUp and self._field[self._r][c].wUp:
                    self._field[self._r][c].label = 'green'
                    
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu(): 
        r.up()
        r.pt()
        r.dn()
    if r.fd():
        r.dn()
        r.pt()
        r.up()
    if r.wd() and r.wu(): r.pt()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task8-12':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                self._field[self._r][c].wUp = True
                if rnd(2):
                    self._field[self._r][c].label = 'green'
                    self._field[self._r][c].color = 'green'
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                elif self._field[self._r][c].label == 'green': 
                    self._field[self._r+1][c].label = 'green'
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.color() and r.fd(): 
        r.dn()
        r.pt()
        r.up()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------        
        elif mn == 'task8-13':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if rnd(2):
                    self._field[self._r][c].label = 'green'
                    self._field[self._r][c].color = 'green'
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                if rnd(2):
                    self._field[self._r][c].wUp = True
                    
                if self._field[self._r][c].label == 'green' and not self._field[self._r][c].wUp or not self._field[self._r][c].wUp and not self._field[self._r+1][c].wUp : 
                    self._field[self._r-1][c].label = 'green'
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.color() and r.fu() or r.fu() and r.fd(): 
        r.up()
        r.pt()
        r.dn()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-14':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)
            
            t = 0
            for c in range (self._c,34):
                self._field[self._r+1][c].wUp = True
                if t < 2:
                    self._field[self._r][c].wUp = True
                    t +=1
                else:
                    t = 0
                    if rnd(3):
                        self._field[self._r-1][c].wUp = True
                    if rnd(3):
                        self._field[self._r-1][c].wLeft = True
                    if rnd(3):
                        self._field[self._r-1][c+1].wLeft = True
                        
            for c in range (self._c,35):
                if  self._field[self._r-1][c].wUp and self._field[self._r-1][c+1].wLeft and self._field[self._r-1][c].wLeft:
                    self._field[self._r][c].label = 'green'
                    

            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.fu(): 
        r.up()
        if r.wl() and r.wr() and r.wu():
            r.dn()
            r.pt()
        else:
            r.dn()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-15':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if rnd(3):
                    self._field[self._r][c].label = 'green'
                    self._field[self._r][c].color = 'green'
                if rnd(2):
                    self._field[self._r+1][c].wUp = True
                if rnd(2):
                    self._field[self._r][c].wUp = True
                    
                if self._field[self._r][c].label == 'green' and not self._field[self._r][c].wUp and self._field[self._r+1][c].wUp or not self._field[self._r][c].wUp and not self._field[self._r+1][c].wUp and not self._field[self._r][c].label: 
                    self._field[self._r-1][c].label = 'green'
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    if r.color() and r.fu() and r.wd() or r.fu() and r.fd() and not r.color(): 
        r.up()
        r.pt()
        r.dn()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-16':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)

            for c in range (self._c,34):
                if not rnd(3):
                    if rnd(2):
                        self._field[self._r+1][c].label = 'green'
                        self._field[self._r+1][c].color = 'green'
                    if rnd(2):
                        self._field[self._r-1][c].label = 'green'
                        self._field[self._r-1][c].color = 'green'
                else:
                    if rnd(2):
                        self._field[self._r+1][c].wUp = True
                    if rnd(2):
                        self._field[self._r][c].wUp = True
                    if rnd(2):
                        self._field[self._r+1][c].label = 'green'
                        self._field[self._r+1][c].color = 'green'
                    else:
                        self._field[self._r-1][c].label = 'green'
                        self._field[self._r-1][c].color = 'green'
                    
                if self._field[self._r+1][c].label == 'green' and  self._field[self._r-1][c].label == 'green' and not self._field[self._r][c].wUp and not self._field[self._r+1][c].wUp: 
                    self._field[self._r][c].label = 'green'
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
#r.sleep = 1
while r.fr():
    c_up = ''
    c_d = ''
    if r.fu():
        r.up()
        c_up = r.color()
        r.dn()
        if r.fd() and c_up: 
            r.dn()
            c_d = r.color()
            r.up()
    if c_d and c_up: r.pt()
    r.rt()           
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-17':
            self._nc = 35
            self._nr = 8
            self._size = 30
            self.clear()
            self._r = 4
            self._c = 1
            self._endPoint = (4,34)
            
            for c in range (self._c,34):
                self._field[self._r+1][c].wUp = True
                t = rnd(3)
                if not t:
                    self._field[self._r][c].wUp = True
                elif t == 1:
                        self._field[self._r-1][c].wUp = True
                        self._field[self._r-1][c].wLeft = True
                        self._field[self._r-1][c+1].wLeft = True
                else:
                        self._field[self._r-2][c].wUp = True
                        self._field[self._r-2][c].wLeft = True
                        self._field[self._r-2][c+1].wLeft = True
                        self._field[self._r-1][c].wLeft = True
                        self._field[self._r-1][c+1].wLeft = True
                        self._field[self._r][c].label = 'green'
                        
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    a = 0
    while r.fu():
        a += 1
        r.up()
    b = a
    for b in range(a): r.dn()
    if a == 2: r.pt()
    r.rt()
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-18':
            self._nc = 35
            self._nr = 9
            self._size = 30
            self.clear()
            self._r = 7
            self._c = 1
            self._endPoint = (7,34)
            
            for c in range (self._c,34):
                self._field[self._r+1][c].wUp = True
                t = rnd(3)
                if not t:
                    self._field[self._r][c].wUp = True
                else:
                    t = 1+rnd(6)
                    cc = 0
                    for d in range(1,t):
                        self._field[self._r-d][c].wLeft = True
                        self._field[self._r-d][c+1].wLeft = True
                        if rnd(3):
                            self._field[self._r-d][c].color = 'green'
                            self._field[self._r-d][c].label = 'green'
                            cc += 1
                    self._field[self._r-t+1][c].wUp = True
                    if cc ==3: self._field[self._r][c].label = 'green'
                        
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    a = 0
    while r.fu():
        if r.color(): a += 1
        r.up()
    if r.color(): a += 1
    while r.fd(): r.dn()
    if a == 3: r.pt()
    r.rt()
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить отмеченные'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-19':
            self._nc = 35
            self._nr = 9
            self._size = 30
            self.clear()
            self._r = 7
            self._c = 1
            self._endPoint = (7,34)
            
            for c in range (self._c,34):
                self._field[self._r+1][c].wUp = True
                t = rnd(3)
                if not t:
                    self._field[self._r][c].wUp = True
                else:
                    t = 2+rnd(5)
                    cc_red = cc_green = 0
                    for d in range(1,t):
                        self._field[self._r-d][c].wLeft = True
                        self._field[self._r-d][c+1].wLeft = True
                        if rnd(3):
                            self._field[self._r-d][c].color = 'green'
                            self._field[self._r-d][c].label = 'green'
                            cc_green += 1
                        else:
                            self._field[self._r-d][c].color = 'red'
                            self._field[self._r-d][c].label = 'red'
                            cc_red += 1
                    self._field[self._r-t+1][c].wUp = True
                    if cc_red > cc_green: self._field[self._r][c].label = 'red'
                    elif cc_red < cc_green: self._field[self._r][c].label = 'green'
                    else: self._field[self._r][c].label = 'cyan'
                        
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    green = 0
    red = 0
    if r.fu():
        while r.fu():
            r.up()
            if r.color() == 'red': red += 1
            else: green += 1
        while r.fd(): r.dn()
        if green > red: r.pt()
        elif red > green: r.pt('red')
        else: r.pt('cyan')
    
    r.rt()
"""
      
            self.sleep = 0.04
            self._task = 'Закрасить красным или зеленым. Тем цветом, который встречается чаще в верхнем тупике\n'
            self._task += 'Если красный и зеленый встречается одинаково, то закрасить голубым (cyan)'

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-20':
            self._nc = 35
            self._nr = 9
            self._size = 30
            self.clear()
            self._r = 7
            self._c = 1
            self._endPoint = (7,34)
            
            for c in range (self._c,34):
                self._field[self._r+1][c].wUp = True
                t = rnd(3)
                if not t:
                    self._field[self._r][c].wUp = True
                else:
                    t = 2+rnd(5)
                    cc = 0
                    for d in range(1,t):
                        self._field[self._r-d][c].wLeft = True
                        self._field[self._r-d][c+1].wLeft = True
                        if not rnd(3):
                            self._field[self._r-d][c].color = 'green'
                            self._field[self._r-d][c].label = 'green'
                            cc += 1

                    self._field[self._r-t+1][c].wUp = True
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
while r.fr():
    cc = 0
    while r.fu():
        r.up()
        if r.color(): cc += 1
    while r.fd(): r.dn()
    if not cc: r.sw('up')
    r.rt()
"""
            self.sleep = 0.04
            self._task = 'Закрыть вход в тупики, где нет закрашенных клеток\n'
            self._test = """
w = l = p = True
if self._endPoint != self.getCoords(): p = False
self._r = 7
self._c = 1
for c in range (self._c,34):
    cc = 0
    rr = self._r
    while not self._field[rr][c].wUp:
        rr -= 1
        if self._field[rr][c].color == 'green': cc += 1
    if not cc and not self._field[self._r][c].wUp: w = False
"""
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-21':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            t = rnd(4)
            if t == 0:
                self._r = 1
                self._c = 1
                self._endPoint = (9,9)
            elif t == 1:
                self._r = 9
                self._c = 9
                self._endPoint = (1,1)
            elif t == 2:
                self._r = 1
                self._c = 9
                self._endPoint = (9,1)
            else:
                self._r = 9
                self._c = 1
                self._endPoint = (1,9)
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._solve = """
if r.wu():
    while r.fd(): r.dn()
else:
    while r.fu(): r.up()

if r.wl():    
    while r.fr(): r.rt()
else:
    while r.fl(): r.lt()
"""
            self.sleep = 0.04
            self._task = 'Перейти в противополжный угол \n(в каком углу Робот вначале - неизвестно) '
            
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-22':
            self._nc = 12
            self._nr = 12
            self._size = 30
            self.clear()
            
            if rnd(2):
                self._r = self._nr-1
                self._c = (self._nr-1) // 3
                rr = 2+rnd(5)
                for r in range(self._r,rr,-1):
                    self._field[r][self._c+1].wLeft = True
                    self._field[r][self._c].wLeft = True
                self._field[rr+1][self._c].wUp = True
                cc = rnd(self._c,self._nc-2)
                rr += 1
                for c in range(self._c,cc):
                    self._field[rr+1][c].wUp = True
                    self._field[rr][c].wUp = True
                if self._c != cc: 
                    self._endPoint = (rr,cc-1)
                    self._field[r][self._c+1].wLeft = False
                else: 
                    self._endPoint = (rr,cc)
                    self._field[r][self._c+1].wLeft = True
                    
                    
                self._field[rr][cc].wLeft = True
                self._field[r+1][self._c].wUp = False
            else:
                self._r = self._nr-1
                self._c = 2 * (self._nr-1) // 3
                rr = 2+rnd(5)
                for r in range(self._r,rr,-1):
                    self._field[r][self._c+1].wLeft = True
                    self._field[r][self._c].wLeft = True
                self._field[rr+1][self._c].wUp = True
                cc = rnd(2,self._c)
                self._field[r][self._c].wLeft = False
                rr += 1
                for c in range(cc,self._c):
                    self._field[rr+1][c].wUp = True
                    self._field[rr][c].wUp = True
                self._endPoint = (rr,cc)
                    
                self._field[rr][cc].wLeft = True
                self._field[r+1][self._c].wUp = False
            
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._task = "Дойти до конца тупика (буквой Г влево или вправо)"
            
            self._solve= """
while r.fu(): r.up()
if r.fr():
    while r.fr(): r.rt()
elif r.fl():
    while r.fl(): r.lt()
    
"""
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-23':
            self._nc = 25
            self._nr = 5
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 2
            c1 = rnd(10,20)
            c2 = c1
            while c2 == c1:
                c2 = rnd(10,20)
            for c in range(self._c,c1):
                self._field[self._r][c].wUp = True
                
            for c in range(self._c,c2):
                self._field[self._r+2][c].wUp = True
                    
            if c1 < c2:
                self._endPoint = (self._r,c1)
            else:
                self._endPoint = (self._r+1,c2)
                
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._task = "Перейти в конец более короткой стены \n"
            self._task += "Размеры стен заранее неизвестны \n"
            
            self._solve= """
r.sleep = 0.1
while r.wu():
    r.dn()
    r.rt()
    if r.wd(): r.up()
"""
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-24':
            self._nc = 25
            self._nr = 5
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 2
            c1 = rnd(10,20)
            c2 = c1
            while c2 == c1:
                c2 = rnd(10,20)
            for c in range(self._c,c1):
                self._field[self._r][c].wUp = True
                
            for c in range(self._c,c2):
                self._field[self._r+2][c].wUp = True
                    
            if c1 > c2:
                self._endPoint = (self._r,c1)
            else:
                self._endPoint = (self._r+1,c2)
                
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._task = "Перейти в конец более длинной стены \n"
            self._task += "Размеры стен заранее неизвестны \n"
            
            self._solve= """
r.sleep = 0.1
while r.wu():
    r.rt()
r.dn()
if r.wd():
    while r.wd(): r.rt()
else:
    r.up()
"""
            

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-25':
            self._nc = 25
            self._nr = 5
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 2
            c1 = rnd(10,20)
            c2 = c1
            while c2 == c1:
                c2 = rnd(10,20)
            for c in range(self._c,c1):
                self._field[self._r][c].color = self._field[self._r][c].label = 'green'
                
            for c in range(self._c,c2):
                self._field[self._r+1][c].color = self._field[self._r+1][c].label = 'green'
                    
            if c1 > c2:
                self._endPoint = (self._r,c1)
            else:
                self._endPoint = (self._r+1,c2)
                
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._task = "Перейти в конец длинного закрашенного ряда \n"
            
            self._solve= """
r.sleep = 0.04
while r.color():
    r.rt()
r.dn()
if r.color():
    while r.color(): r.rt()
else:
    r.up()
"""
                 
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-26':
            self._nc = 25
            self._nr = 5
            self._size = 30
            self.clear()
            self._r = 2
            self._c = 2
            c1 = rnd(10,20)
            c2 = c1
            while c2 == c1:
                c2 = rnd(10,20)
            for c in range(self._c,c1):
                self._field[self._r][c].color = self._field[self._r][c].label = 'green'
                
            for c in range(self._c,c2):
                self._field[self._r+1][c].color = self._field[self._r+1][c].label = 'green'
                    
            if c1 < c2:
                self._endPoint = (self._r,c1)
            else:
                self._endPoint = (self._r+1,c2)
                
            
            self.sleep = 0.1
            self._Nonelabel = True
            self._task = "Перейти в конец короткого закрашенного ряда \n"
            
            self._solve= """
r.sleep = 0.04
while r.color():
    r.dn()
    r.rt()
    if r.color():
        r.up()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-27':
            self._nc = 10
            self._nr = 10
            self._size = 30
            self.clear()
            self._r = 8
            self._c = 5

            r = rnd(2,5)
            c = self._c
            while c == self._c:
                c = rnd(2,9)
            print(r,c)

            self._field[r][c].color = self._field[r][c].label =  self.randcolor()
            self._field[r][self._c].color =  self._field[r][self._c].label = self.randcolor()

            self._endPoint = (r,c)
                
            
            self.sleep = 0.1
            self._NoneisPark = True
            self._task = "Перейти на вторую закрашенную клетку \nцвет неизвестен\nможет быть как справа, так и слева\n"
            
            self._solve= """
r.sleep = 0.04
while not r.color():
    r.up()
r.rt()
while not r.color() and r.fr(): 
    r.rt()
if r.wr():
    while not r.color(): 
        r.lt()
    r.lt()
    while not r.color(): 
        r.lt()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-28':
            self._nr = 8
            self._nc = 14
            self._size = 30
            self.clear()
            self._r = 6
            self._c = 5

            c1 = rnd(2,4)
            c2 = rnd(9,13)

            for c in range(c1,c2):
                self._field[self._r][c].wUp = self._field[self._r+1][c].wUp =  True
            self._field[self._r][c1].wLeft = self._field[self._r][c2].wLeft =  True
            
            if rnd(2):
                rr = rnd(6,8)
                cc = rnd(c1,c2)
                self._field[rr][cc].wUp = False
            else:
                if rnd(2):
                    self._field[self._r][c1].wLeft = False
                else:
                    self._field[self._r][c2].wLeft = False
                


            self._endPoint = (1,1)
            self.sleep = 0.1
            self._task = "Выйти из ловушки. Где находиться выход - неизвестно."
            self._solve= """
r.sleep = 0.04
while r.wu() and r.wd() and r.fl():
    r.lt()
if r.wu() and r.wd() and r.wl(): 
    while r.wu() and r.wd() and r.fr():
        r.rt()
if r.wu() and r.wd() and r.wr(): 
    print "Выхода нет. Ключ поверни и полетели..."
else:
    if r.fu():
        while r.fu(): r.up()
        while r.fl(): r.lt()
    elif r.fd():
        r.dn()
        while r.fl(): r.lt()
        while r.fu(): r.up()

"""
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-29':
            self._nr = 8
            self._nc = 14
            self._size = 30
            self.clear()
            self._r = 6
            self._c = 5

            c1 = rnd(2,4)
            c2 = rnd(9,13)

            self._endPoint = (1,1)
            for c in range(c1,c2):
                self._field[self._r][c].wUp = self._field[self._r+1][c].wUp =  True
            self._field[self._r][c1].wLeft = self._field[self._r][c2].wLeft =  True
            if rnd(2):
                #print "!"
                if rnd(2):
                    rr = rnd(6,8)
                    cc = rnd(c1,c2)
                    self._field[rr][cc].wUp = False
                else:
                    if rnd(2):
                        self._field[self._r][c1].wLeft = False
                    else:
                        self._field[self._r][c2].wLeft = False
            else:
                self._endPoint = (self._r,c2-1)

            self.sleep = 0.1
            self._task = "Выйти из ловушки. Где находиться выход - неизвестно.\n Выхода может не быть, в этом случае остановиться в правом тупике\n"
            self._solve= """
r.sleep = 0.04
while r.wu() and r.wd() and r.fl():
    r.lt()
if r.wu() and r.wd() and r.wl(): 
    while r.wu() and r.wd() and r.fr():
        r.rt()
if r.wu() and r.wd() and r.wr(): 
    print "Выхода нет. Ключ поверни и полетели..."
else:
    if r.fu():
        while r.fu(): r.up()
        while r.fl(): r.lt()
    elif r.fd():
        r.dn()
        while r.fl(): r.lt()
        while r.fu(): r.up()

"""
                 
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task8-30':
            self._nr = 16
            self._nc = 10
            self._size = 30
            self.clear()
            self._r = 1
            self._c = 8

            self._endPoint = (self._nr-1,1)
            for r in range(2+rnd(3),self._nr-1,rnd(4)+2):
                for c in range(1,self._nc):
                    self._field[r][c].wUp = True
                self._field[r][rnd(1,self._nc-1)].wUp = False

            self.sleep = 0.1
            self._task = "Погружение. Добраться до нижнего уровня.\n Количество уровней неизвестно\n"
            self._task +="След. задача: task9-1"
            self._solve = """
while r.fr(): r.rt()
while r.fl() and r.wd(): r.lt()
while r.fd(): 
    r.dn()
    while r.fr(): r.rt()
    while r.fl() and r.wd(): r.lt()
"""

        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-1':
            self._nr = 21
            self._nc = 21
            self._size = 27
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (20,1)

            for r in range(1,self._nr-1):
                for c in range(1,self._nc-1):
                    if r > c:
                        self._field[r][c].label = 'yellow'
                    else:
                        self._field[r][c].label =  'red'

            self.sleep = 0.001
            self._Nonelabel = True
            self._task = "Закрасить поле 'треугольниками': см r.demo()\n"
            self._solve= """
for rr in range(19):
    for cc in range(19):
        if rr > cc: r.pt('yellow')
        else: r.pt('red')
        r.rt()
    r.lt(19)
    r.dn()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-2':
            self._nr = 21
            self._nc = 21
            self._size = 27
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (20,1)

            for r in range(1,self._nr-1):
                for c in range(1,self._nc-1):
                    if r > c:
                        self._field[r][c].label = 'yellow'
                    if r < c:
                        self._field[r][c].label =  'red'

            self.sleep = 0.001
            self._Nonelabel = True
            self._task = "Закрасить поле 'треугольниками': см r.demo()\n"
            self._solve= """
for rr in range(19):
    for cc in range(19):
        if rr > cc: r.pt('yellow')
        if rr < cc: r.pt('red')
        r.rt()
    r.lt(19)
    r.dn()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-2':
            self._nr = 21
            self._nc = 21
            self._size = 27
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (20,1)

            for r in range(1,self._nr-1):
                for c in range(1,self._nc-1):
                    if r > (self._nc-c-1):
                        self._field[r][c].label = 'yellow'
                    if r < (self._nc-c-1):
                        self._field[r][c].label =  'red'

            self.sleep = 0.001
            self._Nonelabel = True
            self._task = "Закрасить поле 'треугольниками': см r.demo()\n"
            self._solve= """
for rr in range(19):
    for cc in range(19):
        if rr > (19-cc-1): r.pt('yellow')
        if rr < (19-cc-1): r.pt('red')
        r.rt()
    r.lt(19)
    r.dn()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-3':
            self._nr = 21
            self._nc = 21
            self._size = 27
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (20,1)

            for r in range(1,self._nr-1):
                for c in range(1,self._nc-1):
                    if r > (self._nc-c-1) and (r > c): self._field[r][c].label = 'yellow'
                    if r < (self._nc-c-1) and (r > c): self._field[r][c].label = 'red'
                    if r > (self._nc-c-1) and (r < c): self._field[r][c].label = 'green'
                    if r < (self._nc-c-1) and (r < c): self._field[r][c].label = 'blue'

            self.sleep = 0.001
            self._Nonelabel = True
            self._task = "Закрасить поле 'треугольниками': см r.demo()\n"
            self._solve= """
for rr in range(19):
    for cc in range(19):
        if rr > cc and rr > (19-cc-1): r.pt('yellow')
        if rr > cc and rr < (19-cc-1): r.pt('red')
        if rr < cc and rr > (19-cc-1): r.pt('green')
        if rr < cc and rr < (19-cc-1): r.pt('blue')
        r.rt()
    r.lt(19)
    r.dn()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-4':
            self._nr = 14+rnd(5)
            self._nc = 14+rnd(5)
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (0,0)

            self.sleep = 0.001
            self._Nonelabel = True
            self._task = "Спираль внутрь: см. r.demo()\n"
            self._test = """
if self._endPoint != self.getCoords(): p = False
a = 0
d = 0
r = 1
c = 1 
l = w = p = t = True
work = True
r1 = 1 
c1 = 0
r2 = self._nr
c2 = self._nc
while t and work:
    a += 1
    if self._field[r][c].text <> a: t = False
    else:
        if d == 0:
            c += 1
            if c == c2:
                c -= 1
                r += 1
                d += 1
                c2 -= 1
        elif d == 1:
            r += 1
            if r == r2:
                r -= 1
                c -= 1
                d += 1
                r2 -= 1
        elif d == 2:
            c -= 1
            if c == c1:
                c += 1
                r -= 1
                d += 1
                c1 += 1
        elif d == 3:
            r -= 1
            if r == r1:
                r += 1
                c += 1
                d = 0
                r1 += 1
    if abs(c1-c2) == 1 or abs(r1-r2) == 1: work = False
"""
            self._solve= """
a = 0
d = 0
def gtr():
    t = ''
    if r.fr():
        r.rt()
        t = r.gettext()
        r.lt()
    return t

def gtl():
    t = ''
    if r.fl():
        r.lt()
        t = r.gettext()
        r.rt()
    return t

def gtu():
    t = ''
    if r.fu():
        r.up()
        t = r.gettext()
        r.dn()
    return t

def gtd():
    t = ''
    if r.fd():
        r.dn()
        t = r.gettext()
        r.up()
    return t


while not r.gettext():
    a += 1
    r.settext(a)
    if d == 0:
        if r.fr() and not gtr(): 
            r.rt()
        else: 
            r.dn()
            d += 1
    elif d == 1:
        if r.fd() and not gtd(): 
            r.dn()
        else:
            d += 1
            r.lt()
    elif d == 2:
        if r.fl() and not gtl(): 
            r.lt()
        else: 
            d += 1
            r.up()
    elif d == 3:
        if r.fu() and not gtu(): 
            r.up()
        else: 
            d = 0
            r.rt()

"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-5':
            self._nr = 14
            self._nc = 18
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (self._nr-1,1)

            self.sleep = 0.01
            self._Nonelabel = True
            self._Nonesettext = True

            for r in range(self._nr-1):
                for c in range(self._nc-1):
                    self._field[r][c].text = rnd(10)
                    if self._field[r][c].text % 2 == 0: self._field[r][c].label = 'green'

            self._task = "Четные цифры закрасить зеленым\n"

            self._solve = """
for rr in range(12):
    for cc in range(16):
        if r.gettext() != '' and r.gettext() % 2 == 0: 
            r.pt()
        r.rt()
    r.lt(16)
    r.dn()
"""     

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-6':
            self._nr = 10
            self._nc = 6
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (self._nr-1,1)

            self.sleep = 0.01
            self._Nonelabel = True
            for r in range(self._nr-1):
                for c in range(self._nc-1):
                    self._field[r][c].text = rnd(10)

            self._task = "Сумму каждой строки вписать в последний столбец\n"

            self._solve = """
while r.fd():
    s = 0
    while r.fr():
        if r.gettext(): s += r.gettext()
        r.rt()
    r.settext(s)
    while r.fl(): r.lt()
    r.dn()
"""     
            self._test = """
l = p = w = t = True
for r in range(1,self._nr-1):
    s = 0
    for c in range(1,self._nc-1):
        if self._field[r][c].text: s += self._field[r][c].text
    if self._field[r][self._nc-1].text != s: t = False
    print  self._field[r][self._nc-1].text , s , t
if self._endPoint != self.getCoords(): p = False

"""
        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-7':
            self._nr = 8
            self._nc = 12
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (1,self._nc-1)

            self.sleep = 0.01
            self._Nonelabel = True
            for r in range(self._nr-1):
                for c in range(self._nc-1):
                    self._field[r][c].text = rnd(10)

            self._task = "Сумму каждого столбца вписать в последнюю строку\n"

            self._solve = """
while r.fr():
    s = 0
    while r.fd():
        if r.gettext(): s += r.gettext()
        r.dn()
    r.settext(s)
    while r.fu(): r.up()
    r.rt()
"""     
            self._test = """
l = p = w = t = True
for c in range(1,self._nc-1):
    s = 0
    for r in range(1,self._nr-1):
        if self._field[r][c].text: s += self._field[r][c].text
    if self._field[self._nr-1][c].text != s: t = False
    print  self._field[self._nr-1][c].text , s , t
if self._endPoint != self.getCoords(): p = False
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-8':
            self._nr = 8
            self._nc = 12
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (self._nr-1,1)

            self.sleep = 0.01
            self._Nonelabel = True
            for r in range(self._nr-1):
                for c in range(self._nc-1):
                    self._field[r][c].text = rnd(10)

            self._task = "Найти сумму четных и вписать в клетку с парковкой\n"

            self._solve = """
s = 0
while r.fd():
    while r.fr():
        if r.gettext() and r.gettext() % 2 == 0: s += r.gettext()
        r.rt()
    while r.fl(): r.lt()
    r.dn()
r.settext(s)
"""     
            self._test = """
l = p = w = t = True
s = 0
for r in range(1,self._nr-1):
    for c in range(1,self._nc-1):
        if self._field[r][c].text and  self._field[r][c].text % 2 == 0: s += self._field[r][c].text
if self._field[self._nr-1][1].text != s: t = False
if self._endPoint != self.getCoords(): p = False
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-9':
            self._nr = 8
            self._nc = 12
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (self._nr-1,1)

            self.sleep = 0.01
            self._Nonelabel = True
            for r in range(self._nr-1):
                for c in range(self._nc-1):
                    self._field[r][c].text = rnd(100)

            self._task = "Найти минимальное значение вписать в клетку с парковкой\n"

            self._solve = """
min = r.gettext()
while r.fd():
    while r.fr():
        if r.gettext() != '' and r.gettext() < min: min = r.gettext()
        r.rt()
    while r.fl(): r.lt()
    r.dn()
r.settext(min)
"""     
            self._test = """
l = p = w = t = True
min = self._field[1][1].text
for r in range(1,self._nr-1):
    for c in range(1,self._nc-1):
        if self._field[r][c].text != '' and  self._field[r][c].text < min : min = self._field[r][c].text
if self._field[self._nr-1][1].text != min: t = False
if self._endPoint != self.getCoords(): p = False
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task9-10':
            self._nr = 8
            self._nc = 12
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 1
            self._c = 1
            self._endPoint = (self._nr-1,1)

            self.sleep = 0.01
            self._Nonelabel = True
            for r in range(self._nr-1):
                for c in range(self._nc-1):
                    self._field[r][c].text = rnd(100)

            self._task = "Найти максимальное значение вписать в клетку с парковкой\n"
            self._task += "След. задача: task10-1\n"
            self._solve = """
max = r.gettext()
while r.fd():
    while r.fr():
        if r.gettext() != '' and r.gettext() > max: max = r.gettext()
        r.rt()
    while r.fl(): r.lt()
    r.dn()
r.settext(max)
"""     
            self._test = """
l = p = w = t = True
max = self._field[1][1].text
for r in range(1,self._nr-1):
    for c in range(1,self._nc-1):
        if self._field[r][c].text != '' and  self._field[r][c].text > max : max = self._field[r][c].text
if self._field[self._nr-1][1].text != max: t = False
if self._endPoint != self.getCoords(): p = False
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task10-1':
            self._nr = 10
            self._nc = 16
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 6
            self._c = 2+rnd(3)

            self._endPoint = (self._r,self._c)
            cc = rnd(7,15)
            self._field[self._r][cc].wLeft = True
            self._field[self._r][cc-1].label = 'green'

            self.sleep = 0.1
            self._Nonelabel = True

            self._task = "Дойти до стены, закрасить и вернуться\nИспользовать рекурсивную процедуру (см. task7-0)"
            self._solve = """
global step
def step():
    if r.fr():
        r.rt()
        step()
        r.lt()
    else: 
        r.pt()
step()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task10-2':
            self._nr = 10
            self._nc = 16
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 8
            self._c = 3

            self._endPoint = (self._r,self._c)
            cc = rnd(self._c+5,15)
            for x in range(self._c+1,cc):
                self._field[self._r][x].wLeft = True
            self._field[self._r][cc-1].label = 'green'

            self.sleep = 0.07
            self._Nonelabel = True

            self._task = "Обойти забор, закрасить и вернуться\nИспользовать рекурсивную процедуру (см. task7-0)"
            self._solve = """
global step
def step():
    r.up()
    r.rt()
    r.dn()
    if r.wr():
        step()
    else: 
        r.pt()
    r.up()
    r.lt()
    r.dn()
step()
"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task10-3':
            self._nc = 30
            self._nr = 30
            self._size = 25
            self._field = []
            
            for r in range(1,self._nr+2):
                row = []
                for c in range(1,self._nc+2):
                    row.append (self._Tcell())
                self._field.append(row)
                
            self.clear()
            self._r = 15
            self._c = 15
            self._Nonelabel = True
            choise = rnd(4)
            self._endPoint = (self._r,self._c)
            # ------------ червячки
            if choise == 0:
                for t in range(1,100):
                    cr = rnd(1,30)
                    cc = rnd(1,30)
                    self._field[cr][cc].wUp = True
                    cr = rnd(1,30)
                    cc = rnd(1,30)
                    self._field[cr][cc].wLeft = True
            # ------------ спираль
            if choise == 1:
                d = 0
                r = 1
                c = 1 
                r1 = 3 
                c1 = 2
                r2 = self._nr-2
                c2 = self._nc-2
                while abs(c1-c2) >= 2 and abs(r1-r2) >= 2:
                    if d == 0:
                        c += 1
                        self._field[r+1][c].wUp = True
                        if c == c2:
                            self._field[r+1][c].wUp = False
                            c -= 1
                            r += 1
                            d += 1
                            c2 -= 1
                    elif d == 1:
                        r += 1
                        self._field[r][c].wLeft = True
                        if r == r2:
                            self._field[r][c].wLeft = False
                            r -= 1
                            c -= 1
                            d += 1
                            r2 -= 1
                    elif d == 2:
                        c -= 1
                        self._field[r][c].wUp = True
                        if c == c1:
                            self._field[r][c].wUp = False
                            c += 1
                            r -= 1
                            d += 1
                            c1 += 1
                    elif d == 3:
                        r -= 1
                        self._field[r][c+1].wLeft = True
                        if r == r1:
                            self._field[r][c+1].wLeft = False
                            r += 1
                            c += 1
                            d = 0
                            r1 += 1
            # ------------ пустое поле
            if choise == 2:
                pass
            # ------------ коридор с коридорами?
            if choise == 3:
                self._field[self._r][3].wLeft = True
                self._field[self._r][self._nc-3].wLeft = True
                for c in range(3,self._nc-3):
                    self._field[self._r][c].wUp = True
                    self._field[self._r+1][c].wUp = True
                c = rnd(3,6)
                self._field[3][c].wUp = True
                self._field[self._nr-3][c].wUp = True
                for r in range(3,self._nr-3):
                    if r != self._r:
                        self._field[r][c].wLeft = True
                        self._field[r][c+1].wLeft = True
                    else:
                        self._field[self._r][c].wUp = False
                        self._field[self._r+1][c].wUp = False
                c = rnd(9,12)
                self._field[3][c].wUp = True
                self._field[self._nr-3][c].wUp = True
                for r in range(3,self._nr-3):
                    if r != self._r:
                        self._field[r][c].wLeft = True
                        self._field[r][c+1].wLeft = True
                    else:
                        self._field[self._r][c].wUp = False
                        self._field[self._r+1][c].wUp = False
                c = rnd(15,19)
                self._field[3][c].wUp = True
                self._field[self._nr-3][c].wUp = True
                for r in range(3,self._nr-3):
                    if r != self._r:
                        self._field[r][c].wLeft = True
                        self._field[r][c+1].wLeft = True
                    else:
                        self._field[self._r][c].wUp = False
                        self._field[self._r+1][c].wUp = False
                c = rnd(20,25)
                self._field[3][c].wUp = True
                self._field[self._nr-3][c].wUp = True
                for r in range(3,self._nr-3):
                    if r != self._r:
                        self._field[r][c].wLeft = True
                        self._field[r][c+1].wLeft = True
                    else:
                        self._field[self._r][c].wUp = False
                        self._field[self._r+1][c].wUp = False
                r = 8
                self._field[r][3].wLeft = True
                self._field[r][self._nc-3].wLeft = True
                for c in range(3,self._nc-3):
                    if not (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wUp = True
                        self._field[r+1][c].wUp = True
                    elif (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wLeft = False
                        self._field[r][c+1].wLeft = False
                r = 22
                self._field[r][3].wLeft = True
                self._field[r][self._nc-3].wLeft = True
                for c in range(3,self._nc-3):
                    if not (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wUp = True
                        self._field[r+1][c].wUp = True
                    elif (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wLeft = False
                        self._field[r][c+1].wLeft = False
            self._test = '-'
            self._task = 'Закрасить все клетки'
            self._solve = """
global pp
global color
color= 'green'
def pp(color):
    if not r.color():
        r.pt(color)
        if r.fu():
            r.up()
            pp('red')
            r.dn()
        if r.fl():
            r.lt()
            pp('yellow')
            r.rt()
        if r.fr():
            r.rt()
            pp('green')
            r.lt()
        if r.fd():
            r.dn()
            pp('blue')
            r.up()
print "Рекурсия. В глубину"
pp('green')
print "Конец программы..."

"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task10-4':
            self._nr = 16
            self._nc = 16
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 7
            self._c = 7

            choise = rnd(4)
            self._endPoint = (self._r,self._c)
            # ------------ червячки
            if choise == 0:
                for t in range(1,100):
                    cr = rnd(1,self._nr)
                    cc = rnd(1,self._nc)
                    self._field[cr][cc].wUp = True
                    cr = rnd(1,self._nr)
                    cc = rnd(1,self._nc)
                    self._field[cr][cc].wLeft = True
            # ------------ спираль
            if choise == 1:
                d = 0
                r = 1
                c = 1 
                r1 = 3 
                c1 = 2
                r2 = self._nr-2
                c2 = self._nc-2
                while abs(c1-c2) >= 2 and abs(r1-r2) >= 2:
                    if d == 0:
                        c += 1
                        self._field[r+1][c].wUp = True
                        if c == c2:
                            self._field[r+1][c].wUp = False
                            c -= 1
                            r += 1
                            d += 1
                            c2 -= 1
                    elif d == 1:
                        r += 1
                        self._field[r][c].wLeft = True
                        if r == r2:
                            self._field[r][c].wLeft = False
                            r -= 1
                            c -= 1
                            d += 1
                            r2 -= 1
                    elif d == 2:
                        c -= 1
                        self._field[r][c].wUp = True
                        if c == c1:
                            self._field[r][c].wUp = False
                            c += 1
                            r -= 1
                            d += 1
                            c1 += 1
                    elif d == 3:
                        r -= 1
                        self._field[r][c+1].wLeft = True
                        if r == r1:
                            self._field[r][c+1].wLeft = False
                            r += 1
                            c += 1
                            d = 0
                            r1 += 1
            # ------------ пустое поле
            if choise == 2:
                pass
            # ------------ коридор с коридорами?
            if choise == 3:
                self._field[self._r][3].wLeft = True
                self._field[self._r][self._nc-3].wLeft = True
                for c in range(3,self._nc-3):
                    self._field[self._r][c].wUp = True
                    self._field[self._r+1][c].wUp = True
                c = rnd(3,6)
                self._field[3][c].wUp = True
                self._field[self._nr-3][c].wUp = True
                for r in range(3,self._nr-3):
                    if r != self._r:
                        self._field[r][c].wLeft = True
                        self._field[r][c+1].wLeft = True
                    else:
                        self._field[self._r][c].wUp = False
                        self._field[self._r+1][c].wUp = False
                c = rnd(9,12)
                self._field[3][c].wUp = True
                self._field[self._nr-3][c].wUp = True
                for r in range(3,self._nr-3):
                    if r != self._r:
                        self._field[r][c].wLeft = True
                        self._field[r][c+1].wLeft = True
                    else:
                        self._field[self._r][c].wUp = False
                        self._field[self._r+1][c].wUp = False
                r = 8
                self._field[r][3].wLeft = True
                self._field[r][self._nc-3].wLeft = True
                for c in range(3,self._nc-3):
                    if not (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wUp = True
                        self._field[r+1][c].wUp = True
                    elif (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wLeft = False
                        self._field[r][c+1].wLeft = False
                r = 12
                self._field[r][3].wLeft = True
                self._field[r][self._nc-3].wLeft = True
                for c in range(3,self._nc-3):
                    if not (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wUp = True
                        self._field[r+1][c].wUp = True
                    elif (self._field[r][c+1].wLeft and self._field[r][c].wLeft):
                        self._field[r][c].wLeft = False
                        self._field[r][c+1].wLeft = False
            self._test = '-'
            self.sleep = 0.01
            self._task = "Вписать в каждую клетку расстояние от начальной точки\n"
            self._solve = """
global pp
def pp(step):
    if not r.gettext() or r.gettext() > step:
        r.settext(step)
        if r.fu():
            r.up()
            pp(step+1)
            r.dn()
        if r.fl():
            r.lt()
            pp(step+1)
            r.rt()
        if r.fr():
            r.rt()
            pp(step+1)
            r.lt()
        if r.fd():
            r.dn()
            pp(step+1)
            r.up()

r.sleep = 0
#r._NoneUpdate = True
pp(1)
r._NoneUpdate = False
r._update()

"""

        ##--------------------------------------------------------------------------------------------
        elif mn == 'task10-5':
            self._nr = 16
            self._nc = 16
            self._size = 30
            self._font_size = '11'
            self.clear()
            self._r = 7
            self._c = 7
            self._field[self._r][self._c].label = 'green'
            self._field[self._r][self._c].color = 'green'


            # ------------ червячки
            if rnd(2):
                for t in range(1,100+rnd(80)):
                    cr = rnd(1,self._nr)
                    cc = rnd(1,self._nc)
                    self._field[cr][cc].wUp = True
                    cr = rnd(1,self._nr)
                    cc = rnd(1,self._nc)
                    self._field[cr][cc].wLeft = True
            # иначе ------------ пустое поле
            cr = rnd(1,self._nr)
            cc = rnd(1,self._nc)
            self._endPoint = (cr,cc)

            
            self._test = '-'
            self.sleep = 0.01
            self._task = "Найти короткий путь до базы и закрасить его\n"
            self._task += "Это последняя задача. Переходите к следующему курсу. progras.ru"
            self._solve = """
q = [r.getCoords()]
step = 0
r.settext(step)
find = False
while q and not find:
    q1 = []
    while q:
        r.jumpTo(q.pop())
        if r.fr():
            r.rt()
            if r.isPark(): 
                find = True
                break
            if r.gettext() == '':
                q1.append(r.getCoords())
                r.settext(step+1)
            r.lt()
        if r.fl():
            r.lt()
            if r.isPark(): 
                find = True
                break
            if r.gettext() == '':
                q1.append(r.getCoords())
                r.settext(step+1)
            r.rt()
        if r.fu():
            r.up()
            if r.isPark(): 
                find = True
                break
            if r.gettext() == '':
                q1.append(r.getCoords())
                r.settext(step+1)
            r.dn()
        if r.fd():
            r.dn()
            if r.isPark(): 
                find = True
                break
            if r.gettext() == '':
                q1.append(r.getCoords())
                r.settext(step+1)
            r.up()
    q = q1[:]
    step += 1

def tomin():
    coords = []
    texts = []
    if r.fr():
        r.rt()
        texts.append(r.gettext())
        coords.append(r.getCoords())
        r.lt()
    if r.fl():
        r.lt()
        texts.append(r.gettext())
        coords.append(r.getCoords())
        r.rt()
    if r.fd():
        r.dn()
        texts.append(r.gettext())
        coords.append(r.getCoords())
        r.up()
    if r.fu():
        r.up()
        texts.append(r.gettext())
        coords.append(r.getCoords())
        r.dn()
    r.pt()
    print min(texts)
    print texts.index(min(texts))
    print coords[texts.index(min(texts))]
    r.jumpTo (coords[texts.index(min(texts))])
    return min(texts)
if find:
    while tomin() > 1:
        pass
else:
    r.pt('red')

"""

        ##--------------------------------------------------------------------------------------------
# сделать прямое управление с демонстрацией датчиков и возможностей
# при запуске робота создавать task.py и справочник :)
# сделать робота без клеток !!!
        ##--------------------------------------------------------------------------------------------
        ##--------------------------------------------------------------------------------------------
        else:
            print(mn)
            self._task = "Нет задачи с таким номером"
            self._test = '-'

        self._canvas.config(
            width=(self._size*(self._nc+1)),
            height=(self._size*(self._nr+1)))
        x = y = 1
        d = self._d
        d = 6
        self._robot = self._canvas.create_oval(
            x*self._size+d,y*self._size+d,
            x*self._size+self._size-d,y*self._size+self._size-d,
            outline = '#4400FF', width = 3)

        self._paintMap()
 

    lm = loadmap
    lt = left
    rt = right
    dn = down
    dn = down
    pt = paint
    sw = setWall
    wu = wallUp
    wd = wallDown
    wl = wallLeft
    wr = wallRight
    fu = freeUp
    fd = freeDown
    fl = freeLeft
    fr = freeRight
    cl = color
