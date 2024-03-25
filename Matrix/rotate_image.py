from typing import List

class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        mlen = len(matrix)

        # transpose
        for i in range(mlen):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] 

        # reflect on y axis
        for i in range(mlen):
            for j in range(mlen//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j] 


