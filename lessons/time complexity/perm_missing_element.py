def solution(A):

    B = list(range(1, len(A)+1))
    if len(A) == 1:
        B = [1, 2]

    if len(A) == 0:
        return 1

    C = set(B) - set(A)

    if len(C) == 0:
        return len(A) + 1

    return C.pop()