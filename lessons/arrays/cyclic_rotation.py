
def solution(A, K):
    if len(A) == 0:
        return A

    r = A
    for _ in range(K):
        aux = []
        aux.append(r[-1])
        aux.extend(r[:-1])
        r = aux

    return r
