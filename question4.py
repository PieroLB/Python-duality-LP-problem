import numpy as np

def is_the_solution(y, b, x, c):
    return np.dot(y,b) == np.dot(x,c)