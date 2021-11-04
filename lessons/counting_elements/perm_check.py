def solution(A):
    n = len(A)
    s = set(A)
    cs = set(list(range(1, n+1)))

    if cs.issubset(s):
        return 1
    else:
        return 0
