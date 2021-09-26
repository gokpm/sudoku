#################################################################################
#                                                                               #
#                                    start                                      #  
#                                                                               #
#################################################################################

#################################################################################
#                                                                               #
#   category:       script                                                      #
#   title:          sudoku matrix checker                                       #  
#   description:    check if a matrix follows all the rules of a sudoku matrix  #
#   modified on:    26-09-2021                                                  #
#   contributed by: @icemelting                                                 #
#                                                                               #
#################################################################################

import numpy as np
from utils import *

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        sudoku matrix checker                                         #  
#   description:  check if a matrix follows all the rules of a sudoku matrix    #
#   arguments:    matrix to be checked                                          #
#   returns:      Boolean                                                       #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

def conformityCheck(arg_matrix):
    matrix = np.copy(arg_matrix)
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
        
#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
################################################################################# 

        
        
        
