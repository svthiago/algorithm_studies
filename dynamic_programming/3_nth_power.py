def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

p = power(2, 3)

print(p)