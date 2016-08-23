def find_shortest_path(price, n):
    C = [float('inf'), price[1]] + [0]*(n-1)
    for i in range(2, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    print(*enumerate(C))

    path = [n]
    i = n
    while i != 1:
        if C[i-1] < C[i-2]:
            i = i-1
        else:
            i = i-2
        path.append(i)
    path[:] = path[::-1]
    return path

price = [0, 10, 2, 2, 1, 6, 2, 3, 0, 1, 3]
path = find_shortest_path(price, 10)
