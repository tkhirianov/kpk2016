# field = " "*9
#координаты хода -- индекс позиции в строке: от 0 до 8
players = ['X', '0']
player = 0


def print_field(field):
    print(*field[:3])
    print(*field[3:6])
    print(*field[6:])


def do_turn(field, x, player):
    return field[:x] + players[player] + field[x+1:]


def ai_choice(field, player):
    """ возвращает координаты хода AI """
    # FIXME: тут нужно реализовать рекурсивный искусственный интеллект
    return 0


def human_choice(field, player):
    """ возвращает координаты хода AI """
    # FIXME: нельзя вводить тот номер клетки, где уже есть символ (кроме .)
    return int(input("Введите номер клетки (от 0 до 8): "))


def won(field, player):
    """ определяет, выиграл ли игрок с номером player
    """
    char = players[player]
    lines = 0
    lines += (field[0:3] == char*3)
    lines += (field[3:6] == char*3)
    lines += (field[6:9] == char*3)
    lines += (field[0::3] == char*3)
    lines += (field[1::3] == char*3)
    lines += (field[2::3] == char*3)
    lines += (field[2::3] == char*3)
    lines += (field[0::4] == char*3)  # главная диагональ
    lines += (field[2::2] == char*3)  # вторая диагональ
    return lines > 0


def game_over(field):
    """ определяет, закончилась ли игра (любым результатом, включая ничью)"""
    if (field.find('.') == -1  # ничья
        or won(field, 0) or won(field, 1)):
        return True
    else:
        return False


def tournir():
    field = "."*9
    while True:
        print_field(field)
        x = human_choice(field, 0)
        field = do_turn(field, x, 0)
        if game_over(field):
            break

        print_field(field)
        x = human_choice(field, 1)
        field = do_turn(field, x, 1)
        if game_over(field):
            break
    print_field(field)
    print('победил кто-то...')

if __name__ == '__main__':
    tournir()