from typing import List

class TrappingRainWater:
    def trap(self, height: List[int]) -> int:
    
        volume, left, right = 0, 0, len(height)-1
        lmax, rmax = height[0], height[-1]

        while left < right:
            if height[left] > lmax: lmax = height[left]
            if height[right] > rmax: rmax = height[right]

            if  lmax <= rmax:
                volume += lmax - height[left]
                left += 1
            else:
                volume += rmax - height[right]
                right -= 1

        return volume

