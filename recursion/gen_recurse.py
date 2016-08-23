def gen(n, prefix = []):
    if len(prefix) == n:
        print(*prefix)
    else:
        for digit in range(1, n+1):
            if digit not in prefix:
                gen(n, prefix + [digit])

gen(4)
