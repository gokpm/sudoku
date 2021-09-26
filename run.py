from generate import *
from solve import *
from check import *
from utils import *
np.set_printoptions(threshold=np.inf)
                                            
if __name__ == '__main__':
    sudoku = genSudoku(3)
    puzzle = genPuzzle(sudoku, 60)
    solved_puzzle = solveSudoku(puzzle)
    print(solved_puzzle)
        
        
        
