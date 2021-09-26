#################################################################################
#                                                                               #
#                                    start                                      #  
#                                                                               #
#################################################################################

#################################################################################
#                                                                               #
#   category:       script                                                      #
#   title:          utilities                                                   #  
#   description:    helper functions to run sudoku generator.py and solver.py   #
#   modified on:    26-09-2021                                                  #
#   contributed by: @icemelting                                                 #
#                                                                               #
#################################################################################

import numpy as np
from time import perf_counter

#################################################################################
#                                                                               #
#   category:     decorator                                                     #
#   title:        stopwatch                                                     #  
#   description:  calculate the execution time of a function                    #
#   arguments:    function with any arguments                                   #
#   returns:      value returned by the function                                #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

def stopWatch(function): #function
    def wrapper(*args, **kwargs): #arguments of the function
        t1 = perf_counter()
        result = function(*args, **kwargs) #result of the function
        t2 = perf_counter()
        t = t2-t1
        print(t)
        return result #return the result of the function
    return wrapper #run the wrapper function and return the result of the argument function

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        matrix validation                                             #  
#   description:  check if a matrix is a sudoku matrix                          #
#   arguments:    sudoku matrix                                                 #
#   returns:      size and region size of the sudoku matrix                     #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

def dimMatrix(matrix):
    a = matrix.shape[0] #rows
    b = matrix.shape[1] #columns
    if ((a != b) or (((int(a**0.5))**2) != b)): #row count = column count and row, column is a square of a whole number
        raise ValueError('matrix cannot be divided into blocks')
    else:
        n = int(a**0.5) #region size
        return a, n #size and region size

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        divide sudoku matrix into regions                             #  
#   description:  divide sudoku matrix into blocks and store each block as rows #
#   arguments:    sudoku matrix                                                 #
#   returns:      region matrix (eg. sudoku matrix(9x9) -> region matrix(9x3x3) #
#                 each row in the region matrix is a 3x3 matrix)                #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

def blockConverter(matrix):
    a, n = dimMatrix(matrix) #validate the sudoku matrix
    region = np.zeros((a,n,n), dtype = np.uint8) #init region matrix
    i = 0 #counter for region matrix
    for j in range(0, a, n): #counter for rows of sudoku matrix
        for k in range(0, a, n): #counter for columns of sudoku matrix
            region[i] = matrix[j:j+n, k:k+n] #slice sudoku matrix into regions eg.region[2] = matrix[0:2, 6:9]
            i += 1
    return region  #return region matrix        

#################################################################################
#                                                                               #
#   category:     function                                                      #
#   title:        find an element in the region matrix                          #  
#   description:  find the row in the region matrix that contains the element   #
#                 from the sudoku matrix                                        #
#   arguments:    index matrix (nxn)                                            #
#   returns:      row of the region matrix. each row in the region matrix is a  #
#                 (nxn) matrix                                                  #
#   modified on:  26-09-2021                                                    #
#                                                                               #
#################################################################################

def indexFinder(matrix, x, y): #index matrix and coordinates of sudoku matrix
    a = matrix.shape[0] #row count
    b = matrix.shape[1] #column count
    i = matrix[int(x/a), int(y/b)] #convert coordinates of sudoku matrix to that of region matrix and get the corresponding row value of the region matrix
    return i

#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
#################################################################################       
        
        
