def solution(A):
    b = set(range(1,len(A)+1))
    a = set(A)
    c = b - a
    if c:
        return min(c)
    else:
        return len(A)+1
