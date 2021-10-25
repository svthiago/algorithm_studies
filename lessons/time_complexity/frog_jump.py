import math

def solution(X, Y, D):
    G = Y - X
    J = math.ceil(G / D)

    return J
