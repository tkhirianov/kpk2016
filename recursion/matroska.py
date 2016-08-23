def matroska(n):
    if n == 1:
        print('  '*n + 'матрёшечка')
    else:
        print('  '*n + 'матрёшка №', n, '(верх)')
        matroska(n-1)
        print('  '*n + 'матрёшка №', n, '(низ)')

def factorial(n):
    if n == 0:
        return 1
    else:
        print('  '*n + 'n =', n)  # прямой ход рекурсии
        result = factorial(n-1)*n
        print('  '*n + 'n =', n)  # обратный ход рекурсии
        return result

counter = 0

def power(a, n):
    global counter
    counter += 1
    
    if n == 0:
        return 1
    elif n%2 == 0:
        return power(a*a, n//2)
    else:  # n - нечётное
        return power(a, n-1)*a

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

    
