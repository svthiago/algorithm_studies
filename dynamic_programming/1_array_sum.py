def array_sum(a, i):
    if i >= len(a):
        return 0
    return a[i] + array_sum(a, i+1)

a = [1,2,3,4,5,6]

b = array_sum(a, 0)
print(b)
