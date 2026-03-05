class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h*w)
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
        
        return max_area
