import networkx
import matplotlib.pyplot as plt

color_list = ['red', 'green', 'blue', 'orange', 'magenta', 'pink', 'cyan']

def edges_list_to_adjacency_list(E):
    """E - граф в форме словаря рёбер и соответствующих им весов
    return граф в форме словаря словарей смежности с весами
    """
    G = {}
    for vertex1, vertex2 in E:
        weight = E[(vertex1, vertex2)]
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


def dfs(G, start, called=set(), skelet=set()):
    called.add(start)
    for neighbour in G[start]:
        if neighbour not in called:
            dfs(G, neighbour, called, skelet)
            skelet.add((start, neighbour))

s = """L B 1
B D 1
B C 2
G J 7
V W 2
N M 2
C L 2
O D 3
G R 1
R T 2
N S 2
Y W 5""".split('\n')
E = {}
for line in s:
    a, b, weight = line.split()
    E[(a, b)] = int(weight)

A = edges_list_to_adjacency_list(E)

G = networkx.Graph(A)
position = networkx.spring_layout(G) # positions for all nodes
networkx.draw(G, position)
networkx.draw_networkx_labels(G, position)

called = set()
count_components = 0
for vertex in A:
    if vertex in called:
        continue
    else:
        # vertex ещё не встречалась ни в одной обойдённой компоненте связности
        skelet = set()
        dfs(A, vertex, called, skelet)
        networkx.draw_networkx_edges(G, position, edgelist=skelet,
                                     width=5, alpha=0.5,
                                     edge_color=color_list[count_components])
        count_components += 1

print('Количество компонент связности:', count_components)

plt.show() # display
