N = 4
m1 = None
for i in range(N):
    x = int(input())
    if x%2 == 0:
        if m1 == None or x > m1:
            m1 = x
if m1 != None:
    print('максимальное чётное', m1)
else:
    print('чётных чисел не было')