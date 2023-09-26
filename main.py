from Arrays.missing_number import MissingNumber
from Arrays.products_except_self import ProductExceptSelf
from Matrix.set_matrix_zeroes import SetMatrixZeroes
from random_problem import chose_random

def main():
   # chose_random() 
    matrix = [
        [0,1,2],
        [4,1,0],
        [1,1,1]
    ]
    zeros = SetMatrixZeroes()
    zeros.setZeroes(matrix)

if __name__ == "__main__":
    main()
