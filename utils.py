import numpy as np
from time import perf_counter

def stopWatch(function):
    def wrapper(*args, **kwargs):
        t1 = perf_counter()
        result = function(*args, **kwargs)
        t2 = perf_counter()
        t = t2-t1
        print(t)
        return result
    return wrapper

def dimMatrix(matrix):
    a = matrix.shape[0]
    b = matrix.shape[1]
    if ((a != b) or (((int(a**0.5))**2) != b)):
        raise ValueError('matrix cannot be divided into blocks')
    else:
        n = int(a**0.5)
        return a, n

def blockConverter(matrix):
    a, n = dimMatrix(matrix)
    region = np.zeros((a,n,n), dtype = np.uint8)
    i = 0
    for j in range(0, a, n):
        for k in range(0, a, n):
            region[i] = matrix[j:j+n, k:k+n]
            i += 1
    return region          

def indexFinder(matrix, x, y):
    a = matrix.shape[0]
    b = matrix.shape[1]
    i = matrix[int(x/a), int(y/b)]
    return i
        
        
        
