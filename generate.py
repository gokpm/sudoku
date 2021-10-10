import numpy as np
from itertools import permutations
from random import shuffle
from random import choice
from utils import *

@stopWatch
def genSudoku(block_size):
    n = block_size
    a = int(n**2)
    numbers = list(np.arange(a) + 1)
    matrix = np.zeros((a,a), dtype = np.uint8)
    index_block = np.arange(a).reshape(-1, n)
    i = 0
    while i < a:
        block = blockConverter(matrix)
        shuffle(numbers)
        index = indexFinder(index_block, i, 0)
        counter = 0  # Number of movements from front to back.
        while (((numbers[0] in block[index,:i%n]) or (numbers[0] in matrix[:i,0])) and counter < a):
            numbers.append(numbers.pop(0))  # Push the first element to the back.
            counter += 1
        if counter == a:  # If number of movements = total number of elements.
            i = (i//n)*n  # Back track to the region's first row.
            matrix[i:, :] = 0  # Reset
            continue   
        permutations_numbers = permutations(numbers)
        for sequence in permutations_numbers:  # One sequence at a time (lazy).
            matrix[i] = sequence
            block = blockConverter(matrix)
            count_duplicate = 0
            for j in range(0,a):
                temporary = matrix[i,j]
                matrix[i,j] = 0
                block = blockConverter(matrix)
                index = indexFinder(index_block, i, j)
                if ((temporary in block[index]) or (temporary in matrix[:, j])):
                    count_duplicate += 1
                matrix[i,j] = temporary
                temporary = None
            if count_duplicate == 0:
                break
        if count_duplicate > 0:
            i = (i//n)*n  # Back track to the region's first row.
            matrix[i:, :] = 0
            continue
        i += 1
    return matrix

def genPuzzle(arg_matrix, min_clues):
    matrix = np.copy(arg_matrix)
    a, n = dimMatrix(matrix)
    remaining_clues = int(a**2)
    cache = []
    while remaining_clues > min_clues:
        i = choice(list(np.arange(a)))  # Choose a random value in x-axis.
        j = choice(list(np.arange(a)))  # Choose a random value in y-axis.
        x0 = list(matrix[i,:]).count(0)
        y0 = list(matrix[:,j]).count(0)
        if not [i,j] in cache:  # If not visited yet.
            if x0 > a-2 or y0 > a-2:
                pass
            else:
                matrix[i,j] = 0
                remaining_clues -= 1
            cache.append([i,j])
    return matrix
