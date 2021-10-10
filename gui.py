from tkinter import *
from generate import *
import numpy as np

def clean():
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
    matrix = np.copy(genPuzzle(genSudoku(3), 17))
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
    pass

def solve_sudoku():
    pass

def validate_sudoku():
    pass

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
