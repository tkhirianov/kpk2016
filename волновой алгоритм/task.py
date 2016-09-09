#-*- coding: utf-8 -*
import robot
r = robot.rmap()
r.lm('task10-5')
def task():
    pass
    #------- пишите код здесь -----

    queue = [r.getCoords()]
    step = 0
    r.settext(step)
    find = False
    while queue and not find:
        q1 = []
        while queue:
            r.jumpTo(queue.pop())
            if r.freeRight():
                r.right()
                if r.isPark():
                    find = True
                    break
                if r.gettext() == '':
                    q1.append(r.getCoords())
                    r.settext(step+1)
                r.left()
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
            if r.freeDown():
                r.down()
                if r.isPark():
                    find = True
                    break
                if r.gettext() == '':
                    q1.append(r.getCoords())
                    r.settext(step+1)
                r.up()
        queue = q1[:]
        step += 1

    def tomin():
        """ шагает из текущей клетки в соседнюю,
        в которой минимальное значение
        возвращает количество шагов от текущей до начала """

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
        # везде, где текст в ячейке не является числом -- ставим 10000
        texts[:] = [10000 if x == '' else x for x in texts]
        print(min(texts))
        print(texts.index(min(texts)))
        print(coords[texts.index(min(texts))])
        r.jumpTo (coords[texts.index(min(texts))])
        return min(texts)

    if find:
        while tomin() > 0:
            pass
    else:
        r.paint('red')
    
    #------- пишите код здесь -----
r.start(task)
