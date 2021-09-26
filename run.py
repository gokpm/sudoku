from generate import *
from solve import *
from check import *
from utils import *
np.set_printoptions(threshold=np.inf)
                                            
if __name__ == '__main__':
    z = 1
    while z<101:
        sudoku = genSudoku(3)
        print(z, conformityCheck(sudoku))
        z += 1

        
        
        
