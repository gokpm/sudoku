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
def solveSudoku(arg_matrix): #puzzle matrix
    matrix = np.copy(arg_matrix) #work with a copy of the puzzle matrix
    a, n = dimMatrix(matrix) #validate the puzzle matrix for dimensions of a sudoku matrix
    copy_matrix = np.copy(matrix) #work with a copy of the original puzzle matrix for that it can be reverted if back tracking is required
    index_block = np.arange(a).reshape(-1, n) #index matrix
    i = 0 #puzzle matrix row counter
    while i < a:
        numbers = list(np.arange(a) + 1) #allowed numbers
        for j in range(0,a): #puzzle matrix column counter
            if copy_matrix[i,j] in numbers: #if element is present in allowed numbers
                numbers.remove(copy_matrix[i,j]) #remove that element from the allowed numbers, returns all the elements not present in the row of the puzzle matrix
        shuffle(numbers) #shuffle the numbers not present in the row of the puzzle matrix
        permutations_numbers = permutations(numbers) #find the permutations of numbers not present in the row of the puzzle matrix
        for sequence in permutations_numbers: #one sequence at a time (lazily)
            k = 0 #counter to go element by element in each sequence
            count_duplicate = 0 #counter for duplicates
            for j in range(0,a): #puzzle matrix column counter
                if copy_matrix[i,j] == 0: #if an element is not present
                    copy_matrix[i,j] = sequence[k] #enter a corresponding element from the sequence
                    temporary = copy_matrix[i,j] #store the element in a temporary variable so that it is not mistaken for it's duplicate while checking it's row, column and region
                    copy_matrix[i,j] = 0
                    block = blockConverter(copy_matrix) #convert to blocks after making the element under view as 0
                    index = indexFinder(index_block, i, j) #find the index of the region matrix
                    if ((temporary in block[index]) or (temporary in copy_matrix[:, j]) or (temporary in copy_matrix[i, :])): #apply the rules of sudoku. check if the element under view is already present in it's row, column or region
                        count_duplicate += 1 #increment the duplicate counter
                    copy_matrix[i,j] = temporary #reinstate the value into the matrix
                    block = blockConverter(copy_matrix) #divide into regions once the element has been reinstated
                    temporary = None
                    k += 1 #go to the next element in the sequence
            if count_duplicate > 0: #if duplicates are found
                copy_matrix[i] = matrix[i] #remove the entered values and return the row to the defaul puzzle look, i.e as the row of the original puzzle
                continue #go to the next sequence in the permutation of numbers
            else: #if no duplicates are found
                break #do not go to the next sequence
        if count_duplicate > 0: #even after trying all the sequences, if a duplicate is found
            i = 0 #there is no solution to this row, so back track and start from the first row of the puzzle matrix
            copy_matrix = np.copy(matrix) #remove all the entered elements and return the matrix to the default state i.e look of the puzzle matrix
            continue #start from the first row
        i += 1
    return copy_matrix #return the solved matrix
    
#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
#################################################################################

        
        
        
