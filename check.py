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

def conformityCheck(arg_matrix): #sudoku matrix
    matrix = np.copy(arg_matrix) #work with a copy of the numpy array
    a, n = dimMatrix(matrix) #validate sudoku matrix dimensions
    count_duplicate = 0 #counter to store duplicates
    index_block = np.arange(a).reshape(-1, n) #index matrix
    for i in range(0,a): #row counter for sudoku matrix
        for j in range(0,a): #column counter for sudoku matrix
            temporary = matrix[i,j] #store the value in a temporary variable
            matrix[i,j] = 0 #make the value 0 so that the value is not a duplicate of itself in it's row, column, region
            block = blockConverter(matrix) #convert the sudoku to regions
            index = indexFinder(index_block, i, j) #find the region to check
            if ((temporary in block[index]) or (temporary in matrix[:, j]) or (temporary in matrix[i, :])): #check if the element is present in the row, column or region
                count_duplicate += 1 #increment if a duplicate value is present
            matrix[i,j] = temporary #reinstate the value from temporary variable into the matrix
            temporary = None #destroy the temporary variable
    if count_duplicate > 0:
        return False #return false if duplicates are found
    else:
        return True #return true if the matrix is a sudoku matrix
        
#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
################################################################################# 

        
        
        
