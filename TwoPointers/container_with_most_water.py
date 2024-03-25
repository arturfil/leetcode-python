from typing import List

class ContainerWithMostWater:

    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height)-1
        
        while left < right:
            min_height = min(height[left], height[right])
            base = right - left
            area = min_height * base

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            max_area = max(max_area, area)

        return max_area

         

        
