#################################################################################
#                                                                               #
#                                    start                                      #  
#                                                                               #
#################################################################################

#################################################################################
#                                                                               #
#   category:       script                                                      #
#   title:          solve sudoku                                                #  
#   description:    solve sudoku using permutation of allowed numbers           #
#   modified on:    26-09-2021                                                  #
#   contributed by: @icemelting                                                 #
#                                                                               #
#################################################################################

import numpy as np
from itertools import permutations
from random import shuffle
from utils import *

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        solve sudoku                                                  #  
#   description:  solve sudoku using permutation of allowed numbers             #
#   arguments:    puzzle matrix                                                 #
#   returns:      solved sudoku matrix                                          #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

@stopWatch
def solveSudoku(arg_matrix):
    matrix = np.copy(arg_matrix)
    a, n = dimMatrix(matrix)
    copy_matrix = np.copy(matrix)  # Can be reverted if back tracking is required.
    index_block = np.arange(a).reshape(-1, n)
    i = 0
    while i < a:
        numbers = list(np.arange(a) + 1)
        for j in range(0,a):
            if copy_matrix[i,j] in numbers:
                numbers.remove(copy_matrix[i,j])
        shuffle(numbers)  # Shuffle the numbers not present in the row of the puzzle matrix.
        permutations_numbers = permutations(numbers)
        for sequence in permutations_numbers:  # One sequence at a time (lazy).
            k = 0  # One element at a time in the sequence.
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
                copy_matrix[i] = matrix[i]  # Reset row.
                continue  # Next sequence.
            else:
                break  # Do not start the next sequence.
        if count_duplicate > 0:
            i = 0  # Back tracking.
            copy_matrix = np.copy(matrix)  # Reset matrix.
            continue  # Start from the first row.
        i += 1
    return copy_matrix
    
#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
#################################################################################

        
        
        
