def index_sum(a, i):
    if i > len(a):
        return []
    return [sum(a[:i])] + index_sum(a, i+1)

a = [1,2,3,4,5,6]

b = index_sum(a, 1)
print(b)
