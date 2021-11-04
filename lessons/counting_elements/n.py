def solution(N, A):
    c = [0] * N
    m = 0
    for i, n in enumerate(A):
        if i > 0 and A[i-1] > N:
            continue
        elif n <= N:
            c[n-1] += 1
            if c[n-1] > m:
                m = c[n-1]
        elif n > N:
            c = [m] * N
    return c
