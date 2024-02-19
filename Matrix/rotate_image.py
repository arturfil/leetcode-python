from typing import List

class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        mlen = len(matrix)

        # transpose
        for i in range(mlen):
            for j in range(i + 1, mlen):
                matrix[j][i], matrix[i][j]  =  matrix[i][j], matrix[j][i]

        # reflect
        for i in range(mlen):
            for j in range(mlen//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]




