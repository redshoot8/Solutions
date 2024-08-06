from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        left = 0
        right = len(height) - 1

        max_height = max(height)

        while left != right:
            S = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, S)

            if max_height * (right - left) <= max_area:
                break

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
