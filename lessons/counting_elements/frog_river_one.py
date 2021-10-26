import cProfile
from multiprocessing import Pool
import numpy as np


def tests(path):
    with open(path, 'r') as f:
        inputs = f.read().split('\n')
        print("="*10)
        for i in inputs:
            s = solution(eval(i))
            print(f"{i} = {s}")
        print("="*10)

def solution(t):
    X = t[0]
    A = t[1]
    s = sum(list(range(1, X+1)))
    
    if X > len(A):
        return -1

    ms = 0
    j = set()
    for i, n in enumerate(A):
        if n not in j:
            j.add(n)
            ms +=n
            if ms == s:
                return i
    return -1

if __name__ == "__main__":
    # checking performance on simple cases
    path = './frog_river_one.txt'
    cProfile.run(f"tests('{path}')")

    # checking performance on big arrays
    # a = np.random.randint(-1000,1000,10000)
    # cProfile.run("solution(a)")
