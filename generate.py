#################################################################################
#                                                                               #
#                                    start                                      #  
#                                                                               #
#################################################################################

#################################################################################
#                                                                               #
#   category:       script                                                      #
#   title:          generate                                                    #  
#   description:    generates sudoku and puzzle matrix                          #
#   modified on:    26-09-2021                                                  #
#   contributed by: @icemelting                                                 #
#                                                                               #
#################################################################################

import numpy as np
from itertools import permutations
from random import shuffle
from random import choice
from utils import *

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        generate sudoku                                               #  
#   description:  generate a random sudoku matrix by permutation of allowed     #
#                 numbers                                                       #
#   arguments:    region size                                                   #
#   returns:      sudoku matrix                                                 #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

@stopWatch
def genSudoku(block_size): #region size
    n = block_size #region size
    a = int(n**2) #size of the sudoku matrix
    numbers = list(np.arange(a) + 1) #allowed numbers
    matrix = np.zeros((a,a), dtype = np.uint8) #init sudoku matrix
    index_block = np.arange(a).reshape(-1, n) #init index matrix
    i = 0 #sudoku row counter
    while i < a:
        block = blockConverter(matrix) #convert sudoku matrix into region matrix
        shuffle(numbers) #shuffle allowed numbers for a random behaviour
        index = indexFinder(index_block, i, 0) #find the index of the region matrix
        counter = 0 #counter to check the number of element displacements from front to back
        while (((numbers[0] in block[index,:i%n]) or (numbers[0] in matrix[:i,0])) and counter < a): #move elements to the back if these condtions are satisfied
            numbers.append(numbers.pop(0)) #move the first element to the last
            counter += 1
        if counter == a: #if number of displacement equals the number of elements, then all elements have been tried and no element is remaining
            i = (i//n)*n #there is no solution for this row, so back track to the first row of this block
            matrix[i:, :] = 0 #starting from the block's first row, make everything 0
            continue #again fill values from the block's first row    
        permutations_numbers = permutations(numbers) #permutate the allowed numbers
        for sequence in permutations_numbers: #get one sequence at a time (lazily)
            matrix[i] = sequence #fill the row with the sequence
            block = blockConverter(matrix) #convert the sudoku into regions
            count_duplicate = 0 #counter to check for duplicates
            for j in range(0,a): #sudoku column counter
                temporary = matrix[i,j] #store matrix[i,j] in temporary, so that it doesn't duplicate itself while comparing in it's row, column and region
                matrix[i,j] = 0
                block = blockConverter(matrix) #convert the sudoku into regions after making the element under view as 0
                index = indexFinder(index_block, i, j) #get the index of the region matrix
                if ((temporary in block[index]) or (temporary in matrix[:, j])): #apply rules of sudoku
                    count_duplicate += 1 #increment if duplicates are found in region or column. the same number will not be repeated in the row since all elements in the sequence are unique
                matrix[i,j] = temporary
                temporary = None
            if count_duplicate == 0: #if no duplicates are found in the row after entering a sequence
                break #do not go to the next sequence
        if count_duplicate > 0: #even after trying all the sequences, if duplicates are found
            i = (i//n)*n #there is no solution to this row. so back track to the block's first row
            matrix[i:, :] = 0 #from the block's first row, make everything 0
            continue #continue filling the sequence from the block's first row
        i += 1
    return matrix #return the sudoku matrix

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        generate puzzle                                               #  
#   description:  remove random elements from a sudoku matrix to generate a     #
#                 puzzle                                                        #
#   arguments:    sudoku matrix                                                 #
#   returns:      puzzle matrix                                                 #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

def genPuzzle(arg_matrix, min_clues): #completed sudoku matrix and the min number of elements to retain
    matrix = np.copy(arg_matrix) #work with a copy
    a, n = dimMatrix(matrix) #validate the sudoku matrix for dimensions
    remaining_clues = int(a**2) #counter to track the number of clues remaining
    cache = [] #list to store already removed elements. already removed element should not be removed again. will result in more clues than the minimum number of clues
    while remaining_clues > min_clues: #stop when only min no. of clues are remaining
        i = choice(list(np.arange(a))) #choose a random x value
        j = choice(list(np.arange(a))) #choose a random y value
        x0 = list(matrix[i,:]).count(0) #count the 0's in the row
        y0 = list(matrix[:,j]).count(0) #count the 0's in the column
        if not [i,j] in cache: #if not already seen
            if x0 > a-2 or y0 > a-2: #if no. of 0's in rows or columns is greater than 7
                cache.append([i,j]) #add the location as visited
                continue #next iteration
            else: #if no. of 0's in rows or columns is less than 7
                matrix[i,j] = 0 #remove the clue
                remaining_clues -= 1 #decrement the remaining clues since a clue was removed
                cache.append([i,j]) #add the location as visited
    return matrix #return the puzzle
    
#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
################################################################################# 
        
        
        
