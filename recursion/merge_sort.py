def merge_sort(A):
    if len(A) <= 1:
        return A
    middle = len(A)//2
    L = merge_sort(A[:middle])
    R = merge_sort(A[middle:])
    return merge(L, R)

def s(A):
    return A if len(A) <= 1 else merge(s(A[:len(A)//2]),
                                       s(A[len(A)//2:]))

def merge(A, B):
    i = 0
    k = 0
    n = 0
    C = [0]*(len(A)+len(B))
    while i < len(A) and k < len(B):
        if A[i] < B[k]:
            C[n] = A[i]
            i += 1
        else:
            C[n] = B[k]
            k += 1
        n += 1
    C[n:] = A[i:] + B[k:]
    return C
    
