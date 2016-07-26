from tkinter import *

frame_sleep_time = 1   # задержка между кадрами в милисекундах

cell_width = 10
cell_height = 10
cells_horizontal_number = 100
cells_vertical_number = 100
max_physical_x = cells_horizontal_number
max_physical_y = cells_vertical_number
screen_width = cell_width * cells_horizontal_number    # ширина игрового экрана
screen_height = cell_height * cells_vertical_number    # высота игрового экрана


def screen_x(_physical_x):
    return round(_physical_x * cell_width)


def screen_y(_physical_y):
    return screen_height - round(_physical_y * cell_height)


def physical_x(_screen_x):
    return _screen_x / cell_width


def physical_y(_screen_y):
    return (screen_height - _screen_y) / cell_height


def cell_color(symbol):
    colors = {0: 'white', 1: 'green', ' ': None}
    return colors[symbol]


def cell_outline_color(symbol):
    colors = {0: 'lightgray', 1: 'lightgray', ' ': None}
    return colors[symbol]


class Field:
    def __init__(self, field_file, canvas):
        """загружает поле с клетками из файла"""
        self._canvas = canvas
        with open(field_file) as file:
            self.matrix = [None] * cells_vertical_number
            self.avatars = [None] * cells_vertical_number
            for yi in range(cells_vertical_number):
                self.matrix[yi] = [None] * cells_horizontal_number
                self.avatars[yi] = [None] * cells_horizontal_number
                line = file.readline().rstrip()
                line += ' '*(cells_horizontal_number - len(line))
                for xi in range(cells_horizontal_number):
                    # любой символ, кроме пробела -- значикт соотв. клетка жива
                    is_cell_alive = 0 if line[xi] == ' ' else 1
                    self.matrix[yi][xi] = is_cell_alive
                    self.avatars[yi][xi] = canvas.create_rectangle(screen_x(xi), screen_y(yi),
                                                                   screen_x(xi+1), screen_y(yi+1),
                                                                   fill=cell_color(is_cell_alive),
                                                                   outline=cell_outline_color(is_cell_alive))

    def calculate(self):
        """  """
        # рассчитываем матрицу состояний клеток на следующем шаге
        new_matrix = [[0]*cells_horizontal_number for i in range(cells_vertical_number)]
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                # подсчитаем количество живых соседей
                number_of_neighbours = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        number_of_neighbours += self.matrix[yi+i][xi+j]
                number_of_neighbours -= self.matrix[yi][xi]
                cell_is_alive = self.matrix[yi][xi]
                if (cell_is_alive and number_of_neighbours == 2) or number_of_neighbours == 3:
                    new_matrix[yi][xi] = 1
                else:
                    new_matrix[yi][xi] = 0
        # копируем рассчитанную матрицу в self.matrix
        for yi in range(1, cells_vertical_number-1):
            for xi in range(1, cells_horizontal_number-1):
                if self.matrix[yi][xi] != new_matrix[yi][xi]:
                    self.matrix[yi][xi] = new_matrix[yi][xi]
                    self._canvas.delete(self.avatars[yi][xi])
                    self.avatars[yi][xi] = self._canvas.create_rectangle(screen_x(xi), screen_y(yi),
                                                                         screen_x(xi+1), screen_y(yi+1),
                                                                         fill=cell_color(new_matrix[yi][xi]),
                                                                         outline=cell_outline_color(new_matrix[yi][xi]))


def time_event():
    global scores
    # перевычислить состояние поля с клетками
    field.calculate()
    canvas.after(frame_sleep_time, time_event)


def mouse_move(event):
    pass


def mouse_click(event):
    pass


if __name__ == "__main__":
    root = Tk()
    canvas = Canvas(root, width=screen_width, height=screen_height)
    canvas.pack()
    canvas.bind('<Motion>', mouse_move)

    field = Field('map2.txt', canvas)

    time_event()  # начинаю циклически запускать таймер
    root.mainloop()
