from typing import List

class SetMatrixZeroes:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_val = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        row_val = 0

        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, -1, -1):
                if i == 0:
                    matrix[i][j] *= row_val
                elif matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

