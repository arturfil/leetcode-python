from typing import List

class SpiralMatrix:
    def generate_matrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        up,   down  = 0, n-1
        left, right = 0, n-1
        val = 1
        
        while left <= right:
            
            for col in range(left, right+1):
                matrix[up][col] = val
                val += 1
            up += 1    
    
            for row in range(up, down+1):
                matrix[row][right] = val
                val += 1
            right -= 1

            for col in range(right, left-1, -1):
                matrix[down][col] = val
                val += 1
            down -= 1

            for row in range(down, up-1, -1):
                matrix[row][left] = val
                val += 1
            left += 1
        
        return matrix