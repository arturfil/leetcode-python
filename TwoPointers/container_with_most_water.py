from typing import List

class ContainerWithMostWater:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height)-1

        while left < right:
            temp_height = min(height[left], height[right])
            temp_area = temp_height * (right-left)
            max_area = max(temp_area, max_area)

            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1

        return max_area
