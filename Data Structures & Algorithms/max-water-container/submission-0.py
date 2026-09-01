class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(heights) - 1

        while left < right:

            area = min(heights[right], heights[left]) * (right - left)
            maxArea = max(area, maxArea)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return maxArea

        