import networkx
import matplotlib.pyplot as plt

def input_edges_list():
    """считывает список рёбер в форме:
    в первой строке N - число рёбер,
    затем следует N строк из двух слов и одного числа
    слова - названия вершин, концы ребра, а число - его вес

    return граф в форме словаря словарей смежности с весами"""
    N = int(input('Введите количество рёбер:'))
    G = {}
    for i in range(N):
        vertex1, vertex2, weight = input().split()
        weight = float(weight)
        # добавляю ребро (vertex1, vertex2)
        if vertex1 not in G:
            G[vertex1] = {vertex2:weight}
        else:  # значит такая вершина уже встречалась
            G[vertex1][vertex2] = weight
        # граф не направленный, поэтому добавляю ребро (vertex2, vertex1)
        if vertex2 not in G:
            G[vertex2] = {vertex1:weight}
        else:  # значит такая вершина уже встречалась
            G[vertex2][vertex1] = weight
    return G

A = networkx.Graph(input_edges_list())
position = networkx.spring_layout(A) # positions for all nodes
networkx.draw(A, position)
networkx.draw_networkx_labels(A, position)
#networkx.draw_networkx_edge_labels(A, position, edge_labels=)

plt.show() # display
