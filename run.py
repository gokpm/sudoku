#################################################################################
#                                                                               #
#                                    start                                      #  
#                                                                               #
#################################################################################

import numpy as np
from time import sleep
from tkinter import *
from generate import *
from solve import *
from check import *

def validate_right_click(event):
    button_validate.config(text = 'Validate', bg = '#f0f0f0')

def clean():
    button_validate.config(text = 'Validate', bg = '#f0f0f0')
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            element[i][j].config(state=NORMAL)
            element[i][j].delete(0, END)
            j += 1
        i += 1
    return

def generate_sudoku():
    clean()
    matrix = np.copy(genPuzzle(genSudoku(3), 60))
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            if matrix[i,j] > 0:
                element[i][j].insert(0, matrix[i,j])
                element[i][j].config(state=DISABLED)
            else:
                pass            
            j += 1
        i += 1
    return

def solve_sudoku():
    matrix = np.zeros((9,9), dtype = np.uint8)
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            try:
                matrix[i,j] = element[i][j].get()
                element[i][j].config(state=DISABLED)
            except ValueError:
                matrix[i,j] = 0
            j += 1
        i += 1
    matrix = np.copy(solveSudoku(matrix))
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            element[i][j].insert(0, matrix[i,j])
            j += 1
        i += 1
    return

def validate_sudoku():
    matrix = np.zeros((9,9), dtype = np.uint8)
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            try:
                matrix[i,j] = element[i][j].get()
                element[i][j].config(state=DISABLED)
            except ValueError:
                matrix[i,j] = 0
            j += 1
        i += 1
    flag = conformityCheck(matrix)
    if flag:
        button_validate.config(text = 'True', bg = '#00ff00')
    else:
        button_validate.config(text = 'False', bg = '#ff0000')
    return

root = Tk()
root.title('Sudoku')

# Sudoku grid.
element = [[], [], [], [], [], [], [], [], []]
i = 0
while i < 9:
    j = 0
    while j < 9:
        element[i].append(Entry(root, width = 3))
        element[i][j].grid(row = i, column = j)
        j += 1
    i += 1       

# Definition of buttons.
button_generate = Button(root,
                         text = 'Generate',
                         width = 10, height = 2, bd = 3,
                         activebackground = '#000000', activeforeground = '#ffffff',
                         command = generate_sudoku)
button_solve = Button(root,
                         text = 'Solve',
                         width = 10, height = 2, bd = 3,
                         activebackground = '#000000', activeforeground = '#ffffff',
                         command = solve_sudoku)
button_validate = Button(root,
                         text = 'Validate',
                         width = 10, height = 2, bd = 3,
                         activebackground = '#000000', activeforeground = '#ffffff',
                         command = validate_sudoku)

button_validate.bind("<Button-3>", validate_right_click)

button_clear = Button(root,
                      text = 'Clear',
                      width = 10, height = 3, bd = 3,
                      activebackground = '#000000', activeforeground = '#ffffff',
                      command = clean)
# Placement of buttons.
button_generate.grid(row = 0, column = 10, rowspan = 2)
button_solve.grid(row = 2, column = 10, rowspan = 2)
button_validate.grid(row = 4, column = 10, rowspan = 2)
button_clear.grid(row = 6, column = 10, rowspan = 3)

root.mainloop()

#################################################################################
#                                                                               #
#                                     end                                       #  
#                                                                               #
################################################################################# 
