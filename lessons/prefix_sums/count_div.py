
def solution(A, B, K):
    if A == B:
        if A % K == 0:
            return 1
        return 0

    N = range(A, B+1)
    for n in N:
        if n % K == 0:
            return len(range(n, B+1, K))
