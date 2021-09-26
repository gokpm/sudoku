import numpy as np
from time import perf_counter
from itertools import permutations
from random import shuffle
from random import choice
np.set_printoptions(threshold=np.inf)

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

def genSudoku(block_size):
    n = block_size
    a = int(n**2)
    numbers = list(np.arange(a) + 1)
    sudoku = np.zeros((a,a), dtype = np.uint8)
    index_block = np.arange(a).reshape(-1, n)
    block = blockConverter(sudoku)
    i = 0
    while i < a:
        shuffle(numbers)
        index = indexFinder(index_block, i, 0)
        counter = 0
        while (((numbers[0] in block[index,:i%n]) or (numbers[0] in sudoku[:i,0])) and counter < a):
            numbers.append(numbers.pop(0))
            counter += 1
        if counter == a:
            i = n - 1
            sudoku[i:, :] = 0
            continue
        #print(block[index,:i%n])
        #print(i, numbers, "\n")    
        permutations_numbers = permutations(numbers)
        for sequence in permutations_numbers:
            sudoku[i] = sequence
            block = blockConverter(sudoku)
            count_duplicate = 0
            for j in range(0,a):
                temporary = sudoku[i,j]
                sudoku[i,j] = 0
                block = blockConverter(sudoku)
                index = indexFinder(index_block, i, j)
                if ((temporary in block[index]) or (temporary in sudoku[:, j])):
                    count_duplicate += 1
                sudoku[i,j] = temporary
                temporary = None
                block = blockConverter(sudoku)
            if count_duplicate == 0:
                break
        if count_duplicate > 0:
            i = n - 1
            sudoku[i:, :] = 0
            continue
        i += 1
    return sudoku

def genPuzzle(matrix, min_clues):
    a, n = dimMatrix(matrix)
    remaining_clues = int(a**2)
    cache = []
    while remaining_clues > min_clues:
        i = choice(list(np.arange(a)))
        j = choice(list(np.arange(a)))
        x0 = list(matrix[i,:]).count(0)
        y0 = list(matrix[:,j]).count(0)
        if not [i,j] in cache:
            if x0 > 7 or y0 > 7:
                cache.append([i,j])
                continue
            else:
                matrix[i,j] = 0
                remaining_clues -= 1
                cache.append([i,j])
    return matrix

def conformityCheck(matrix):
    a, n = dimMatrix(matrix)
    count_duplicate = 0
    index_block = np.arange(a).reshape(-1, n)
    for i in range(0,a):
        for j in range(0,a):
            temporary = matrix[i,j]
            matrix[i,j] = 0
            block = blockConverter(matrix)
            index = indexFinder(index_block, i, j)
            if ((temporary in block[index]) or (temporary in matrix[:, j]) or (temporary in matrix[i, :])):
                count_duplicate += 1
            matrix[i,j] = temporary
            temporary = None
    if count_duplicate > 0:
        return False
    else:
        return True

def solveSudoku(matrix):
    a, n = dimMatrix(matrix)
    copy_matrix = np.copy(matrix)
    index_block = np.arange(a).reshape(-1, n)
    i = 0
    while i < a:
        numbers = list(np.arange(a) + 1)
        for j in range(0,a):
            if copy_matrix[i,j] in numbers:
                numbers.remove(copy_matrix[i,j])
        shuffle(numbers)
        permutations_numbers = permutations(numbers)
        for sequence in permutations_numbers:
            k = 0
            count_duplicate = 0
            for j in range(0,a):
                if copy_matrix[i,j] == 0:
                    copy_matrix[i,j] = sequence[k]
                    temporary = copy_matrix[i,j]
                    copy_matrix[i,j] = 0
                    block = blockConverter(copy_matrix)
                    index = indexFinder(index_block, i, j)
                    if ((temporary in block[index]) or (temporary in copy_matrix[:, j]) or (temporary in copy_matrix[i, :])):
                        count_duplicate += 1
                    copy_matrix[i,j] = temporary
                    temporary = None
                    k += 1
            if count_duplicate > 0:
                copy_matrix[i] = matrix[i]
                continue
            else:
                break
        if count_duplicate > 0:
            i = 0
            copy_matrix = np.copy(matrix)
            continue
        i += 1
    return copy_matrix
                                                                  
if __name__ == '__main__':
    sudoku = genSudoku(3)
    copy_sudoku = np.copy(sudoku)
    puzzle = genPuzzle(copy_sudoku, 17)
    copy_puzzle = np.copy(puzzle)
    solved_sudoku = solveSudoku(copy_puzzle)
    print(np.array_equal(sudoku, solved_sudoku))
    print(sudoku)
    print(solved_sudoku)
        
        
        
