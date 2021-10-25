import cProfile
from multiprocessing import Pool
import numpy as np


def tests(path):
    with open(path, 'r') as f:
        inputs = f.read().split('\n')
        for i in inputs:
            s = solution(eval(i))
            print(f"{i} = {s}")

def solution(A):
    a = sum(A[:1])
    b = sum(A[1:])
    s = abs(a - b)

    r = range(1, len(A))
    for i in r:
        n = abs(a - b)
        if n < s:
            s = n
        a += A[i]
        b -= A[i]
    return s


if __name__ == "__main__":
    # checking performance on simple cases
    cProfile.run("tests('tape_equilibrium.txt')")

    # checking performance on big arrays
    a = np.random.randint(-1000,1000,10000)
    cProfile.run("solution(a)")
