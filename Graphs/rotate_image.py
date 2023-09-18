from typing import List

class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        n = len(matrix) # the length of matrix ROWS
        for i in range(n):
            for j in range(i + 1, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] # python swap rotation

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

    

'''
    TESTING
    test_matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rot_img = RotateImage()
    # rot_img.rotate_alt(test_matrix)
    rot_img.rotate(test_matrix)

    AL
'''