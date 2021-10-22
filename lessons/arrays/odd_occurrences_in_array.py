from collections import Counter

def solution(A):
    c = Counter(A)

    for k in c:
        if (c[k] % 2) == 1:
            return k
