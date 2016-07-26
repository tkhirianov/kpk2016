# -. coding: utf8 .-
__author__ = "Timofey Khirianov"

N = 150

def cell_calculate(left, current, right):
    return left^right

def calculate_field(field):
    """field -- список из N ноликов или единичек"""
    new_field = [0]*N
    for i in range(1, N-1):
        new_field[i] = cell_calculate(field[i-1], field[i], field[i+1])
    field[:] = new_field

def generate_field():
    field = [0]*N
    x = N//2
    field[x] = 1
    return field

def print_field(field):
    for cell in field:
        print('۞' if cell else ' ' , end = '')
    print()
    
def modelling():
    """ цикл моделирования клеточного автомата """
    field = generate_field()
    print_field(field)
    for t in range(50):
        calculate_field(field)
        print_field(field)

if __name__ == '__main__':
    modelling()
