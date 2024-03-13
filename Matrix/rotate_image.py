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


'''
1, 2, 3
4, 5, 6
7, 8, 9


1, 4, 7 
2, 5, 8 
3, 6, 9


7, 4, 1
8, 5, 2
9, 6, 3

'''
