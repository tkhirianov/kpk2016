
def sort_test(my_sort):
    import random

    A = [1, 2, 3, 4, 5, 6]
    A_ans = [1, 2, 3, 4, 5, 6]
    my_sort(A)
    print('test case #1: ' + ('OK' if A == A_ans else 'Fail'))

    A = [-1, -2, -3, -4, -5, -6]
    A_ans = [-6, -5, -4, -3, -2, -1]
    my_sort(A)
    print('test case #2: ' + ('OK' if A == A_ans else 'Fail'))

    A = [-1, 2, -3, 4, -5, 6]
    A_ans = [-5, -3, -1, 2, 4, 6]
    my_sort(A)
    print('test case #3: ' + ('OK' if A == A_ans else 'Fail'))

    A = [1000]
    A_ans = [1000]
    my_sort(A)
    print('test case #4: ' + ('OK' if A == A_ans else 'Fail'))

    A = []
    A_ans = []
    my_sort(A)
    print('test case #5: ' + ('OK' if A == A_ans else 'Fail'))

    A = [5]*100
    A_ans = [5]*100
    my_sort(A)
    print('test case #6: ' + ('OK' if A == A_ans else 'Fail'))

    A = [random.randint(1, 100) for i in range(1000)]
    A_ans = sorted(A)
    my_sort(A)
    print('test case #7: ' + ('OK' if A == A_ans else 'Fail'))

    A = [[2], [1], [3], [5], [4], [5]]
    A_ans = sorted(A)
    my_sort(A)
    print('test case #8: ' + ('OK' if A == A_ans else 'Fail'))



def do_nothing(A):
    pass


def bubble_sort(A):
    N = len(A)
    for prohod in range(1, N):
        for i in range(N-prohod):
            if A[i] > A[i+1]:
                tmp = A[i]
                A[i] = A[i+1]
                A[i+1] = tmp


def choice_sort(A):
    N = len(A)
    for pos in range(0, N-1):
        for i in range(pos+1, N):
            if A[i] < A[pos]:
                A[pos], A[i] = A[i], A[pos]


def insert_sort(A):
    N = len(A)
    for pos in range(1, N):
        # УВЕРЕН, что список отсортирован в позициях с 0-й по (pos-1)-ю включительно
        i = 0
        while A[i] < A[pos]:
            i += 1
        # УВЕРЕН, что i указывает на элемент не меньше вставляемого
        tmp = A[pos]
        for k in range(pos-1, i-1, -1):
            A[k+1] = A[k]
        A[i] = tmp
        # УВЕРЕН, что список отсортирован в позициях с 0-й по pos-ю включительно

if __name__ == '__main__':
    print('Test Bubble Sort:')
    sort_test(bubble_sort)
    print('Test Choice Sort:')
    sort_test(choice_sort)
    print('Test Insert Sort:')
    sort_test(insert_sort)

