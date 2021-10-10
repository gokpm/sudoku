import numpy as np
from utils import *

def conformityCheck(arg_matrix):
    matrix = np.copy(arg_matrix)
    a, n = dimMatrix(matrix)
    count_duplicate = 0
    index_block = np.arange(a).reshape(-1, n)
    for i in range(0,a):  
        for j in range(0,a):
            temporary = matrix[i,j]
            matrix[i,j] = 0  # So that the value is not a duplicate of itself in it's row, column, region.
            block = blockConverter(matrix)
            index = indexFinder(index_block, i, j)
            if ((temporary in block[index]) or (temporary in matrix[:, j]) or (temporary in matrix[i, :])):
                count_duplicate += 1  # Duplicate found.
            matrix[i,j] = temporary
            temporary = None
    if count_duplicate > 0:
        return False
    else:
        return True

        
        
        
